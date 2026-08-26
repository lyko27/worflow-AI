#!/usr/bin/env python3
"""
distill_workflow.py

Distills universal, domain-agnostic workflow improvements from a completed
or active project and synchronizes them cleanly to the central base workflow
repository (and optionally ~/.gemini/config/).

Ensures strict sanitization to prevent project-specific logic, absolute paths,
or proprietary business domain rules from polluting the base workflow.
"""

import argparse
import difflib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


DEFAULT_BASE_DIR = os.environ.get(
    "WORKFLOW_BASE_DIR",
    "/home/lyko/Dossier-perso/workflow"
)

# Patterns that indicate project-specific data that must NOT leak to base workflow
SENSITIVE_PATTERNS = [
    r"api[_-]?key\s*[:=]\s*['\"][^'\"]+['\"]",
    r"bearer\s+[a-zA-Z0-9_\-\.]{15,}",
    r"password\s*[:=]\s*['\"][^'\"]+['\"]",
    r"secret\s*[:=]\s*['\"][^'\"]+['\"]",
    r"localhost:[0-9]{4,5}",
]


def detect_base_repository(explicit_path: Optional[str] = None) -> Path:
    """Finds and validates the central workflow repository path."""
    if explicit_path:
        base_path = Path(explicit_path).expanduser().resolve()
    else:
        base_path = Path(DEFAULT_BASE_DIR).expanduser().resolve()

    if not base_path.exists():
        raise FileNotFoundError(f"Central workflow directory not found: {base_path}")
    
    agents_md = base_path / "AGENTS.md"
    setup_sh = base_path / "setup_agents.sh"
    if not (agents_md.exists() or setup_sh.exists()):
        raise ValueError(f"Directory {base_path} does not appear to be a valid Antigravity workflow base.")

    return base_path


def sanitize_content(content: str, source_dir: Path, base_dir: Path) -> Tuple[str, List[str]]:
    """Checks for project-specific leaks and removes hardcoded project paths."""
    warnings = []
    
    for pattern in SENSITIVE_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            warnings.append(f"Potential secret/sensitive token detected: {matches[0][:20]}...")

    # Replace local absolute workspace paths with generic placeholders if source differs from base
    if source_dir.resolve() != base_dir.resolve():
        proj_path_str = str(source_dir.resolve())
        if proj_path_str in content:
            content = content.replace(proj_path_str, "<PROJECT_ROOT>")
            warnings.append(f"Replaced local absolute path '{proj_path_str}' with '<PROJECT_ROOT>'.")

    return content, warnings


def compare_and_distill_files(source_dir: Path, base_dir: Path) -> Dict[str, Any]:
    """Compares local .agents and AGENTS.md with base workflow repo."""
    results = {
        "identical": [],
        "modified": [],
        "new_in_project": [],
        "warnings": []
    }

    relative_files_to_check = [
        Path("AGENTS.md"),
        Path(".agents/mcp_config.json"),
    ]

    # Add all subagent definitions
    source_agents_dir = source_dir / ".agents" / "agents"
    if source_agents_dir.exists():
        for agent_file in source_agents_dir.rglob("*.md"):
            rel_path = agent_file.relative_to(source_dir)
            relative_files_to_check.append(rel_path)

    # Add all skill definitions
    source_skills_dir = source_dir / ".agents" / "skills"
    if source_skills_dir.exists():
        for skill_file in source_skills_dir.rglob("*"):
            if skill_file.is_file():
                rel_path = skill_file.relative_to(source_dir)
                relative_files_to_check.append(rel_path)

    for rel_path in relative_files_to_check:
        source_file = source_dir / rel_path
        base_file = base_dir / rel_path

        if not source_file.exists():
            continue

        try:
            with open(source_file, "r", encoding="utf-8", errors="replace") as sf:
                source_content = sf.read()
        except OSError as e:
            results["warnings"].append(f"Could not read {source_file}: {e}")
            continue

        sanitized_content, file_warnings = sanitize_content(source_content, source_dir, base_dir)
        for w in file_warnings:
            results["warnings"].append(f"{rel_path}: {w}")

        if not base_file.exists():
            results["new_in_project"].append({
                "path": str(rel_path),
                "sanitized_content": sanitized_content
            })
        else:
            try:
                with open(base_file, "r", encoding="utf-8", errors="replace") as bf:
                    base_content = bf.read()
            except OSError as e:
                results["warnings"].append(f"Could not read base file {base_file}: {e}")
                continue

            if sanitized_content == base_content:
                results["identical"].append(str(rel_path))
            else:
                diff = list(difflib.unified_diff(
                    base_content.splitlines(),
                    sanitized_content.splitlines(),
                    fromfile=f"base/{rel_path}",
                    tofile=f"local/{rel_path}",
                    lineterm=""
                ))
                results["modified"].append({
                    "path": str(rel_path),
                    "sanitized_content": sanitized_content,
                    "diff": "\n".join(diff)
                })

    return results


