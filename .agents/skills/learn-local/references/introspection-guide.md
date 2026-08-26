# Guide d'Introspection & d'Adaptation des Agents Locaux

Ce guide fournit la methodologie de reference pour analyser les conversations en cours, identifier les frictions et adapter le pool d'agents locaux au projet.

---

## 1. Types de Signaux a Detecter dans la Conversation

1. **Corrections & Directives Utilisateur** :
   - Ordres explicites de changer de methode (ex: "arrete de faire X, utilise Y", "fais des commits sans emoji").
   - Preferences d'architecture ou de style (ex: typage strict, framework specifique, convention de nommage).
   - Retours sur les livrables (ex: "le composant est trop grand", "les tests n'ont pas couvert le cas Z").

2. **Frictions Techniques & Echecs d'Outils** :
   - Commandes terminales en echec ou dependances manquantes.
   - Erreurs de compilation ou de linter repetees.
   - Echecs de tests E2E ou de navigation Playwright.

3. **Manques de Specialisation** :
   - Le sous-agent `@coder` doit gerer une technologie tres specialisee qui merite un sous-agent dedie (ex: `@db-migrator`, `@api-designer`, `@css-animator`).
   - Le sous-agent `@ui-tester` necessite des parametres de viewport ou des routes specifiques a memoriser.

---

## 2. Actions d'Adaptation Disponibles

1. **Raffinement des Sous-Agents Existants (`.agents/agents/<name>/agent.md`)** :
   - Ajouter des regles precises dans la section `## Objectifs et Responsabilites` ou `## Regles de Conduite`.
   - Inserer les contraintes de stack technique decouvertes dans le projet.

2. **Creation d'un Nouveau Sous-Agent Local (`.agents/agents/<nouveau-role>/agent.md`)** :
   - Format standardise avec frontmatter YAML :
     ```markdown
     ---
     name: nom-du-role
     description: Description courte et precise de la responsabilite.
     subagent: true
     ---

     # Titre du Role Expert

     ## Objectifs et Responsabilites
     - ...

     ## Regles de Conduite
     - ...
     ```

3. **Mise a Jour des Regles de Gouvernance (`AGENTS.md`)** :
   - Ajouter des criteres specifiques dans les 4 phases pour adapter le workflow aux exigences du projet.

---

## 3. Format de Restitution Recommande

A la fin d'une introspection, presenter :
- **Synthese des Signaux Cles** : Ce qui a fonctionne vs ce qui a genere de la friction.
- **Modifications Appliquees** : Liste des fichiers de sous-agents ou regles modifies.
- **Nouveaux Agents Crees** (si applicable) : Nom, role et modalites d'appel.
