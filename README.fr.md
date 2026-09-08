[🇬🇧 Read in English](README.md)

# Workflow Multi-Agents Dual-Stack — OpenCode & Antigravity (AGY)

Configuration, protocoles de gouvernance et scripts d'orchestration pour structurer le developpement assiste par IA avec **OpenCode** et **Antigravity CLI (AGY)**.

Le but fondamental de ce workflow est d'eviter les erreurs classiques des LLMs (hallucinations d'APIs, manque de planification, code non teste, regressions silencieuses) en appliquant un cycle d'ingenierie rigoureux en 4 etapes.

---

## 1. Comment ca marche (Cycle en 4 Phases)

Le systeme fonctionne avec un agent principal (**Lead Architect / Coordinator**) qui orchestre 4 sous-agents specialises :

```mermaid
flowchart TD
    Start([Demande / Tache]) --> P1[1. Recherche & Cadrage\n@researcher en Mode Plan]
    P1 -->|Spec Validee - Barriere Stricte| FanOut{Fan-Out Parallele}
    FanOut -->|Branche Code| P2A[2A. Implementation du Code\n@coder en Mode Build]
    FanOut -->|Branche Pedagogie| P2B[2B. Formalisation & Soutenance\n@pedagogue]
    P2A --> P3[3. Test Visuel & QA\n@ui-tester + Playwright MCP]
    P2B --> P4
    P3 --> P4{4. Validation Finale\nLead Architect}
    P4 -- Retouches si besoin --> P2A
    P4 -- Valide --> End([Termine])
```

1. **Recherche (`@researcher`)** : Verifie la documentation officielle, inspecte les fichiers existants et cadre la tache en lecture seule. Le codeur ne demarre pas tant que ce cadrage n'est pas valide (**Barriere Sequentielle**).
2. **Implementation (`@coder`)** : Ecrit le code propre, type, modulaire et sans hallucination en suivant strictement la specification de la phase 1.
3. **Formalisation & Pedagogie (`@pedagogue`)** : Vulgarise les concepts complexes, produit la modelisation mathematique/algorithmique, les schemas Mermaid et les fiches d'oral de soutenance.
4. **Tests & QA Visuel (`@ui-tester`)** : Pilote un navigateur reel via Playwright MCP, teste les parcours et prend des captures d'ecran obligatoires (**Desktop 1200px** et **Mobile 390px**).
5. **Validation (Lead)** : Verifie le diff Git et inspecte visuellement les captures d'ecran avant de cloturer la tache.

---

## 2. Coexistence Dual-Stack & Installation

Le depot est concu pour permettre une utilisation independante d'**OpenCode** ou d'**Antigravity (AGY)**, ou des deux en parallele sans aucune interférence.

### Installation Rapide avec le Selecteur Unifie :
```bash
./setup_all.sh
```

### Installation Specifique OpenCode :
```bash
# Rendre le script executable
chmod +x setup_opencode.sh

# Installer dans le dossier courant
./setup_opencode.sh

# Installer dans un autre dossier de projet
./setup_opencode.sh /chemin/vers/projet

# Installer globalement dans ~/.config/opencode/
./setup_opencode.sh --global
```

### Installation Specifique Antigravity (AGY) :
```bash
chmod +x setup_agents.sh
./setup_agents.sh
./setup_agents.sh /chemin/vers/projet
./setup_agents.sh --global
```

---

## 3. Demarrage des Sessions

- **Sous OpenCode** :
  ```bash
  opencode
  ```
  *Basculez entre le Mode Plan et le Mode Build avec `<Tab>`. Utilisez `/undo` ou `/redo` pour voyager dans le temps via les snapshots Git.*

- **Sous Antigravity (AGY)** :
  ```bash
  agy
  ```
  *Utilisez `/goal <mission>` pour lancer l'execution autonome supervisée.*

---

## 4. Competences d'Amelioration Continue (Cycle "Learn")

Les deux workflows integrent des commandes de retroaction et de distillation continue :

- **`/learn-local`** : 
  - Met a jour automatiquement le sous-module de documentation (`git submodule update --remote docs/opencode`).
  - Analyse les logs de session/conversation pour detecter les frictions et erreurs d'outils.
  - Adapte les invites des sous-agents locaux et la configuration du projet.
- **`/learn-global`** :
  - Met a jour `docs/opencode`.
  - Analyse les evolutions locales avec verification anti-fuite (suppression des secrets et chemins absolus).
  - Synchronise les ameliorations universelles vers le depot central de workflow.

---

## 5. Structure du Depot

```text
workflow/
├── .agents/                                      # Stack Antigravity CLI (AGY)
│   ├── agents/                                   # Sous-agents Agy (coder, researcher, ui-tester, pedagogue)
│   ├── skills/                                   # Skills Agy (learn-local, learn-global)
│   └── mcp_config.json                           # Configuration Playwright MCP Agy
├── .opencode/                                    # Stack OpenCode
│   ├── opencode.json                             # Configuration OpenCode (schema officiel)
│   ├── AGENTS.md                                 # Protocole de gouvernance et regles OpenCode
│   ├── agents/                                   # Sous-agents OpenCode (coder.md, researcher.md, etc.)
│   ├── command/                                  # Commandes slash OpenCode (/learn-local, /learn-global)
│   └── skills/                                   # Scripts python d'introspection et distillation
├── docs/
│   └── opencode/                                 # [Git Submodule] Documentation officielle OpenCode
├── AGENTS.md                                     # Protocole de gouvernance Agy d'origine
├── documentation_agy.md                          # Guide technique de reference Antigravity
├── documentation_opencode.md                     # Guide technique de reference OpenCode
├── opencode.json                                 # Configuration OpenCode a la racine
├── setup_agents.sh                               # Script d'installation Agy
├── setup_opencode.sh                             # Script d'installation OpenCode
├── setup_all.sh                                  # Selecteur de workflow interactif
├── .gitmodules                                   # Definition du sous-module docs/opencode
├── .gitignore
├── LICENSE
├── README.fr.md                                  # Documentation francaise
└── README.md                                     # English documentation (default)
```

---

## 6. Outils & Prerequis

- **Node.js & npx** : Fait tourner le serveur Playwright MCP (`@executeautomation/playwright-mcp-server`).
- **OpenCode** : Installe via `curl -fsSL https://opencode.ai/install | bash`.
- **Antigravity CLI (agy)** : CLI agentique Google DeepMind.
- **Python 3** : Scripts d'analyse de session et distillation.
