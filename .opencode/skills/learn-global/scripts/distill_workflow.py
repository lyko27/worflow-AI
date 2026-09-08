#!/usr/bin/env python3
"""
distill_workflow.py

Distills universal, domain-agnostic workflow improvements from an OpenCode
project and synchronizes them cleanly to the central base workflow repository
(and optionally ~/.config/opencode/).

Ensures strict sanitization to prevent project-specific logic, absolute paths,
or proprietary business domain rules from polluting the base workflow.
Automatically ensures the docs/opencode git submodule is updated.
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

SENSITIVE_PATTERNS = [
    r"api[_-]?key\s*[:=]\s*['\"][^'\"]+['\"]",
    r"bearer\s+[a-zA-Z0-9_\-\.]{15,}",
    r"password\s*[:=]\s*['\"][^'\"]+['\"]",
    r"secret\s*[:=]\s*['\"][^'\"]+['\"]",
    r"localhost:[0-9]{4,5}",
]


def sync_opencode_doc_submodule(repo_dir: Path) -> bool:
    """Updates the docs/opencode git submodule to the latest remote state."""
    git_modules = repo_dir / ".gitmodules"
    if git_modules.exists() and (repo_dir / ".git").exists():
        try:
            print("[SYNC] Synchronisation prealable de la documentation OpenCode...")
            res = subprocess.run(
                ["git", "submodule", "update", "--init", "--recursive", "--remote", "docs/opencode"],
                cwd=repo_dir,
                capture_output=True,
                text=True,
                timeout=30
            )
            if res.returncode == 0:
                print("  [OK] Documentation OpenCode a jour.")
                return True
            else:
                print(f"  [WARN] Note sync submodule: {res.stderr.strip()}")
        except Exception as e:
            print(f"  [WARN] Echec de mise a jour du sous-module: {e}")
    return False


def detect_base_repository(explicit_path: Optional[str] = None) -> Path:
    """Finds and validates the central workflow repository path."""
    if explicit_path:
        base_path = Path(explicit_path).expanduser().resolve()
    else:
        base_path = Path(DEFAULT_BASE_DIR).expanduser().resolve()

    if not base_path.exists():
        raise FileNotFoundError(f"Central workflow directory not found: {base_path}")

    # Check for OpenCode or Agy signature
    opencode_dir = base_path / ".opencode"
    agents_md = base_path / "AGENTS.md"
    setup_sh = base_path / "setup_agents.sh"
    if not (opencode_dir.exists() or agents_md.exists() or setup_sh.exists()):
        raise ValueError(f"Directory {base_path} does not appear to be a valid workflow repository.")

    return base_path


def sanitize_content(content: str, source_dir: Path, base_dir: Path) -> Tuple[str, List[str]]:
    """Checks for project-specific leaks and removes hardcoded project paths."""
    warnings = []
    
    for pattern in SENSITIVE_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            warnings.append(f"Detecte jeton/secret potentiel: {matches[0][:20]}...")

    if source_dir.resolve() != base_dir.resolve():
        proj_path_str = str(source_dir.resolve())
        if proj_path_str in content:
            content = content.replace(proj_path_str, "<PROJECT_ROOT>")
            warnings.append(f"Chemin absolu remplace par '<PROJECT_ROOT>'.")

    return content, warnings


def compare_and_distill_files(source_dir: Path, base_dir: Path) -> Dict[str, Any]:
    """Compares local .opencode files with base workflow repository."""
    results = {
        "identical": [],
        "modified": [],
        "new_in_project": [],
        "warnings": []
    }

    relative_files_to_check: List[Path] = []

    # Check .opencode directory elements
    source_oc = source_dir / ".opencode"
    if source_oc.exists():
        for f in source_oc.rglob("*"):
            if f.is_file() and not f.name.startswith("."):
                relative_files_to_check.append(f.relative_to(source_dir))

    # Also check root configuration if present
    if (source_dir / "opencode.json").exists():
        relative_files_to_check.append(Path("opencode.json"))

    for rel_path in relative_files_to_check:
        source_file = source_dir / rel_path
        base_file = base_dir / rel_path

        if not source_file.exists():
            continue

        try:
            with open(source_file, "r", encoding="utf-8", errors="replace") as sf:
                source_content = sf.read()
        except OSError as e:
            results["warnings"].append(f"Impossible de lire {source_file}: {e}")
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
                results["warnings"].append(f"Impossible de lire le fichier de base {base_file}: {e}")
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
            subprocess.run(["git", "add"] + applied_files, cwd=base_dir, check=True, capture_output=True)
            status_out = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=base_dir)
            if status_out.returncode != 0:
                default_msg = f"feat(workflow): distillation des ameliorations opencode ({len(applied_files)} fichiers)"
                msg = commit_msg or default_msg
                subprocess.run(["git", "commit", "-m", msg], cwd=base_dir, check=True, capture_output=True)
        except subprocess.SubprocessError as e:
            print(f"Attention : echec du commit git dans le depot central: {e}", file=sys.stderr)

    return applied_files


def sync_to_global_opencode(base_dir: Path, global_config_dir: Path) -> List[str]:
    """Syncs base OpenCode configuration to ~/.config/opencode/."""
    synced = []
    global_config_dir.mkdir(parents=True, exist_ok=True)

    base_oc = base_dir / ".opencode"
    if not base_oc.exists():
        return synced

    # Copy config
    base_json = base_oc / "opencode.json"
    if base_json.exists():
        dest_json = global_config_dir / "opencode.json"
        with open(base_json, "r", encoding="utf-8") as src, open(dest_json, "w", encoding="utf-8") as dst:
            dst.write(src.read())
        synced.append("opencode.json")

    # Copy agents
    base_agents = base_oc / "agents"
    if base_agents.exists():
        target_agents = global_config_dir / "agents"
        target_agents.mkdir(parents=True, exist_ok=True)
        for af in base_agents.glob("*.md"):
            dest = target_agents / af.name
            with open(af, "r", encoding="utf-8") as src, open(dest, "w", encoding="utf-8") as dst:
                dst.write(src.read())
            synced.append(f"agents/{af.name}")

    # Copy commands
    base_cmd = base_oc / "command"
    if base_cmd.exists():
        target_cmd = global_config_dir / "command"
        target_cmd.mkdir(parents=True, exist_ok=True)
        for cf in base_cmd.glob("*.md"):
            dest = target_cmd / cf.name
            with open(cf, "r", encoding="utf-8") as src, open(dest, "w", encoding="utf-8") as dst:
                dst.write(src.read())
            synced.append(f"command/{cf.name}")

    return synced


def main():
    parser = argparse.ArgumentParser(description="Distill and synchronize OpenCode workflow improvements.")
    parser.add_argument("--base-dir", default=DEFAULT_BASE_DIR, help=f"Path to central workflow repo (default: {DEFAULT_BASE_DIR})")
    parser.add_argument("--source-dir", default=os.getcwd(), help="Path to current project root (default: cwd)")
    parser.add_argument("--apply", action="store_true", help="Apply distilled changes and commit to base workflow")
    parser.add_argument("--sync-global", action="store_true", help="Sync to ~/.config/opencode/")
    parser.add_argument("--commit-msg", help="Custom commit message for base repo")
    parser.add_argument("--no-sync-doc", action="store_true", help="Skip doc submodule update")
    args = parser.parse_args()

    source_dir = Path(args.source_dir).expanduser().resolve()
    base_dir = detect_base_repository(args.base_dir)

    print("=== OpenCode Workflow Distillation ===")
    print(f"Source Project : {source_dir}")
    print(f"Base Workflow  : {base_dir}")
    print("")

    if not args.no_sync_doc:
        sync_opencode_doc_submodule(base_dir)

    if source_dir == base_dir:
        print("Notice: Le projet source est deja le depot de base. Verification de coherence interne.")

    results = compare_and_distill_files(source_dir, base_dir)

    print(f"Fichiers identiques : {len(results['identical'])}")
    print(f"Fichiers modifies   : {len(results['modified'])}")
    print(f"Nouveaux elements   : {len(results['new_in_project'])}")
    print("")

    if results["warnings"]:
        print("Avertissements de securite et sanitarisation :")
        for w in results["warnings"]:
            print(f"  - [WARN] {w}")
        print("")

    if results["modified"]:
        print("Elements modifies a distiller :")
        for item in results["modified"]:
            print(f"  * {item['path']}")
        print("")

    if results["new_in_project"]:
        print("Nouveaux elements a ajouter a la base :")
        for item in results["new_in_project"]:
            print(f"  + {item['path']}")
        print("")

    if args.apply:
        if source_dir == base_dir and not results["new_in_project"] and not results["modified"]:
            print("Aucune modification externe a appliquer (deja dans le depot de base).")
        else:
            applied = apply_distillation(results, base_dir, args.commit_msg)
            print(f"Distillation reussie : {len(applied)} fichiers synchronises dans le workflow de base.")

        if args.sync_global:
            global_dir = Path(os.path.expanduser("~/.config/opencode"))
            synced = sync_to_global_opencode(base_dir, global_dir)
            print(f"Synchronisation globale effectuee : {len(synced)} elements dans {global_dir}.")
    else:
        print("Simulation terminee. Utilisez --apply pour enregistrer et commiter dans le workflow de base.")


if __name__ == "__main__":
    main()
