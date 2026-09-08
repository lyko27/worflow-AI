#!/usr/bin/env python3
"""
extract_conversation_insights.py

Extracts actionable feedback, user corrections, friction points, and tool errors
from OpenCode sessions and conversation logs (with fallback to Agy transcripts)
to guide local agent introspection and rule adaptations.

Automatically ensures the docs/opencode git submodule is synchronized.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


def sync_opencode_doc_submodule(repo_dir: Path) -> bool:
    """Updates the docs/opencode git submodule to the latest remote state."""
    git_modules = repo_dir / ".gitmodules"
    doc_submodule = repo_dir / "docs" / "opencode"
    if git_modules.exists() and (repo_dir / ".git").exists():
        try:
            print("[SYNC] Verification et mise a jour du sous-module docs/opencode...")
            res = subprocess.run(
                ["git", "submodule", "update", "--init", "--recursive", "--remote", "docs/opencode"],
                cwd=repo_dir,
                capture_output=True,
                text=True,
                timeout=30
            )
            if res.returncode == 0:
                print("  [OK] Documentation OpenCode synchronisee.")
                return True
            else:
                print(f"  [WARN] Note synchronisation submodule: {res.stderr.strip()}")
        except Exception as e:
            print(f"  [WARN] Impossible d'actualiser le sous-module: {e}")
    return False


def find_latest_agy_transcript(app_data_dir: Path) -> Optional[Path]:
    """Fallback: finds the most recently modified Agy conversation transcript."""
    brain_dir = app_data_dir / "brain"
    if not brain_dir.exists():
        return None

    candidate_files = []
    for conv_dir in brain_dir.iterdir():
        if conv_dir.is_dir():
            log_file = conv_dir / ".system_generated" / "logs" / "transcript.jsonl"
            if log_file.exists():
                try:
                    mtime = log_file.stat().st_mtime
                    candidate_files.append((mtime, log_file))
                except OSError:
                    continue

    if not candidate_files:
        return None

    candidate_files.sort(key=lambda x: x[0], reverse=True)
    return candidate_files[0][1]


def find_opencode_session_file(project_dir: Path) -> Optional[Path]:
    """Finds OpenCode session export or log files in project or user directory."""
    # 1. Check project directory exports
    for name in ["session.json", "opencode_session.json", ".opencode_session.json"]:
        p = project_dir / name
        if p.exists():
            return p

    # 2. Check .opencode/ directory
    opencode_dir = project_dir / ".opencode"
    if opencode_dir.exists():
        for p in opencode_dir.glob("*.json"):
            if "config" not in p.name and "opencode" != p.stem:
                return p

    # 3. Check ~/.local/share/opencode/
    user_share = Path(os.path.expanduser("~/.local/share/opencode"))
    if user_share.exists():
        candidates = []
        for p in user_share.rglob("*.json"):
            try:
                candidates.append((p.stat().st_mtime, p))
            except OSError:
                continue
        if candidates:
            candidates.sort(key=lambda x: x[0], reverse=True)
            return candidates[0][1]

    return None


def parse_session_or_transcript(file_path: Path) -> List[Dict[str, Any]]:
    """Parses JSON or JSONL file into a list of normalized steps/messages."""
    items = []
    if not file_path.exists():
        return items

    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read().strip()

    if not content:
        return items

    # Try full JSON parse (OpenCode session format)
    if content.startswith("{") or content.startswith("["):
        try:
            parsed = json.loads(content)
            if isinstance(parsed, list):
                return parsed
            if isinstance(parsed, dict):
                # Common OpenCode session structures
                if "messages" in parsed and isinstance(parsed["messages"], list):
                    return parsed["messages"]
                if "history" in parsed and isinstance(parsed["history"], list):
                    return parsed["history"]
                return [parsed]
        except json.JSONDecodeError:
            pass

    # Try JSONL line-by-line parse
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
            items.append(data)
        except json.JSONDecodeError:
            continue

    return items


def analyze_interactions(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyzes conversation messages to identify corrections, errors, and subagents."""
    user_messages = []
    tool_errors = []
    subagents_mentioned = []
    corrections = []

    correction_keywords = [
        "non", "pas comme ca", "arrete", "erreur", "mauvais", "attends", "refais",
        "corrige", "modifie", "attention", "pourquoi", "probleme", "echec", "bug",
        "no", "stop", "wrong", "fail", "fix", "wait", "dont", "do not"
    ]

    for idx, item in enumerate(items, 1):
        # Extract text content
        role = item.get("role", "")
        item_type = item.get("type", "")
        status = item.get("status", "")
        content = item.get("content", item.get("text", item.get("message", "")))

        text_str = str(content) if content else ""

        is_user = (role == "user" or item_type == "USER_INPUT" or item.get("source") == "USER_EXPLICIT")
        if is_user and text_str:
            user_messages.append({"index": idx, "text": text_str})
            lower_text = text_str.lower()
            if any(kw in lower_text for kw in correction_keywords):
                corrections.append({"index": idx, "text": text_str[:250]})

            # Detect subagent mentions
            for sub in ["@coder", "@researcher", "@ui-tester", "@pedagogue", "@general"]:
                if sub in lower_text and sub not in subagents_mentioned:
                    subagents_mentioned.append(sub)

        # Detect errors
        if status == "ERROR" or item.get("is_error") or "error" in item:
            tool_errors.append({
                "index": idx,
                "error": text_str[:250] or str(item.get("error", ""))[:250]
            })

    return {
        "total_items": len(items),
        "user_messages_count": len(user_messages),
        "corrections": corrections,
        "tool_errors": tool_errors,
        "subagents_mentioned": subagents_mentioned
    }


