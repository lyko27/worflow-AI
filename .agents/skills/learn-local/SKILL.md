---
name: learn-local
description: Analyzes active conversation transcripts, user feedback, friction points, and project requirements to introspect and adapt local project subagents, prompts, and governance rules.
---

# Learn Local — Project Introspection & Local Agent Adaptation

Cette competence permet d'analyser la conversation courante, les retours explicites de l'utilisateur, les reussites et les blocages techniques, afin de faire evoluer le pool d'agents du **projet local**.

---

## Quand utiliser cette competence ?

- Apres plusieurs echanges ou a la fin d'un sprint de developpement dans le projet.
- Lorsque l'utilisateur a exprime des corrections repetees, des preferences d'architecture ou des regles metier specifiques.
- Lorsque l'agent principal constate des echecs d'outils repetes ou des manques dans les capacites des sous-agents locaux.
- Sur demande explicite : `/learn-local` (ou "analyse notre conversation et adapte nos agents").

---

## Protocole d'Execution pas a pas

### Etape 1 : Extraction des Signaux de la Conversation
1. Synchroniser la documentation de reference et executer le script d'analyse :
   ```bash
   git submodule update --init --recursive --remote docs/opencode 2>/dev/null || true
   python3 .agents/skills/learn-local/scripts/extract_conversation_insights.py
   ```
2. Analyser les points saillants :
   - Directives utilisateur prioritaires (corrections, preferences de style, conventions).
   - Echecs d'outils ou blocages de compilation/tests.
   - Roles de sous-agents ayant necessite des ajustements manuels.

### Etape 2 : Cadrage des Adaptations Locales
Evaluer les 3 leviers d'amelioration pour le projet :
- **Ajustement de Prompts** : Enrichir `.agents/agents/<name>/agent.md` avec les nouvelles contraintes detectees.
- **Creation de Nouveaux Sous-Agents** : Si une responsabilite complexe et recurrente apparait (ex: migration SQL, composant 3D, integration API specifique), creer `.agents/agents/<nouveau-role>/agent.md`.
- **Mise a Jour des Regles Locales** : Adapter [AGENTS.md](file:///home/lyko/Dossier-perso/workflow/AGENTS.md) ou `.agents/rules/` pour refleter les preferences du projet.

### Etape 3 : Application des Modifications
1. Modifier ou creer les fichiers d'agents de facon atomique.
2. S'assurer que tout nouveau sous-agent possede bien le frontmatter YAML `subagent: true`.
3. Verifier la lisibilite et la clarte des consignes.

### Etape 4 : Synthese & Restitution au Manager
Presenter a l'utilisateur :
1. Les principaux enseignements extraits de la conversation.
2. Le detail des agents modifies ou ajoutes dans `.agents/agents/`.
3. Les eventuelles recommandations pour les prochains echanges.
