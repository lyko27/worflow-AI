#!/usr/bin/env python3
"""
analyze_transcript.py - Analyseur de transcript Antigravity CLI pour méta-apprentissage

Parse les fichiers transcript.jsonl / transcript_full.jsonl d'une session Antigravity,
extrait les corrections utilisateur, les erreurs d'outils, les échecs QA et propose
des recommandations d'optimisation concrètes pour les agents et règles du projet.
"""

import argparse
import glob
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


def find_latest_transcript() -> str | None:
    """Recherche automatiquement le fichier transcript.jsonl le plus récent."""
    patterns = [
        os.path.expanduser("~/.gemini/antigravity-cli/brain/*/.system_generated/logs/transcript*.jsonl"),
        os.path.expanduser("~/.gemini/antigravity/brain/*/.system_generated/logs/transcript*.jsonl"),
        os.path.expanduser("~/.gemini/brain/*/.system_generated/logs/transcript*.jsonl"),
    ]
    files = []
    for pattern in patterns:
        files.extend(glob.glob(pattern))
    
    if not files:
        return None
    
    # Trier par date de dernière modification décroissante
    files.sort(key=os.path.getmtime, reverse=True)
    return files[0]


CORRECTION_PATTERNS = [
    r"\b(non\b|au lieu de|plut[oô]t|pr[eé]f[eè]re|corrige|rectifie|attention|ne fais pas|arr[eê]te|mauvais|erreur|ne pas|jamais|invalide)\b",
    r"\b(utilise|immerge|ajoute|change|remplace|modifie|supprime)\b.*(strictement|exclusivement|toujours|obligatoire)",
    r"\b(typage strict|interface|eslint|prettier|lint|convention|architecture|clean code)\b",
    r"\b(fix|bug|broken|wrong|invalid|fail|failed|reject|refused)\b",
]

DOMAIN_KEYWORDS = {
    "db-expert": [
        "sql", "postgres", "mysql", "sqlite", "prisma", "typeorm", "migration",
        "schema.prisma", "alembic", "database", "bdd", "table", "query", "orm"
    ],
    "api-contract": [
        "openapi", "swagger", "graphql", "grpc", "endpoint", "rest api", "dto",
        "payload", "schema validation", "zod", "pydantic", "fastapi", "route"
    ],
    "devops-engineer": [
        "docker", "dockerfile", "docker-compose", "k8s", "kubernetes", "ci/cd",
        "github actions", "deploy", "nginx", "helm", "pipeline"
    ],
    "security-auditor": [
        "cve", "auth", "jwt", "oauth", "cors", "xss", "csrf", "sqli",
        "vulnerability", "sanitize", "permission", "rbac"
    ],
}


