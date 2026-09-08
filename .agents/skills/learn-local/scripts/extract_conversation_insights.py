#!/usr/bin/env python3
"""
extract_conversation_insights.py

Extracts actionable feedback, user corrections, friction points, and tool errors
from Antigravity conversation transcripts (transcript.jsonl) to guide local
project agent introspection and rule adaptations.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


def sync_opencode_doc_submodule(repo_dir: Path) -> bool:
    """Updates the docs/opencode git submodule if present."""
    git_modules = repo_dir / ".gitmodules"
    if git_modules.exists() and (repo_dir / ".git").exists():
        try:
            res = subprocess.run(
                ["git", "submodule", "update", "--init", "--recursive", "--remote", "docs/opencode"],
                cwd=repo_dir,
                capture_output=True,
                text=True,
                timeout=30
            )
            return res.returncode == 0
        except Exception:
            return False
    return False


def find_latest_transcript_dir(app_data_dir: Path) -> Optional[Path]:
    """Finds the most recently modified brain conversation transcript directory."""
    brain_dir = app_data_dir / "brain"
    if not brain_dir.exists():
        return None

    candidate_dirs = []
    for conv_dir in brain_dir.iterdir():
        if conv_dir.is_dir():
            log_dir = conv_dir / ".system_generated" / "logs"
            transcript_file = log_dir / "transcript.jsonl"
            if transcript_file.exists():
                try:
                    mtime = transcript_file.stat().st_mtime
                    candidate_dirs.append((mtime, log_dir))
                except OSError:
                    continue

    if not candidate_dirs:
        return None

    candidate_dirs.sort(key=lambda x: x[0], reverse=True)
    return candidate_dirs[0][1]


def parse_transcript(transcript_path: Path) -> List[Dict[str, Any]]:
    """Reads a transcript.jsonl file and parses all JSON steps."""
    steps = []
    if not transcript_path.exists():
        return steps

    with open(transcript_path, "r", encoding="utf-8", errors="replace") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                steps.append(data)
            except json.JSONDecodeError:
                continue
    return steps


def analyze_conversation(steps: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyzes transcript steps to extract user inputs, errors, and subagent invocations."""
    user_inputs = []
    tool_failures = []
    subagents_spawned = []
    corrections_detected = []

    correction_keywords = [
        "non", "pas comme ca", "arrete", "erreur", "mauvais", "attends", "refais",
        "corrige", "modifie", "attention", "pourquoi", "probleme", "echec", "bug",
        "no", "stop", "wrong", "fail", "fix", "wait", "dont", "do not"
    ]

    for step in steps:
        step_type = step.get("type", "")
        source = step.get("source", "")
        content = step.get("content", "")
        status = step.get("status", "")
        step_idx = step.get("step_index", 0)

        if step_type == "USER_INPUT" or source == "USER_EXPLICIT":
            text_str = str(content)
            user_inputs.append({"step_index": step_idx, "content": text_str})
            
            lower_text = text_str.lower()
            if any(kw in lower_text for kw in correction_keywords):
                corrections_detected.append({
                    "step_index": step_idx,
                    "content": text_str
                })

        if status == "ERROR":
            tool_failures.append({
                "step_index": step_idx,
                "type": step_type,
                "content": str(content)[:300]
            })

        tool_calls = step.get("tool_calls", [])
        if isinstance(tool_calls, list):
            for tc in tool_calls:
                if isinstance(tc, dict):
                    tool_name = tc.get("name", "")
                    if tool_name == "invoke_subagent":
                        subagents_spawned.append({
                            "step_index": step_idx,
                            "args": tc.get("parameters", tc.get("args", {}))
                        })

    return {
        "total_steps": len(steps),
        "total_user_messages": len(user_inputs),
        "user_inputs": user_inputs,
        "corrections_detected": corrections_detected,
        "tool_failures": tool_failures,
        "subagents_spawned": subagents_spawned
    }


def generate_markdown_report(analysis: Dict[str, Any], conversation_id: str) -> str:
    """Formats the extracted insights into a clean Markdown document."""
    lines = [
        f"# Conversation Introspection & Feedback Report",
        f"",
        f"- Conversation ID: `{conversation_id}`",
        f"- Total Steps: {analysis['total_steps']}",
        f"- User Messages: {analysis['total_user_messages']}",
        f"- Detected User Corrections/Alerts: {len(analysis['corrections_detected'])}",
        f"- Tool Failures/Errors: {len(analysis['tool_failures'])}",
        f"- Subagents Invoked: {len(analysis['subagents_spawned'])}",
        f"",
        f"---",
        f"",
        f"## 1. User Directives & Corrections",
        f""
    ]

    if analysis["corrections_detected"]:
        for item in analysis["corrections_detected"]:
            lines.append(f"### [Step {item['step_index']}]")
            lines.append(f"> {item['content']}")
            lines.append(f"")
    else:
        lines.append("Aucune correction explicite directe detectee par mots-cles.")
        lines.append("")

    lines.extend([
        f"## 2. All User Messages Chronology",
        f""
    ])

    for item in analysis["user_inputs"]:
        lines.append(f"- **Step {item['step_index']}** : {item['content']}")

    lines.extend([
        f"",
        f"---",
        f"",
        f"## 3. Tool Errors and Friction Points",
        f""
    ])

    if analysis["tool_failures"]:
        for fail in analysis["tool_failures"]:
            lines.append(f"- **Step {fail['step_index']}** ({fail['type']}): `{fail['content']}`")
    else:
        lines.append("Aucun echec critique d'outil enregistre.")

    lines.extend([
        f"",
        f"---",
        f"",
        f"## 4. Subagent Activity",
        f""
    ])

    if analysis["subagents_spawned"]:
        for spawn in analysis["subagents_spawned"]:
            lines.append(f"- **Step {spawn['step_index']}**: `invoke_subagent` -> `{spawn['args']}`")
    else:
        lines.append("Aucune invocation directe de sous-agent detectee.")

    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Extract conversation insights for agent introspection.")
    parser.add_argument("--conv-id", help="Specific conversation ID to analyze")
    parser.add_argument("--transcript", help="Direct path to transcript.jsonl")
    parser.add_argument("--app-data-dir", default=os.path.expanduser("~/.gemini/antigravity-cli"),
                        help="Path to Antigravity CLI app data directory")
    parser.add_argument("--json", action="store_true", help="Output raw JSON analysis")
    args = parser.parse_args()

    sync_opencode_doc_submodule(Path.cwd())

    app_data_dir = Path(args.app_data_dir)
    transcript_path: Optional[Path] = None
    conv_id = args.conv_id or "latest"

    if args.transcript:
        transcript_path = Path(args.transcript)
    elif args.conv_id:
        transcript_path = app_data_dir / "brain" / args.conv_id / ".system_generated" / "logs" / "transcript.jsonl"
    else:
        log_dir = find_latest_transcript_dir(app_data_dir)
        if log_dir:
            transcript_path = log_dir / "transcript.jsonl"
            conv_id = log_dir.parent.parent.name

    if not transcript_path or not transcript_path.exists():
        print(f"Error: Transcript file not found: {transcript_path}", file=sys.stderr)
        sys.exit(1)

    steps = parse_transcript(transcript_path)
    analysis = analyze_conversation(steps)

    if args.json:
        print(json.dumps(analysis, indent=2))
    else:
        report = generate_markdown_report(analysis, conv_id)
        print(report)


if __name__ == "__main__":
    main()