def main():
    parser = argparse.ArgumentParser(description="Extract insights from OpenCode/Agy sessions.")
    parser.add_argument("--file", help="Path to specific session JSON or transcript JSONL file")
    parser.add_argument("--project-dir", default=os.getcwd(), help="Path to current project root")
    parser.add_argument("--no-sync", action="store_true", help="Skip automatic git submodule sync")
    args = parser.parse_args()

    project_dir = Path(args.project_dir).expanduser().resolve()

    print("=== OpenCode / Agy Session Introspection ===")
    print(f"Project Directory : {project_dir}")

    # Synchronize doc submodule unless disabled
    if not args.no_sync:
        sync_opencode_doc_submodule(project_dir)

    target_file = None
    if args.file:
        target_file = Path(args.file).expanduser().resolve()
    else:
        # Check for OpenCode session file first
        target_file = find_opencode_session_file(project_dir)
        # Fallback to Agy transcript
        if not target_file:
            target_file = find_latest_agy_transcript(Path(os.path.expanduser("~/.gemini/antigravity-cli")))

    if not target_file or not target_file.exists():
        print("Notice: Aucune session recente trouvee. Analyse de base de la structure des agents.")
        print(f"Agents configures dans {project_dir / '.opencode' / 'agents'} :")
        agents_dir = project_dir / ".opencode" / "agents"
        if agents_dir.exists():
            for ag in sorted(agents_dir.glob("*.md")):
                print(f"  - @{ag.stem}")
        sys.exit(0)

    print(f"Source Session    : {target_file}")
    items = parse_session_or_transcript(target_file)
    insights = analyze_interactions(items)

    print(f"Interactions      : {insights['total_items']} evenements ({insights['user_messages_count']} messages utilisateur)")
    print(f"Corrections       : {len(insights['corrections'])} detectees")
    print(f"Erreurs d'outils  : {len(insights['tool_errors'])} detectees")
    print(f"Sous-agents vus   : {', '.join(insights['subagents_mentioned']) or 'aucun'}")
    print("")

    if insights["corrections"]:
        print("Signaux de correction utilisateur cles :")
        for c in insights["corrections"][:5]:
            print(f"  - [Msg #{c['index']}] {c['text']}")
        print("")

    if insights["tool_errors"]:
        print("Erreurs techniques recentes a corriger :")
        for e in insights["tool_errors"][:5]:
            print(f"  - [Err #{e['index']}] {e['error']}")
        print("")

    print("Recommandations d'adaptation :")
    if insights["corrections"]:
        print("  * Considerer d'ajouter les preferences utilisateur explicites dans .opencode/AGENTS.md.")
    if insights["tool_errors"]:
        print("  * Verifier les autorisations d'outils et chemins d'acces dans .opencode/opencode.json.")
    print("  * Consulter docs/opencode/README.md pour les conventions de syntaxe avancees.")


if __name__ == "__main__":
    main()