def parse_transcript(transcript_path: str) -> dict:
    """Parse un fichier JSONL et en extrait les métadonnées et événements pertinents."""
    if not os.path.exists(transcript_path):
        raise FileNotFoundError(f"Fichier transcript introuvable : {transcript_path}")

    records = []
    with open(transcript_path, "r", encoding="utf-8", errors="replace") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                records.append(data)
            except json.JSONDecodeError:
                continue

    user_messages = []
    tool_calls = []
    tool_errors = []
    qa_failures = []
    domain_hits = Counter()
    conversation_id = None
    workspace_paths = []

    for record in records:
        event = record.get("event")
        step_update = record.get("step_update", {})
        
        # Récupération de l'ID de conversation
        if not conversation_id:
            conversation_id = (
                step_update.get("conversation_id")
                or record.get("conversation_id")
                or record.get("init", {}).get("conversation_id")
            )

        step_type = step_update.get("step_type") or record.get("type") or event
        
        # Analyse des messages utilisateurs
        if step_type == "user_input" or record.get("role") == "user":
            content = (
                step_update.get("text_delta")
                or step_update.get("content")
                or record.get("content")
                or record.get("text")
                or ""
            )
            if isinstance(content, dict):
                content = content.get("text", "")
            elif isinstance(content, list):
                content = " ".join([str(c.get("text", c)) if isinstance(c, dict) else str(c) for c in content])
            
            if content and content.strip():
                content_str = str(content).strip()
                # Détection de corrections
                is_correction = any(re.search(p, content_str, re.IGNORECASE) for p in CORRECTION_PATTERNS)
                user_messages.append({
                    "text": content_str,
                    "is_correction": is_correction,
                    "step_index": step_update.get("step_index"),
                })
                
                # Détection de domaines
                lower_content = content_str.lower()
                for domain, kws in DOMAIN_KEYWORDS.items():
                    for kw in kws:
                        if kw in lower_content:
                            domain_hits[domain] += 1

        # Analyse des appels d'outils et erreurs
        if step_type == "tool" or "tool_info" in step_update or "tool_name" in step_update:
            tool_info = step_update.get("tool_info", {})
            tool_name = step_update.get("tool_name") or tool_info.get("name", "unknown_tool")
            output = tool_info.get("output", "")
            error = tool_info.get("error")
            params = tool_info.get("parameters", {})

            tool_calls.append({
                "tool": tool_name,
                "step_index": step_update.get("step_index"),
            })

            # Erreurs d'outils explicites
            if error or (isinstance(output, str) and ("error" in output.lower() or "exception" in output.lower() or "traceback" in output.lower())):
                tool_errors.append({
                    "tool": tool_name,
                    "error": error or str(output)[:300],
                    "params": params,
                    "step_index": step_update.get("step_index"),
                })

            # Échecs QA UI / Tests
            if isinstance(output, str) and ("[FAIL]" in output or "FAIL" in output or "AssertionError" in output):
                qa_failures.append({
                    "tool": tool_name,
                    "output_snippet": output[:400],
                    "step_index": step_update.get("step_index"),
                })

    return {
        "transcript_path": transcript_path,
        "conversation_id": conversation_id or "unknown",
        "total_records": len(records),
        "user_messages": user_messages,
        "tool_calls_count": len(tool_calls),
        "tool_calls": tool_calls,
        "tool_errors": tool_errors,
        "qa_failures": qa_failures,
        "domain_hits": domain_hits,
    }


