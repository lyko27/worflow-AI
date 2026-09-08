# Guide d'Introspection & d'Adaptation des Agents Locaux (OpenCode)

Ce guide fournit la methodologie de reference pour analyser les sessions OpenCode en cours, identifier les frictions et adapter le pool d'agents locaux au projet.

---

## 1. Types de Signaux a Detecter dans la Session

1. **Corrections & Directives Utilisateur** :
   - Ordres explicites de changer de methode (ex: "arrete de faire X, utilise Y", "fais des commits sans emoji").
   - Preferences d'architecture ou de style (ex: typage strict, framework specifique, convention de nommage).
   - Retours sur les livrables (ex: "le composant est trop grand", "les tests n'ont pas couvert le cas Z").

2. **Frictions Techniques & Echecs d'Outils** :
   - Commandes terminales bash en echec ou dependances manquantes.
   - Erreurs de compilation ou de linter repetees.
   - Echecs de tests ou de validation visuelle Playwright.

3. **Besoins de Specialisation** :
   - Le sous-agent `@coder` doit gerer une technologie tres pointue meritant un sous-agent dedie (ex: `@db-migrator`, `@api-designer`).
   - Le sous-agent `@ui-tester` necessite des parametres de viewport ou des routes specifiques a memoriser.

---

## 2. Actions d'Adaptation Disponibles sous OpenCode

1. **Raffinement des Sous-Agents Existants (`.opencode/agents/<name>.md`)** :
   - Ajouter des regles precises dans la section `## Objectifs et Responsabilites` ou `## Regles de Conduite`.
   - Inserer les contraintes de stack technique decouvertes dans le projet.

2. **Creation d'un Nouveau Sous-Agent Local (`.opencode/agents/<nouveau-role>.md`)** :
   - Format standardise avec frontmatter YAML :
     ```markdown
     ---
     name: nom-du-role
     description: Description courte et precise de la responsabilite.
     mode: subagent
     model: anthropic/claude-3-7-sonnet
     permission:
       read: allow
       edit: allow
       write: allow
     ---
     ```

3. **Mise a Jour des Regles de Gouvernance (`.opencode/AGENTS.md`)** :
   - Ajouter des criteres specifiques dans les 4 phases pour adapter le workflow aux exigences du projet.

4. **Ajustement de la Configuration (`.opencode/opencode.json`)** :
   - Modifier les permissions d'outils ou ajouter des variables d'environnement.

---

## 3. Format de Restitution Recommande

A la fin d'une introspection, presenter :
- **Synthese des Signaux Cles** : Ce qui a fonctionne vs ce qui a genere de la friction.
- **Modifications Appliquees** : Liste des fichiers de sous-agents ou regles modifies dans `.opencode/`.
- **Nouveaux Agents Crees** (si applicable) : Nom, role et modalites d'appel `@nom`.
