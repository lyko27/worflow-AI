[🇫🇷 Lire en français](README.fr.md)

# Dual-Stack Multi-Agent Workflow — OpenCode & Antigravity (AGY)

Configuration, governance protocols, and orchestration scripts for AI-assisted software engineering using **OpenCode** and **Antigravity CLI (AGY)**.

The primary mission of this workflow is to prevent standard LLM pitfalls (API hallucinations, lack of planning, untested code, silent regressions) by enforcing a strict 4-step engineering lifecycle.

---

## 1. How It Works (4-Phase Cycle)

The architecture is driven by a main agent (**Lead Architect / Coordinator**) supervising 4 specialized subagents:

```mermaid
flowchart TD
    Start([Task / Prompt]) --> P1[1. Research & Scoping\n@researcher in Plan Mode]
    P1 -->|Spec Approved - Strict Barrier| FanOut{Parallel Fan-Out}
    FanOut -->|Code Branch| P2A[2A. Code Implementation\n@coder in Build Mode]
    FanOut -->|Pedagogy Branch| P2B[2B. Modeling & Theory\n@pedagogue]
    P2A --> P3[3. Visual Testing & QA\n@ui-tester + Playwright MCP]
    P2B --> P4
    P3 --> P4{4. Final Review\nLead Architect}
    P4 -- Fixes if needed --> P2A
    P4 -- Approved --> End([Done])
```

1. **Research (`@researcher`)**: Inspects official documentation and codebase in read-only mode. Coding is forbidden until this research is approved (**Sequential Barrier**).
2. **Implementation (`@coder`)**: Writes clean, typed, modular code without hallucination, strictly adhering to the Phase 1 specification.
3. **Formalization & Pedagogy (`@pedagogue`)**: Explains complex concepts, provides formal mathematical/algorithmic models, Mermaid architecture diagrams, and oral defense presentations.
4. **Visual Testing & QA (`@ui-tester`)**: Pilots a real browser via Playwright MCP, tests interactions, and captures mandatory screenshots (**Desktop 1200px** and **Mobile 390px**).
5. **Validation (Lead)**: Reviews Git diffs and inspects screenshots before marking the task complete.

---

## 2. Dual-Stack Coexistence & Installation

This repository allows independent usage of **OpenCode**, **Antigravity (AGY)**, or both concurrently without interference.

### Fast Unified Setup:
```bash
./setup_all.sh
```

### OpenCode Setup:
```bash
chmod +x setup_opencode.sh

# Install in current project directory
./setup_opencode.sh

# Install in another project directory
./setup_opencode.sh /path/to/project

# Install globally in ~/.config/opencode/
./setup_opencode.sh --global
```

### Antigravity (AGY) Setup:
```bash
chmod +x setup_agents.sh
./setup_agents.sh
./setup_agents.sh /path/to/project
./setup_agents.sh --global
```

---

## 3. Launching Sessions

- **With OpenCode**:
  ```bash
  opencode
  ```
  *Switch between Plan Mode and Build Mode with `<Tab>`. Use `/undo` and `/redo` to time-travel through Git snapshots.*

- **With Antigravity (AGY)**:
  ```bash
  agy
  ```
  *Use `/goal <prompt>` to run long-running autonomous tasks.*

---

## 4. Continuous Learning Skills ("Learn" Cycle)

Both workflows include commands for introspection and distillation:

- **`/learn-local`**:
  - Automatically synchronizes the official OpenCode doc submodule (`git submodule update --remote docs/opencode`).
  - Analyzes session logs to detect tool failures and user corrections.
  - Adapts local subagent prompts and project configurations.
- **`/learn-global`**:
  - Automatically synchronizes `docs/opencode`.
  - Runs leak-detection scans (strips secrets, tokens, and absolute paths).
  - Distills and syncs universal improvements back to the central base workflow repository.

---

## 5. Repository Structure

```text
workflow/
├── .agents/                                      # Antigravity CLI (AGY) Stack
│   ├── agents/                                   # Agy subagents (coder, researcher, ui-tester, pedagogue)
│   ├── skills/                                   # Agy skills (learn-local, learn-global)
│   └── mcp_config.json                           # Playwright MCP configuration for Agy
├── .opencode/                                    # OpenCode Stack
│   ├── opencode.json                             # OpenCode configuration (official schema)
│   ├── AGENTS.md                                 # OpenCode governance protocol & rules
│   ├── agents/                                   # OpenCode subagents (coder.md, researcher.md, etc.)
│   ├── command/                                  # OpenCode slash commands (/learn-local, /learn-global)
│   └── skills/                                   # Python introspection & distillation scripts
├── docs/
│   └── opencode/                                 # [Git Submodule] Official OpenCode documentation
├── AGENTS.md                                     # Original Agy governance protocol
├── documentation_agy.md                          # Antigravity CLI technical guide
├── documentation_opencode.md                     # OpenCode CLI technical guide
├── opencode.json                                 # Root OpenCode configuration
├── setup_agents.sh                               # Agy setup script
├── setup_opencode.sh                             # OpenCode setup script
├── setup_all.sh                                  # Unified interactive selector
├── .gitmodules                                   # Definition of docs/opencode submodule
├── .gitignore
├── LICENSE
├── README.fr.md                                  # French documentation
└── README.md                                     # English documentation (default)
```

---

## 6. Tools & Prerequisites

- **Node.js & npx**: Runs Playwright MCP (`@executeautomation/playwright-mcp-server`).
- **OpenCode**: Installed via `curl -fsSL https://opencode.ai/install | bash`.
- **Antigravity CLI (agy)**: Google DeepMind agentic CLI.
- **Python 3**: For test servers and workflow analysis scripts.
