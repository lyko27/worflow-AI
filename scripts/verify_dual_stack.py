#!/usr/bin/env python3
"""
verify_dual_stack.py

Automated test suite verifying the integrity of the compartmentalized architecture:
1. Antigravity (AGY) workflow in workflows/agy/
2. OpenCode documentation git submodule in docs/opencode/
3. OpenCode workflow in workflows/opencode/
4. Top-level deployment script setup.sh
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

passed_tests = 0
failed_tests = 0


def record_result(name: str, success: bool, details: str = ""):
    global passed_tests, failed_tests
    if success:
        passed_tests += 1
        print(f"  [PASS] {name}")
    else:
        failed_tests += 1
        print(f"  [FAIL] {name}")
    if details:
        print(f"         {details}")


print("==================================================================")
print(" SUITE DE VERIFICATION DES STACKS COMPARTIMENTEES (AGY & OPENCODE)")
print("==================================================================")
print(f"Racine du projet : {REPO_ROOT}\n")

# --- SECTION 1 : WORKFLOW ANTIGRAVITY (AGY) COMPARTIMENTE ---
print("[1/4] Verification du workflow Antigravity (workflows/agy/)...")
agy_dir = REPO_ROOT / "workflows" / "agy"

agy_files = [
    "AGENTS.md",
    "documentation_agy.md",
    "setup_agents.sh",
    ".agents/mcp_config.json",
    ".agents/agents/coder/agent.md",
    ".agents/agents/researcher/agent.md",
    ".agents/agents/ui-tester/agent.md",
    ".agents/agents/pedagogue/agent.md",
    ".agents/skills/learn-local/SKILL.md",
    ".agents/skills/learn-global/SKILL.md",
    ".agents/skills/learn-local/scripts/extract_conversation_insights.py",
    ".agents/skills/learn-global/scripts/distill_workflow.py",
]
missing_agy = [f for f in agy_files if not (agy_dir / f).exists()]
record_result("Fichiers fondamentaux Agy presents dans workflows/agy/", len(missing_agy) == 0, f"Manquants : {missing_agy}" if missing_agy else "")

try:
    res = subprocess.run([str(agy_dir / "setup_agents.sh"), "--help"], capture_output=True, text=True, cwd=agy_dir)
    record_result("Script workflows/agy/setup_agents.sh operationnel", res.returncode == 0)
except Exception as e:
    record_result("Script workflows/agy/setup_agents.sh operationnel", False, str(e))

try:
    res = subprocess.run(
        [sys.executable, str(agy_dir / ".agents/skills/learn-global/scripts/distill_workflow.py"), "--source-dir", str(agy_dir)],
        capture_output=True, text=True, cwd=agy_dir
    )
    record_result("Script learn-global Agy operationnel", res.returncode == 0, res.stderr.strip() if res.returncode != 0 else "")
except Exception as e:
    record_result("Script learn-global Agy operationnel", False, str(e))

# --- SECTION 2 : SOUS-MODULE DOCUMENTATION OPENCODE ---
print("\n[2/4] Verification de la documentation OpenCode (docs/opencode)...")
doc_readme = REPO_ROOT / "docs" / "opencode" / "README.md"
has_doc = doc_readme.exists() and doc_readme.stat().st_size > 1000
record_result("Documentation docs/opencode/README.md presente et lisible", has_doc, f"Taille : {doc_readme.stat().st_size if doc_readme.exists() else 0} octets")

try:
    res = subprocess.run(["git", "submodule", "status", "docs/opencode"], capture_output=True, text=True, cwd=REPO_ROOT)
    record_result("Sous-module docs/opencode enregistre dans git", res.returncode == 0 and "docs/opencode" in res.stdout)
except Exception as e:
    record_result("Sous-module docs/opencode enregistre dans git", False, str(e))

# --- SECTION 3 : WORKFLOW OPENCODE COMPARTIMENTE ---
print("\n[3/4] Verification du workflow OpenCode (workflows/opencode/)...")
oc_dir = REPO_ROOT / "workflows" / "opencode"

json_valid = True
json_errors = []
for jf in [oc_dir / ".opencode" / "opencode.json", oc_dir / "opencode.json"]:
    if not jf.exists():
        json_valid = False
        json_errors.append(f"Fichier absent: {jf.name}")
        continue
    try:
        with open(jf, "r", encoding="utf-8") as f:
            data = json.load(f)
            if "$schema" not in data or "mcp" not in data or "permission" not in data:
                json_errors.append(f"Champs requis manquants dans {jf.name}")
                json_valid = False
    except Exception as e:
        json_valid = False
        json_errors.append(f"Erreur JSON dans {jf.name}: {e}")

record_result("Validite des configurations opencode.json dans workflows/opencode/", json_valid, ", ".join(json_errors))

agents = ["coder.md", "researcher.md", "ui-tester.md", "pedagogue.md"]
agents_valid = True
agent_errs = []
for ag in agents:
    p = oc_dir / ".opencode" / "agents" / ag
    if not p.exists():
        agents_valid = False
        agent_errs.append(f"Agent manquant: {ag}")
        continue
    with open(p, "r", encoding="utf-8") as f:
        txt = f.read()
    if not txt.startswith("---") or "mode: subagent" not in txt:
        agents_valid = False
        agent_errs.append(f"Frontmatter non conforme: {ag}")

record_result("Sous-agents OpenCode presents et valides", agents_valid, ", ".join(agent_errs))

commands = ["learn-local.md", "learn-global.md"]
cmd_valid = True
cmd_errs = []
for c in commands:
    p = oc_dir / ".opencode" / "command" / c
    if not p.exists():
        cmd_valid = False
        cmd_errs.append(f"Commande manquante: {c}")
        continue
    with open(p, "r", encoding="utf-8") as f:
        txt = f.read()
    if "docs/opencode" not in txt or "git submodule" not in txt:
        cmd_valid = False
        cmd_errs.append(f"Auto-sync manquant dans {c}")

record_result("Commandes slash OpenCode avec auto-sync doc", cmd_valid, ", ".join(cmd_errs))

try:
    res_oc = subprocess.run([str(oc_dir / "setup_opencode.sh"), "--help"], capture_output=True, text=True, cwd=oc_dir)
    record_result("Script workflows/opencode/setup_opencode.sh operationnel", res_oc.returncode == 0)
except Exception as e:
    record_result("Script workflows/opencode/setup_opencode.sh operationnel", False, str(e))

try:
    res_ins = subprocess.run(
        [sys.executable, str(oc_dir / ".opencode/skills/learn-local/scripts/extract_conversation_insights.py"), "--project-dir", str(oc_dir)],
        capture_output=True, text=True, cwd=oc_dir
    )
    record_result("Script learn-local OpenCode operationnel", res_ins.returncode == 0, res_ins.stderr.strip() if res_ins.returncode != 0 else "")
except Exception as e:
    record_result("Script learn-local OpenCode operationnel", False, str(e))

try:
    res_dis = subprocess.run(
        [sys.executable, str(oc_dir / ".opencode/skills/learn-global/scripts/distill_workflow.py"), "--source-dir", str(oc_dir)],
        capture_output=True, text=True, cwd=oc_dir
    )
    record_result("Script learn-global OpenCode operationnel", res_dis.returncode == 0, res_dis.stderr.strip() if res_dis.returncode != 0 else "")
except Exception as e:
    record_result("Script learn-global OpenCode operationnel", False, str(e))

# --- SECTION 4 : SCRIPT RACINE UNIFIE (setup.sh) ---
print("\n[4/4] Verification du script d'installation racine (setup.sh)...")
try:
    res_root = subprocess.run([str(REPO_ROOT / "setup.sh"), "--help"], capture_output=True, text=True, cwd=REPO_ROOT)
    record_result("Script racine setup.sh operationnel (--help)", res_root.returncode == 0)
except Exception as e:
    record_result("Script racine setup.sh operationnel (--help)", False, str(e))

try:
    res_root_oc = subprocess.run([str(REPO_ROOT / "setup.sh"), "opencode", "--help"], capture_output=True, text=True, cwd=REPO_ROOT)
    record_result("Delegation setup.sh opencode --help", res_root_oc.returncode == 0)
except Exception as e:
    record_result("Delegation setup.sh opencode --help", False, str(e))

try:
    res_root_agy = subprocess.run([str(REPO_ROOT / "setup.sh"), "agy", "--help"], capture_output=True, text=True, cwd=REPO_ROOT)
    record_result("Delegation setup.sh agy --help", res_root_agy.returncode == 0)
except Exception as e:
    record_result("Delegation setup.sh agy --help", False, str(e))

# --- BILAN FINAL ---
print("\n==================================================================")
print(f" BILAN : {passed_tests} tests reussis, {failed_tests} echecs")
print("==================================================================")

if failed_tests > 0:
    sys.exit(1)
else:
    print("Succes : Architecture compartimentee 100% validee.")
    sys.exit(0)
