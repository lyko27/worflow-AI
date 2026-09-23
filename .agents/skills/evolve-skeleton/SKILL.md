---
name: evolve-skeleton
description: Procédure d'audit et d'évolution du squelette maître (worflow-AI) pour intégrer les améliorations universelles de protocole et de tooling sans pollution contextuelle de projet.
---

# Skill : Evolve Skeleton (Évolution du Framework Universel)

Ce skill formalise le processus d'abstraction pour faire évoluer le dépôt de référence `worflow-AI` à partir d'expériences de workflows personnalisés.

## Matrice de Décision & Filtre Anti-Pollution

| Type de Modification | Destination | Critère de Validation |
| :--- | :--- | :--- |
| **Spécifique au projet** (React, Prisma, Docker, conventions client) | ❌ **PROJET LOCAL ONLY** (`.agents/agents/`, `.agents/rules/`) | Rejeté du squelette |
| **Correction de faille logique** (Orchestration 4 phases, blocage) | ✅ **SQUELETTE** (`AGENTS.md`) | Universel et sans adhérence |
| **Nouvelle primitive AGY** (Hooks, MCP, options frontmatter) | ✅ **SQUELETTE & SCRIPTS** | Vérifié dans `documentation_agy.md` |
| **Amélioration du Script de Déploiement** (`setup_agents.sh`) | ✅ **SQUELETTE** | Testé local + global |

## Procédure d'Évolution
1. Exécuter le script de vérification :
   ```bash
   python3 .agents/skills/evolve-skeleton/scripts/verify_skeleton.py
   ```
2. Valider que tous les sous-agents et skills respectent le standard YAML et ont leurs liens de documentation.
3. Mettre à jour `setup_agents.sh`, `AGENTS.md`, `README.md` et `README.fr.md`.