def generate_learning_report(data: dict) -> str:
    """Génère un rapport Markdown détaillé d'analyse et recommandations."""
    lines = []
    lines.append("# 📊 Rapport d'Analyse de Session & Méta-Apprentissage")
    lines.append("")
    lines.append(f"- **Fichier Transcript** : `{data['transcript_path']}`")
    lines.append(f"- **Conversation ID** : `{data['conversation_id']}`")
    lines.append(f"- **Date d'Analyse** : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"- **Total Événements** : {data['total_records']}")
    lines.append(f"- **Appels d'Outils** : {data['tool_calls_count']}")
    lines.append(f"- **Erreurs d'Outils Détectées** : {len(data['tool_errors'])}")
    lines.append(f"- **Échecs QA / Tests Détectés** : {len(data['qa_failures'])}")
    lines.append("")

    # Corrections Utilisateur
    corrections = [m for m in data["user_messages"] if m["is_correction"]]
    lines.append("## 1. 🎯 Retours & Corrections Utilisateur Détectés")
    if corrections:
        for idx, corr in enumerate(corrections, 1):
            step_info = f" (Étape {corr['step_index']})" if corr.get('step_index') is not None else ""
            lines.append(f"### Correction #{idx}{step_info}")
            lines.append(f"> \"{corr['text'][:400]}\"")
            lines.append("")
    else:
        lines.append("*(Aucune intervention corrective explicite détectée dans cette session)*")
        lines.append("")

    # Erreurs d'outils et échecs QA
    lines.append("## 2. ⚠️ Défaillances d'Outils & Rejets QA")
    if data["qa_failures"]:
        lines.append("### 🔍 Échecs QA (Phase 3)")
        for idx, fail in enumerate(data["qa_failures"], 1):
            lines.append(f"- **Échec #{idx}** (`{fail['tool']}`) :")
            lines.append(f"  ```text\n  {fail['output_snippet'].strip()}\n  ```")
        lines.append("")

    if data["tool_errors"]:
        lines.append("### 🛠️ Erreurs d'Exécution d'Outils")
        for idx, err in enumerate(data["tool_errors"][:5], 1):
            lines.append(f"- **Erreur #{idx}** (`{err['tool']}`) : {str(err['error'])[:200]}")
        if len(data["tool_errors"]) > 5:
            lines.append(f"- *(et {len(data['tool_errors']) - 5} autres erreurs similaires...)*")
        lines.append("")
    
    if not data["qa_failures"] and not data["tool_errors"]:
        lines.append("*(Aucune défaillance bloquante constatée)*")
        lines.append("")

    # Recommandations d'adaptation des agents
    lines.append("## 3. 💡 Recommandations d'Optimisation du Workflow")
    
    # Suggestions pour @coder
    lines.append("### A. Recommandations pour `@coder` (`.agents/agents/coder/agent.md`)")
    if corrections:
        lines.append("- Intégrer les contraintes de style et de typage formulées par l'utilisateur.")
    if data["qa_failures"]:
        lines.append("- Renforcer la validation locale des composants UI et des scénarios de test avant passage en Phase 3.")
    lines.append("- Conserver la politique de modifications atomiques et typage strict.")
    lines.append("")

    # Suggestions pour @researcher
    lines.append("### B. Recommandations pour `@researcher` (`.agents/agents/researcher/agent.md`)")
    lines.append("- Vérifier systématiquement les documentations officielles des dépendances manipulées.")
    lines.append("")

    # Suggestions pour @ui-tester
    lines.append("### C. Recommandations pour `@ui-tester` (`.agents/agents/ui-tester/agent.md`)")
    if data["qa_failures"]:
        lines.append("- Systématiser la capture d'écran multi-viewports (1200px / 390px) et la vérification des statuts réseau.")
    lines.append("- Confirmer que chaque point d'entrée testé génère un fichier image inspectable par le Lead Architect.")
    lines.append("")

    # Suggestions de nouveaux sous-agents
    lines.append("### D. Opportunités de Nouveaux Sous-Agents Détectées")
    dominant_domains = [dom for dom, count in data["domain_hits"].most_common(2) if count >= 2]
    if dominant_domains:
        for dom in dominant_domains:
            count = data["domain_hits"][dom]
            lines.append(f"- **`@{dom}`** (mentionné {count} fois) :")
            lines.append(f"  - Recommandation : Créer le fichier `.agents/agents/{dom}/agent.md` pour isoler cette expertise technique.")
    else:
        lines.append("*(Aucune spécialisation récurrente isolée ne nécessite un nouveau sous-agent pour l'instant)*")
    lines.append("")

    lines.append("---")
    lines.append("*(Généré automatiquement par `analyze_transcript.py` — Skill: `learn-workflow`)*")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Analyseur de transcript Antigravity CLI pour méta-apprentissage.")
    parser.add_argument("--transcript", "-t", type=str, help="Chemin vers le fichier transcript.jsonl")
    parser.add_argument("--auto", "-a", action="store_true", help="Trouve automatiquement le transcript le plus récent")
    parser.add_argument("--output", "-o", type=str, help="Chemin du fichier Markdown pour enregistrer le rapport")
    parser.add_argument("--json", "-j", action="store_true", help="Affiche le résultat au format JSON")

    args = parser.parse_args()

    transcript_path = args.transcript
    if not transcript_path or args.auto:
        auto_path = find_latest_transcript()
        if auto_path:
            transcript_path = auto_path
            print(f"[INFO] Transcript détecté automatiquement : {transcript_path}", file=sys.stderr)
        elif not transcript_path:
            print("[ERREUR] Aucun transcript spécifié et aucun transcript trouvé automatiquement.", file=sys.stderr)
            print("Utilisez --transcript <chemin_du_fichier.jsonl>", file=sys.stderr)
            sys.exit(1)

    try:
        data = parse_transcript(transcript_path)
    except Exception as e:
        print(f"[ERREUR] Échec de l'analyse du transcript : {e}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        # Nettoyage pour JSON sérialisable
        data["domain_hits"] = dict(data["domain_hits"])
        output_str = json.dumps(data, indent=2, ensure_ascii=False)
    else:
        output_str = generate_learning_report(data)

    if args.output:
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_str)
        print(f"[SUCCÈS] Rapport généré dans : {args.output}")
    else:
        print(output_str)


if __name__ == "__main__":
    main()
