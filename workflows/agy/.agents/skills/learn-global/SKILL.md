---
name: learn-global
description: Analyzes local conversation history and agent adaptations at project end, filters out all project-specific logic, and synchronizes generalized workflow improvements to the central workflow repository.
---

# Learn Global — Workflow Distillation & Core Base Synchronization

Cette competence permet, a la fin d'un projet ou a la suite d'un jalon majeur, d'analyser les adaptations et enseignements locaux, d'en extraire les ameliorations **universelles** (prompts, garde-fous, protocoles QA, gouvernance), et de les synchroniser proprement vers le **depot central du workflow**.

---

## Principe Fondamental : Zero Pollution du Workflow Global

> [!IMPORTANT]
> **Isolation Stricte** : Aucune logique metier, aucun secret/cle API, aucun chemin local absolu et aucune donnee specifique au projet en cours ne doit penetrer le depot de base du workflow.

---

## Quand utiliser cette competence ?

- A la livraison finale d'un projet de developpement.
- Apres avoir resolu des problemes complexes dont la solution a une valeur universelle pour tous les futurs projets.
- Pour mettre a jour la base de reference (`/home/lyko/Dossier-perso/workflow` ou chemin configure) et la configuration globale (`~/.gemini/config/`).
- Sur commande explicite : `/learn-global`.

---

## Protocole d'Execution pas a pas

### Etape 1 : Localisation du Depot Central
Le script detecte le depot central via la variable d'environnement `WORKFLOW_BASE_DIR` ou le chemin par defaut :
```bash
python3 .agents/skills/learn-global/scripts/distill_workflow.py --help
```

### Etape 2 : Analyse Comparative & Scan Anti-Fuite (Dry-Run)
Synchroniser la documentation de reference et executer la comparaison entre le projet local et la base centrale :
```bash
git submodule update --init --recursive --remote docs/opencode 2>/dev/null || true
python3 .agents/skills/learn-global/scripts/distill_workflow.py
```
- Verifier les avertissements de securite et de chemins absolus.
- Inspecter les differences sur `.agents/agents/`, `AGENTS.md` et les scripts.

### Etape 3 : Delegation au Sous-Agent d'Analyse (Brain / Researcher)
Invoquer `@researcher` via `invoke_subagent` pour evaluer si les modifications locales meritent une generalisation :
1. Les ameliorations de prompts rendent-elles les agents plus robustes sur d'autres stacks ?
2. Les nouvelles regles de gouvernance renforcent-elles la stabilite globale ?
3. Les eventuels nouveaux sous-agents ont-ils une utilite transverse ou seulement locale ?

### Etape 4 : Application & Synchronisation vers la Base
Appliquer les modifications validees et creer le commit dans le depot central :
```bash
python3 .agents/skills/learn-global/scripts/distill_workflow.py --apply --sync-global
```

### Etape 5 : Rapport Final de Distillation
Fournir au manager un bilan exhaustif :
- Elements generalises et transferes vers la base du workflow.
- Elements volontairement conserves comme specifiques au projet local.
- Statut du commit Git dans le depot central.