def apply_distillation(diff_results: Dict[str, Any], base_dir: Path, commit_msg: Optional[str] = None) -> List[str]:
    """Applies distilled changes to the base workflow repo and creates a git commit."""
    applied_files = []

    for item in diff_results["modified"]:
        rel_path = Path(item["path"])
        target_path = base_dir / rel_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(item["sanitized_content"])
        applied_files.append(str(rel_path))

    for item in diff_results["new_in_project"]:
        rel_path = Path(item["path"])
        target_path = base_dir / rel_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(item["sanitized_content"])
        applied_files.append(str(rel_path))

    if applied_files and (base_dir / ".git").exists():
        try:
            # Stage updated files
            subprocess.run(["git", "add"] + applied_files, cwd=base_dir, check=True, capture_output=True)
            
            # Check if there are staged changes
            status_out = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=base_dir)
            if status_out.returncode != 0:
                default_msg = f"feat(workflow): distillation des ameliorations du workflow ({len(applied_files)} fichiers)"
                msg = commit_msg or default_msg
                subprocess.run(["git", "commit", "-m", msg], cwd=base_dir, check=True, capture_output=True)
        except subprocess.SubprocessError as e:
            print(f"Warning: Git commit in base repo failed: {e}", file=sys.stderr)

    return applied_files


def sync_to_global_config(base_dir: Path, global_config_dir: Path) -> List[str]:
    """Optionally syncs base agents and skills to ~/.gemini/config/."""
    synced = []
    if not global_config_dir.exists():
        return synced

    # Sync agents
    base_agents = base_dir / ".agents" / "agents"
    target_agents = global_config_dir / "agents"
    if base_agents.exists():
        target_agents.mkdir(parents=True, exist_ok=True)
        for agent_file in base_agents.rglob("*.md"):
            rel = agent_file.relative_to(base_agents)
            dest = target_agents / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            with open(agent_file, "r", encoding="utf-8") as src, open(dest, "w", encoding="utf-8") as dst:
                dst.write(src.read())
            synced.append(f"agents/{rel}")

    # Sync skills
    base_skills = base_dir / ".agents" / "skills"
    target_skills = global_config_dir / "skills"
    if base_skills.exists():
        target_skills.mkdir(parents=True, exist_ok=True)
        for skill_file in base_skills.rglob("*"):
            if skill_file.is_file():
                rel = skill_file.relative_to(base_skills)
                dest = target_skills / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                with open(skill_file, "r", encoding="utf-8", errors="replace") as src, open(dest, "w", encoding="utf-8") as dst:
                    dst.write(src.read())
                synced.append(f"skills/{rel}")

    return synced


def main():
    parser = argparse.ArgumentParser(description="Distill and synchronize workflow improvements to core repository.")
    parser.add_argument("--base-dir", default=DEFAULT_BASE_DIR,
                        help=f"Path to central base workflow repository (default: {DEFAULT_BASE_DIR})")
    parser.add_argument("--source-dir", default=os.getcwd(),
                        help="Path to current project root (default: cwd)")
    parser.add_argument("--apply", action="store_true",
                        help="Apply distilled changes to the base workflow repository and create a commit")
    parser.add_argument("--sync-global", action="store_true",
                        help="Also synchronize changes to ~/.gemini/config/")
    parser.add_argument("--commit-msg", help="Custom commit message for base repo")
    args = parser.parse_args()

    source_dir = Path(args.source_dir).expanduser().resolve()
    base_dir = detect_base_repository(args.base_dir)

    print(f"=== Antigravity Workflow Distillation ===")
    print(f"Source Project : {source_dir}")
    print(f"Base Workflow  : {base_dir}")
    print("")

    if source_dir == base_dir:
        print("Notice: Source project is already the base workflow repository. Inspecting internal consistency.")

    results = compare_and_distill_files(source_dir, base_dir)

    print(f"Identical files : {len(results['identical'])}")
    print(f"Modified files  : {len(results['modified'])}")
    print(f"New elements    : {len(results['new_in_project'])}")
    print("")

    if results["warnings"]:
        print("Sanitization & Security Warnings:")
        for w in results["warnings"]:
            print(f"  - [WARN] {w}")
        print("")

    if results["modified"]:
        print("Modified Elements to Distill:")
        for item in results["modified"]:
            print(f"  * {item['path']}")
            if not args.apply:
                print("    --- Diff Preview ---")
                for line in item["diff"].splitlines()[:15]:
                    print(f"    {line}")
        print("")

    if results["new_in_project"]:
        print("New Elements to Add to Core Base:")
        for item in results["new_in_project"]:
            print(f"  + {item['path']}")
        print("")

    if args.apply:
        if source_dir == base_dir and not results["new_in_project"] and not results["modified"]:
            print("No external changes to apply (already in base repo).")
        else:
            applied = apply_distillation(results, base_dir, args.commit_msg)
            print(f"Successfully distilled and updated {len(applied)} files in base workflow.")

        if args.sync_global:
            global_dir = Path(os.path.expanduser("~/.gemini/config"))
            synced = sync_to_global_config(base_dir, global_dir)
            print(f"Synchronized {len(synced)} elements to global configuration ({global_dir}).")
    else:
        print("Dry run completed. Run with --apply to synchronize and commit to base workflow.")


if __name__ == "__main__":
    main()
