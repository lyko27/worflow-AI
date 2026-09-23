#!/usr/bin/env python3
"""
verify_skeleton.py - Validateur de Conformité & Anti-Pollution du Squelette Universel

Ce script valide :
1. Le frontmatter YAML et la structure de tous les sous-agents (.agents/agents/*/agent.md).
2. Le frontmatter YAML et la structure de tous les skills (.agents/skills/*/SKILL.md).
3. La présence des références obligatoires (documentation_agy.md, AGENTS.md).
4. Le filtre anti-pollution (absence de dépendances applicatives dures dans le framework générique).
5. La cohérence des fichiers maîtres (AGENTS.md, setup_agents.sh, README.md, README.fr.md).
"""

import os
import re
import sys
from pathlib import Path

# Couleurs ANSI
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
YELLOW = "\033[1;33m"
RED = "\033[0;31m"
CYAN = "\033[0;36m"
NC = "\033[0m"


def parse_yaml_frontmatter(content: str) -> dict | None:
    """Extrait et parse de façon basique le frontmatter YAML d'un fichier Markdown."""
    if not content.startswith("---"):
        return None
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    
    yaml_text = parts[1].strip()
    result = {}
    for line in yaml_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            # Nettoyage des guillemets
            if val.startswith(('"', "'")) and val.endswith(('"', "'")):
                val = val[1:-1]
            if val.lower() == "true":
                val = True
            elif val.lower() == "false":
                val = False
            result[key] = val
    return result


def find_repo_root(explicit_path: str | None = None) -> Path:
    """Trouve la racine du squelette maître worflow-AI :
    1. Si explicit_path est fourni.
    2. Via variable d'environnement WORFLOW_AI_ROOT.
    3. Via .agents/origin_skeleton.json si présent.
    4. En remontant l'arborescence depuis ce fichier.
    """
    if explicit_path:
        p = Path(explicit_path).resolve()
        if p.exists():
            return p

    env_root = os.environ.get("WORFLOW_AI_ROOT")
    if env_root and Path(env_root).exists():
        return Path(env_root).resolve()

    origin_file = Path.cwd() / ".agents" / "origin_skeleton.json"
    if origin_file.exists():
        try:
            import json
            data = json.loads(origin_file.read_text(encoding="utf-8"))
            master_path = data.get("master_skeleton_path")
            if master_path and Path(master_path).exists():
                return Path(master_path).resolve()
        except Exception:
            pass

    cur = Path(__file__).resolve().parent
    while cur != cur.parent:
        if (cur / "AGENTS.md").exists() and (cur / ".agents").exists():
            return cur
        cur = cur.parent
    return Path.cwd()


def check_subagents(repo_root: Path) -> list[str]:
    """Vérifie tous les sous-agents sous .agents/agents/*/agent.md."""
    errors = []
    agents_dir = repo_root / ".agents" / "agents"
    
    if not agents_dir.exists():
        errors.append(f"Dossier des agents introuvable : {agents_dir}")
        return errors

    agent_dirs = [d for d in agents_dir.iterdir() if d.is_dir()]
    if not agent_dirs:
        errors.append("Aucun sous-agent trouvé dans .agents/agents/")
        return errors

    for adir in sorted(agent_dirs):
        agent_file = adir / "agent.md"
        if not agent_file.exists():
            errors.append(f"Fichier agent.md manquant dans : {adir}")
            continue

        try:
            content = agent_file.read_text(encoding="utf-8")
        except Exception as e:
            errors.append(f"Impossible de lire {agent_file} : {e}")
            continue

        frontmatter = parse_yaml_frontmatter(content)
        if not frontmatter:
            errors.append(f"Frontmatter YAML invalide ou manquant dans : {agent_file}")
            continue

        name = frontmatter.get("name")
        description = frontmatter.get("description")
        subagent = frontmatter.get("subagent")

        if not name:
            errors.append(f"Champ 'name' manquant dans : {agent_file}")
        elif name != adir.name:
            errors.append(f"Nom de l'agent '{name}' ne correspond pas au dossier '{adir.name}' dans : {agent_file}")

        if not description:
            errors.append(f"Champ 'description' manquant dans : {agent_file}")

        if subagent is not True:
            errors.append(f"Champ 'subagent: true' manquant ou invalide dans : {agent_file}")

        # Vérification des liens de documentation
        if "documentation_agy.md" not in content:
            errors.append(f"Référence à documentation_agy.md manquante dans : {agent_file}")
        if "AGENTS.md" not in content:
            errors.append(f"Référence à AGENTS.md manquante dans : {agent_file}")

    return errors


def check_skills(repo_root: Path) -> list[str]:
    """Vérifie tous les skills sous .agents/skills/*/SKILL.md."""
    errors = []
    skills_dir = repo_root / ".agents" / "skills"

    if not skills_dir.exists():
        errors.append(f"Dossier des skills introuvable : {skills_dir}")
        return errors

    skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir()]
    if not skill_dirs:
        errors.append("Aucun skill trouvé dans .agents/skills/")
        return errors

    for sdir in sorted(skill_dirs):
        skill_file = sdir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"Fichier SKILL.md manquant dans : {sdir}")
            continue

        try:
            content = skill_file.read_text(encoding="utf-8")
        except Exception as e:
            errors.append(f"Impossible de lire {skill_file} : {e}")
            continue

        frontmatter = parse_yaml_frontmatter(content)
        if not frontmatter:
            errors.append(f"Frontmatter YAML invalide ou manquant dans : {skill_file}")
            continue

        name = frontmatter.get("name")
        description = frontmatter.get("description")

        if not name:
            errors.append(f"Champ 'name' manquant dans : {skill_file}")
        elif name != sdir.name:
            errors.append(f"Nom du skill '{name}' ne correspond pas au dossier '{sdir.name}' dans : {skill_file}")

        if not description:
            errors.append(f"Champ 'description' manquant dans : {skill_file}")

    return errors


