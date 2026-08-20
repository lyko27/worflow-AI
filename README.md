# Architecture Multi-Agents Antigravity (AGY) & Workflow

Workflow d'orchestration multi-agents autonome pour le développement logiciel avec **Antigravity CLI (AGY)**.

---

## 🏛️ Architecture Globale : Lead Architect + Subagents

Le système repose sur un modèle d'orchestration hiérarchique en 4 phases avec barrière séquentielle stricte :

```mermaid
flowchart TD
    Start([Requête Utilisateur / /goal]) --> Phase1[Phase 1 : Spécification & Recherche\n(Lead Architect + @researcher)]
    Phase1 -->|Barrière de Sync - Rapport Validé| Phase2[Phase 2 : Délégation Implémentation\n(@coder)]
    Phase2 --> Phase3[Phase 3 : Validation Visuelle & QA\n(@ui-tester + Screenshots Réels)]
    Phase3 --> Phase4{Phase 4 : Évaluation Visuelle &\nDécision (Brain via view_file)}
    Phase4 -- "Anomalie / Défaut Visuel\n(Max 3 itérations)" --> Phase2
    Phase4 -- "Critères & Visuels validés\n100% OK" --> Complete([Présentation Finale & Validation Utilisateur])
```

---

## 👥 Rôles & Responsabilités des Agents

| Agent | Rôle | Emplacement | Capacités Clés |
| :--- | :--- | :--- | :--- |
| **Lead Architect** *(Brain)* | Coordinateur & Décideur | Modèle Principal | Orchestration séquentielle, validation des spécifications, inspection visuelle (`view_file`), décisions finales. |
| **`@researcher`** | Recherche & Vérité Terrain | `.agents/agents/researcher/` | Exploration de documentations officielles, analyse de dépôts de code réels, règles anti-hallucination, benchmarking UX/UI. |
| **`@coder`** | Ingénieur Logiciel | `.agents/agents/coder/` | Implémentation atomique, typage strict, clean code, tests unitaires, équilibre ergonomique/UI, respect strict des specs. |
| **`@ui-tester`** | QA & Testeur Visuel *(Eyes)* | `.agents/agents/ui-tester/` | Navigation réelle Playwright MCP / Chrome Headless, captures multi-résolution obligatoires (**Desktop 1200px** & **Mobile 390px**), surveillance console/réseau. |

---

## 🔒 Principes Directeurs & Garde-Fous

1. **Barrière de Synchronisation Séquentielle** : L'implémentation (`@coder`) ne démarre **JAMAIS** avant que la phase de recherche et spécification (`@researcher`) ne soit achevée et validée.
2. **Garde-fous Anti-Hallucination** : Aucune invention de projet, d'API, de dépendance ou de composant fictif. Toutes les spécifications s'appuient sur des données vérifiées et la codebase réelle.
3. **Validation Visuelle Réelle & Multi-Écran** : Ne jamais valider sur un simple statut HTTP 200. Inspection obligatoire des captures d'écran Desktop et Mobile par le Lead Architect via `view_file`.
4. **Autonomie en Mode Manager** : Exécution fluide de bout en bout des 4 phases, avec restitution claire et visuelle pour validation utilisateur finale.

---

## 🚀 Déploiement & Initialisation

Le script `setup_agents.sh` permet d'initialiser ou de mettre à jour l'architecture dans n'importe quel projet ou globalement sur la machine :

```bash
# Déploiement dans le projet courant
./setup_agents.sh

# Déploiement dans un dossier cible spécifique
./setup_agents.sh /chemin/vers/mon-projet

# Déploiement global dans ~/.gemini/config/
./setup_agents.sh --global

# Déploiement des fichiers sans modifier ~/.gemini/antigravity-cli/settings.json
./setup_agents.sh --no-settings
```

---

## 📂 Structure des Fichiers

```
workflow/
├── .agents/
│   ├── agents/
│   │   ├── coder/
│   │   │   └── agent.md        # Définition du sous-agent Coder
│   │   ├── researcher/
│   │   │   └── agent.md        # Définition du sous-agent Researcher
│   │   └── ui-tester/
│   │       └── agent.md        # Définition du sous-agent UI-Tester
│   └── mcp_config.json         # Configuration du serveur Playwright MCP
├── AGENTS.md                   # Protocole de gouvernance et règles des 4 phases
├── documentation_agy.md        # Documentation de référence Antigravity CLI (AGY)
├── setup_agents.sh             # Script d'installation portable et automatisé
└── README.md                   # Présentation générale du workflow
```
