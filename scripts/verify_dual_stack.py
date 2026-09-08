#!/usr/bin/env python3
"""
verify_dual_stack.py

Automated test suite verifying the integrity of the dual-stack architecture:
1. Antigravity (AGY) workflow integrity and non-regression
2. OpenCode documentation git submodule and learn sync
3. OpenCode stack configuration, schema, agent frontmatters and commands
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
print(" SUITE DE VERIFICATION & TESTS DE NON-REGRESSION DUAL-STACK")
print("==================================================================")
print(f"Racine du projet : {REPO_ROOT}\n")

# --- SECTION 1 : VERIFICATION AGY (NON-REGRESSION) ---
print("[1/3] Verification de l'integrite du workflow Antigravity (AGY)...")

# 1.1 Fichiers essentiels
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
missing_agy = [f for f in agy_files if not (REPO_ROOT / f).exists()]
record_result("Fichiers fondamentaux Agy presents", len(missing_agy) == 0, f"Manquants : {missing_agy}" if missing_agy else "")

# 1.2 Execution setup_agents.sh --help
try:
    res = subprocess.run([str(REPO_ROOT / "setup_agents.sh"), "--help"], capture_output=True, text=True, cwd=REPO_ROOT)
    record_result("Script setup_agents.sh executable et valide", res.returncode == 0)
except Exception as e:
    record_result("Script setup_agents.sh executable et valide", False, str(e))

# 1.3 Execution dry-run distill_workflow.py Agy
try:
    res = subprocess.run(
        [sys.executable, str(REPO_ROOT / ".agents/skills/learn-global/scripts/distill_workflow.py"), "--source-dir", str(REPO_ROOT)],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    record_result("Script learn-global Agy operationnel", res.returncode == 0, res.stderr.strip() if res.returncode != 0 else "")
except Exception as e:
    record_result("Script learn-global Agy operationnel", False, str(e))

# --- SECTION 2 : VERIFICATION SOUS-MODULE DOCUMENTATION OPENCODE ---
print("\n[2/3] Verification de la documentation OpenCode & synchronisation...")

doc_readme = REPO_ROOT / "docs" / "opencode" / "README.md"
has_doc = doc_readme.exists() and doc_readme.stat().st_size > 1000
record_result("Documentation docs/opencode/README.md presente et lisible", has_doc, f"Taille : {doc_readme.stat().st_size if doc_readme.exists() else 0} octets")

# 2.2 Test commande de mise a jour du sous-module
try:
    res = subprocess.run(["git", "submodule", "status", "docs/opencode"], capture_output=True, text=True, cwd=REPO_ROOT)
    record_result("Sous-module docs/opencode enregistre dans git", res.returncode == 0 and "docs/opencode" in res.stdout)
except Exception as e:
    record_result("Sous-module docs/opencode enregistre dans git", False, str(e))

# --- SECTION 3 : VERIFICATION STACK OPENCODE ---
print("\n[3/3] Verification de la stack native OpenCode...")

# 3.1 Validation syntaxe JSON opencode.json
json_valid = True
json_errors = []
for jf in [REPO_ROOT / ".opencode" / "opencode.json", REPO_ROOT / "opencode.json"]:
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

record_result("Syntaxe et structure des fichiers opencode.json", json_valid, ", ".join(json_errors))

# 3.2 Verification des frontmatters des agents OpenCode
agents = ["coder.md", "researcher.md", "ui-tester.md", "pedagogue.md"]
agents_valid = True
agent_errs = []
for ag in agents:
    p = REPO_ROOT / ".opencode" / "agents" / ag
    if not p.exists():
        agents_valid = False
        agent_errs.append(f"Agent manquant: {ag}")
        continue
    with open(p, "r", encoding="utf-8") as f:
        txt = f.read()
    if not txt.startswith("---"):
        agents_valid = False
        agent_errs.append(f"Frontmatter manquant: {ag}")
    if "mode: subagent" not in txt:
        agents_valid = False
        agent_errs.append(f"mode: subagent manquant: {ag}")

record_result("Frontmatters des sous-agents OpenCode conformes", agents_valid, ", ".join(agent_errs))

# 3.3 Verification des commandes slash
commands = ["learn-local.md", "learn-global.md"]
cmd_valid = True
cmd_errs = []
for c in commands:
    p = REPO_ROOT / ".opencode" / "command" / c
    if not p.exists():
        cmd_valid = False
        cmd_errs.append(f"Commande manquante: {c}")
        continue
    with open(p, "r", encoding="utf-8") as f:
        txt = f.read()
    if "docs/opencode" not in txt or "git submodule" not in txt:
        cmd_valid = False
        cmd_errs.append(f"Auto-sync manquant dans {c}")

record_result("Commandes slash OpenCode avec synchronisation submodule", cmd_valid, ", ".join(cmd_errs))

# 3.4 Verification de setup_opencode.sh et setup_all.sh
try:
    res_oc = subprocess.run([str(REPO_ROOT / "setup_opencode.sh"), "--help"], capture_output=True, text=True, cwd=REPO_ROOT)
    record_result("Script setup_opencode.sh operationnel", res_oc.returncode == 0)
except Exception as e:
    record_result("Script setup_opencode.sh operationnel", False, str(e))

# 3.5 Test dry-run des scripts learn OpenCode
try:
    res_ins = subprocess.run(
        [sys.executable, str(REPO_ROOT / ".opencode/skills/learn-local/scripts/extract_conversation_insights.py"), "--project-dir", str(REPO_ROOT)],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    record_result("Script extract_conversation_insights OpenCode operationnel", res_ins.returncode == 0, res_ins.stderr.strip() if res_ins.returncode != 0 else "")
except Exception as e:
    record_result("Script extract_conversation_insights OpenCode operationnel", False, str(e))

try:
    res_dis = subprocess.run(
        [sys.executable, str(REPO_ROOT / ".opencode/skills/learn-global/scripts/distill_workflow.py"), "--source-dir", str(REPO_ROOT)],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    record_result("Script distill_workflow OpenCode operationnel", res_dis.returncode == 0, res_dis.stderr.strip() if res_dis.returncode != 0 else "")
except Exception as e:
    record_result("Script distill_workflow OpenCode operationnel", False, str(e))

# --- BILAN FINAL ---
print("\n==================================================================")
print(f" BILAN : {passed_tests} tests reussis, {failed_tests} echecs")
print("==================================================================")

if failed_tests > 0:
    sys.exit(1)
else:
    print("Succes : Toutes les verifications de compatibilite et non-regression ont reussi.")
    sys.exit(0)
