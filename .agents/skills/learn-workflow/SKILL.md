---
name: learn-workflow
description: Analyse l'historique de conversation (transcripts JSONL) pour adapter le workflow au projet en cours, enrichir les sous-agents existants et générer de nouveaux agents ou règles spécialisées.
---

# Skill : Learn Workflow (Adaptation Locale Continue)

Ce skill guide l'agent et l'utilisateur dans l'analyse de la session courante pour emmagasiner les retours personnels et optimiser le workflow sur mesure pour le projet.

## Déclenchement
- Automatique : Invoqué par le Brain ou le sous-agent `@workflow-learner` en fin de cycle complexe.
- Manuel : Recommandé à l'utilisateur après une session riche en ajustements via la commande `/learn-workflow` ou en demandant l'analyse de la conversation.

## Procédure Étape par Étape

### Étape 1 : Localisation et Analyse du Transcript
1. Localiser le fichier `transcript.jsonl` de la conversation sous `<appDataDir>/brain/<conversation-id>/.system_generated/logs/transcript.jsonl`.
2. Exécuter le script d'analyse embarqué :
   ```bash
   python3 .agents/skills/learn-workflow/scripts/analyze_transcript.py --transcript <chemin_du_transcript.jsonl>
   ```

### Étape 2 : Classification des Apprentissages
- **Corrections Utilisateur** : Interventions directes contredisant un choix de l'agent.
- **Règles de Style & Conventions** : Préférences de formatage, types, découpage de code.
- **Défaillances Répétées** : Erreurs d'outils ou échecs QA de la Phase 3.
- **Opportunités de Sous-Agents** : Tâches répétitives méritant un agent dédié (ex: `@db-expert`, `@api-contract`).

### Étape 3 : Application des Changements Locaux
- Mettre à jour chirurgicalement `.agents/agents/*/agent.md`.
- Créer tout nouveau sous-agent requis dans `.agents/agents/<nouveau-nom>/agent.md`.
- Ajouter des règles contextuelles dans `.agents/rules/*.md`.

## Références
- Documentation Antigravity : [`documentation_agy.md`](file:///home/local.isima.fr/nagadaix/worflow-AI/documentation_agy.md)
- Gouvernance : [`AGENTS.md`](file:///home/local.isima.fr/nagadaix/worflow-AI/AGENTS.md)
