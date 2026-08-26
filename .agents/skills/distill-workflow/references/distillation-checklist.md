# Checklist de Distillation & Non-Pollution du Workflow

Ce document definit les regles strictes d'isolation appliquees lors de l'exportation des ameliorations d'un projet local vers le depot central de workflow.

---

## 1. Regles d'Isolation & Anti-Pollution

| Element | Statut pour le Workflow Global | Exemple d'Action / Sanitarisation |
| :--- | :--- | :--- |
| **Logique Metier Specifique** | **INTERDIT** | Remplacer par des modeles ou abstractions generiques. |
| **Chemins Absolus Locaux** | **INTERDIT** | Remplacer `/home/.../mon-projet` par `<PROJECT_ROOT>` ou des chemins relatifs. |
| **Secrets, Tokens & Cles API** | **INTERDIT** | Supprimer toute donnee sensible ou identifiant local. |
| **Noms de Produits / Clients** | **INTERDIT** | Anonymiser ou generaliser les intitulés. |
| **Ameliorations de Prompts Generales** | **AUTORISE** | Generaliser les consignes d'architecture, de typage, de modularite. |
| **Garde-fous QA & Protocoles Playwright** | **AUTORISE** | Enregistrer les bonnes pratiques de tests multi-viewport. |
| **Regles de Gouvernance (AGENTS.md)** | **AUTORISE** | Affiner les barrieres de synchronisation et les boucles itératives. |
| **Scripts Utilitaires & Skills Reutilisables** | **AUTORISE** | Intégrer les scripts d'automatisation portables. |

---

## 2. Processus de Validation Avant Synchronisation

1. **Scan Automatique** : Executer `python3 .agents/skills/distill-workflow/scripts/distill_workflow.py` en mode simulation (`dry-run`).
2. **Revue du Diff** : Verifier chaque ligne modifiee avec `git diff`.
3. **Verification de Generalisation** : Confirmer que la regle ou l'instruction amelioree s'applique a 100% des futurs projets et non a un seul cas particulier.
4. **Commit Propre** : Enregistrer le commit dans le depot central avec une description technique explicite sans emoji.
