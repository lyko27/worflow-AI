---
description: Introspection de session locale et adaptation des agents OpenCode avec mise a jour de la doc
agent: build
---

### Etape 1 : Synchronisation prealable de la documentation OpenCode
!`git submodule update --init --recursive --remote docs/opencode`

### Etape 2 : Analyse des signaux de session et extraction des retours
!`python3 .opencode/skills/learn-local/scripts/extract_conversation_insights.py`

### Etape 3 : Cadrage et adaptation
A partir des signaux extraits ci-dessus et des dernieres fonctionnalites d'OpenCode documentees dans @docs/opencode/README.md :
1. Analyse les retours de l'utilisateur, les corrections de code et les erreurs d'outils rencontrees.
2. Identifie si des ajustements doivent etre apportes :
   - Dans la configuration generale : @.opencode/opencode.json
   - Dans les regles de gouvernance : @.opencode/AGENTS.md
   - Dans les invites et permissions des sous-agents : @.opencode/agents/
3. Applique de facon atomique les modifications utiles pour le projet.
4. Presente une synthese claire des enseignements et des changements effectues.
