---
description: Distillation globale des ameliorations universelles vers le depot central de workflow
agent: build
---

### Etape 1 : Synchronisation prealable de la documentation OpenCode
!`git submodule update --init --recursive --remote docs/opencode`

### Etape 2 : Verification comparative et scan anti-fuite (Dry-Run)
!`python3 .opencode/skills/learn-global/scripts/distill_workflow.py`

### Etape 3 : Cadrage de la distillation
Consulte les differences detectees ci-dessus et verifie la conformite avec les regles d'isolation dans @.opencode/skills/learn-global/references/distillation-checklist.md :
1. Verifie qu'aucun secret, donnee sensible ou chemin absolu specifique au projet n'est exporte.
2. Identifie les ameliorations universelles dans `.opencode/` qui ont une valeur transverse pour d'autres projets.
3. Si la distillation est validee par l'utilisateur, execute la synchronisation :
   !`python3 .opencode/skills/learn-global/scripts/distill_workflow.py --apply --sync-global`
4. Restitue le rapport final de distillation.