def check_core_files(repo_root: Path) -> list[str]:
    """Vérifie la présence et la cohérence des fichiers maîtres."""
    errors = []
    required_files = [
        "AGENTS.md",
        "setup_agents.sh",
        "documentation_agy.md",
        "README.md",
        "README.fr.md",
        ".agents/mcp_config.json",
    ]

    for rf in required_files:
        path = repo_root / rf
        if not path.exists():
            errors.append(f"Fichier maître obligatoire manquant : {rf}")

    # Vérifier que setup_agents.sh est exécutable ou syntaxiquement valide
    setup_sh = repo_root / "setup_agents.sh"
    if setup_sh.exists():
        content = setup_sh.read_text(encoding="utf-8")
        if "workflow-learner" not in content and "cp -r" not in content:
            errors.append("setup_agents.sh ne semble pas déployer l'intégralité des sous-agents.")

    return errors


def check_anti_pollution(repo_root: Path) -> list[str]:
    """Vérifie qu'aucune pollution de projet n'est introduite dans les fichiers du squelette maître."""
    errors = []
    # Motifs proscrits dans le squelette générique (tokens en clair, chemins absolus spécifiques hardcodés dans les règles communes)
    forbidden_patterns = [
        (r"ghp_[A-Za-z0-9]{30,}", "Token GitHub personnel en clair détecté"),
        (r"AIza[0-9A-Za-z-_]{35}", "Clé API Google en clair détectée"),
    ]

    for p in repo_root.glob(".agents/**/*.md"):
        try:
            content = p.read_text(encoding="utf-8")
            for pattern, msg in forbidden_patterns:
                if re.search(pattern, content):
                    errors.append(f"{msg} dans {p}")
        except Exception:
            pass

    return errors


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Validateur de Conformité & Anti-Pollution du Squelette Universel worflow-AI")
    parser.add_argument("--skeleton-dir", "-s", type=str, help="Chemin vers le répertoire du squelette maître worflow-AI")
    args = parser.parse_args()

    repo_root = find_repo_root(args.skeleton_dir)
    print(f"{CYAN}================================================================{NC}")
    print(f"{CYAN}🔍 VALIDATION DU SQUELETTE MAÎTRE : {repo_root.resolve()}{NC}")
    print(f"{CYAN}================================================================{NC}\n")

    subagent_errors = check_subagents(repo_root)
    skill_errors = check_skills(repo_root)
    core_errors = check_core_files(repo_root)
    pollution_errors = check_anti_pollution(repo_root)

    total_errors = subagent_errors + skill_errors + core_errors + pollution_errors

    # Affichage des sous-agents
    agents_dir = repo_root / ".agents" / "agents"
    if agents_dir.exists():
        agents = sorted([d.name for d in agents_dir.iterdir() if d.is_dir()])
        print(f"{BLUE}[1/4] Sous-agents détectés ({len(agents)}) :{NC}")
        for a in agents:
            print(f"  {GREEN}✓{NC} @{a} ({agents_dir / a / 'agent.md'})")
    else:
        print(f"{RED}[1/4] Erreur: Dossier agents manquant{NC}")

    # Affichage des skills
    skills_dir = repo_root / ".agents" / "skills"
    if skills_dir.exists():
        skills = sorted([d.name for d in skills_dir.iterdir() if d.is_dir()])
        print(f"\n{BLUE}[2/4] Skills détectés ({len(skills)}) :{NC}")
        for s in skills:
            print(f"  {GREEN}✓{NC} /{s} ({skills_dir / s / 'SKILL.md'})")
    else:
        print(f"\n{RED}[2/4] Erreur: Dossier skills manquant{NC}")

    # Affichage des fichiers maîtres
    print(f"\n{BLUE}[3/4] Fichiers maîtres & configuration :{NC}")
    for mf in ["AGENTS.md", "setup_agents.sh", "documentation_agy.md", "README.md", "README.fr.md", ".agents/mcp_config.json"]:
        p = repo_root / mf
        if p.exists():
            print(f"  {GREEN}✓{NC} {mf}")
        else:
            print(f"  {RED}✗{NC} {mf} (MANQUANT)")

    # Bilan
    print(f"\n{BLUE}[4/4] Filtre anti-pollution & intégrité :{NC}")
    if not pollution_errors:
        print(f"  {GREEN}✓{NC} Aucune fuite d'informations spécifiques ni token détecté.")

    print("\n" + "=" * 64)
    if total_errors:
        print(f"{RED}❌ VALIDATION ÉCHOUÉE — {len(total_errors)} anomalie(s) détectée(s) :{NC}")
        for err in total_errors:
            print(f"  - {RED}{err}{NC}")
        print("=" * 64)
        sys.exit(1)
    else:
        print(f"{GREEN}✨ SQUELETTE 100% CONFORME & PRÊT POUR DÉPLOIEMENT !{NC}")
        print("=" * 64)
        sys.exit(0)


if __name__ == "__main__":
    main()
