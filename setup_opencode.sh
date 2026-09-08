#!/usr/bin/env bash
# ==============================================================================
# Script d'Initialisation & Deploiement Portable de l'Architecture Multi-Agents
# OpenCode Framework
# ==============================================================================

set -euo pipefail

# Couleurs pour le terminal
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${1:-$PWD}"
INSTALL_GLOBAL=false

print_banner() {
    echo -e "${CYAN}"
    echo "  ================================================================"
    echo "   OPENCODE CLI — MULTI-AGENT ARCHITECTURE SETUP"
    echo "  ================================================================"
    echo -e "${NC}"
}

print_help() {
    echo -e "${CYAN}Usage:${NC}"
    echo "  ./setup_opencode.sh [TARGET_DIR]     Installe l'architecture OpenCode dans le dossier cible (defaut: dossier courant)"
    echo "  ./setup_opencode.sh --global         Installe les agents et la config globalement dans ~/.config/opencode/"
    echo "  ./setup_opencode.sh --help           Affiche cette aide"
    echo ""
}

# Gestion des arguments
for arg in "$@"; do
    case "$arg" in
        --help|-h)
            print_banner
            print_help
            exit 0
            ;;
        --global)
            INSTALL_GLOBAL=true
            TARGET_DIR="$HOME/.config/opencode"
            ;;
        -*)
            echo -e "${RED}Option inconnue: $arg${NC}"
            print_help
            exit 1
            ;;
        *)
            TARGET_DIR="$arg"
            ;;
    esac
done

print_banner

# 1. Verification des prerequis systeme
echo -e "${BLUE}[1/5] Verification de l'environnement & des outils QA/MCP...${NC}"

if command -v node >/dev/null 2>&1; then
    NODE_VERSION=$(node -v)
    echo -e "  ${GREEN}[OK]${NC} Node.js detecte : ${NODE_VERSION}"
else
    echo -e "  ${YELLOW}[WARN] Node.js non detecte.${NC} Necessaire pour executer Playwright MCP via npx."
fi

if command -v npx >/dev/null 2>&1; then
    echo -e "  ${GREEN}[OK]${NC} npx disponible pour @executeautomation/playwright-mcp-server"
    if command -v node >/dev/null 2>&1; then
        echo -e "  ${CYAN}[INFO]${NC} Verification / initialisation du navigateur Chromium pour Playwright..."
        npx -y playwright install chromium >/dev/null 2>&1 && \
            echo -e "  ${GREEN}[OK]${NC} Navigateur Chromium Playwright operationnel pour les captures et tests QA." || \
            echo -e "  ${YELLOW}[WARN] Echec du telechargement automatique de Chromium. Executez 'npx playwright install chromium' manuellement.${NC}"
    fi
else
    echo -e "  ${YELLOW}[WARN] npx non detecte.${NC} Installez Node.js/npm pour activer le serveur MCP."
fi

if command -v python3 >/dev/null 2>&1; then
    PY_VERSION=$(python3 --version 2>&1)
    echo -e "  ${GREEN}[OK]${NC} Python 3 detecte : ${PY_VERSION} (scripts d'introspection & distillation)"
else
    echo -e "  ${YELLOW}[WARN] Python 3 non detecte.${NC}"
fi

OPENCODE_BIN=""
if command -v opencode >/dev/null 2>&1; then
    OPENCODE_BIN="opencode"
elif [ -f "$HOME/.opencode/bin/opencode" ]; then
    OPENCODE_BIN="$HOME/.opencode/bin/opencode"
fi

if [ -n "$OPENCODE_BIN" ]; then
    OC_VER=$("$OPENCODE_BIN" --version 2>/dev/null || echo "detecte")
    echo -e "  ${GREEN}[OK]${NC} OpenCode detecte : ${OC_VER} (${OPENCODE_BIN})"
else
    echo -e "  ${YELLOW}[INFO] OpenCode non present dans le PATH.${NC} Pour l'installer : curl -fsSL https://opencode.ai/install | bash"
fi

# 2. Synchronisation du sous-module Git de documentation
echo ""
echo -e "${BLUE}[2/5] Initialisation et synchronisation de la documentation OpenCode (docs/opencode)...${NC}"
if [ -d "${SCRIPT_DIR}/.git" ] && [ -f "${SCRIPT_DIR}/.gitmodules" ]; then
    if git -C "${SCRIPT_DIR}" submodule update --init --recursive docs/opencode >/dev/null 2>&1; then
        echo -e "  ${GREEN}[OK]${NC} Sous-module docs/opencode synchronise avec succes."
    else
        echo -e "  ${YELLOW}[INFO] Note: Sous-module docs/opencode non modifie ou acces reseau differe.${NC}"
    fi
fi

# 3. Preparation du repertoire cible
echo ""
echo -e "${BLUE}[3/5] Initialisation des dossiers cibles dans : ${CYAN}${TARGET_DIR}${NC}"

if [ "$INSTALL_GLOBAL" = true ]; then
    mkdir -p "${TARGET_DIR}/agents"
    mkdir -p "${TARGET_DIR}/command"
else
    mkdir -p "${TARGET_DIR}/.opencode/agents"
    mkdir -p "${TARGET_DIR}/.opencode/command"
    mkdir -p "${TARGET_DIR}/.opencode/skills/learn-local/scripts"
    mkdir -p "${TARGET_DIR}/.opencode/skills/learn-local/references"
    mkdir -p "${TARGET_DIR}/.opencode/skills/learn-global/scripts"
    mkdir -p "${TARGET_DIR}/.opencode/skills/learn-global/references"
fi

# 4. Deploiement de la configuration, des agents et commandes
echo ""
echo -e "${BLUE}[4/5] Deploiement des definitions OpenCode...${NC}"

if [ "$INSTALL_GLOBAL" = true ]; then
    cp "${SCRIPT_DIR}/.opencode/opencode.json" "${TARGET_DIR}/opencode.json"
    cp "${SCRIPT_DIR}/.opencode/AGENTS.md" "${TARGET_DIR}/AGENTS.md"
    if [ -d "${SCRIPT_DIR}/.opencode/agents" ]; then
        cp -r "${SCRIPT_DIR}/.opencode/agents/"* "${TARGET_DIR}/agents/"
    fi
    if [ -d "${SCRIPT_DIR}/.opencode/command" ]; then
        cp -r "${SCRIPT_DIR}/.opencode/command/"* "${TARGET_DIR}/command/"
    fi
    echo -e "  ${GREEN}[OK]${NC} Configuration globale OpenCode deployee dans ${TARGET_DIR}"
else
    cp -r "${SCRIPT_DIR}/.opencode/"* "${TARGET_DIR}/.opencode/"
    if [ ! -f "${TARGET_DIR}/opencode.json" ]; then
        # Copie optionnelle du fichier racine pour compatibilite TUI directe
        cp "${SCRIPT_DIR}/.opencode/opencode.json" "${TARGET_DIR}/opencode.json"
        echo -e "  ${GREEN}[OK]${NC} Fichier miroir ${CYAN}opencode.json${NC} place a la racine."
    fi
    echo -e "  ${GREEN}[OK]${NC} Configuration OpenCode copiee dans ${CYAN}.opencode/opencode.json${NC}"
    echo -e "  ${GREEN}[OK]${NC} Protocole de gouvernance copie dans ${CYAN}.opencode/AGENTS.md${NC}"
    echo -e "  ${GREEN}[OK]${NC} Definitions des sous-agents copiees dans ${CYAN}.opencode/agents/${NC}"
    echo -e "  ${GREEN}[OK]${NC} Commandes copiees dans ${CYAN}.opencode/command/${NC}"
    echo -e "  ${GREEN}[OK]${NC} Scripts et competences copies dans ${CYAN}.opencode/skills/${NC}"
fi

# 5. Resume et validation
echo ""
echo -e "${BLUE}[5/5] Resume de l'architecture OpenCode...${NC}"
echo -e "  ${GREEN}[OK]${NC} Agent @researcher : Recherche technique, verite terrain & documentation"
echo -e "  ${GREEN}[OK]${NC} Agent @coder      : Implementation propre, typage strict, zero-hallucination"
echo -e "  ${GREEN}[OK]${NC} Agent @ui-tester  : QA, navigation Playwright MCP & captures Desktop/Mobile"
echo -e "  ${GREEN}[OK]${NC} Agent @pedagogue  : Vulgarisation formelle, formalisation mathematique & oraux"
echo -e "  ${GREEN}[OK]${NC} Commande /learn-local  : Auto-sync doc + introspection session"
echo -e "  ${GREEN}[OK]${NC} Commande /learn-global : Auto-sync doc + distillation de workflow vers depot central"
echo -e "  ${GREEN}[OK]${NC} Documentation OpenCode : Git Submodule sous docs/opencode"

echo ""
echo -e "${GREEN}================================================================${NC}"
echo -e "${GREEN}Architecture OpenCode initialisee avec succes !${NC}"
echo -e "${GREEN}================================================================${NC}"
echo ""
echo -e "Pour demarrer votre session OpenCode :"
echo -e "  ${CYAN}cd ${TARGET_DIR} && opencode${NC}"
echo ""
echo -e "Commandes utiles sous OpenCode :"
echo -e "  ${YELLOW}<Tab>${NC}                     Basculer entre Plan Mode et Build Mode"
echo -e "  ${YELLOW}/learn-local${NC}              Analyser la session et adapter les agents locaux"
echo -e "  ${YELLOW}/learn-global${NC}             Transférer les ameliorations universelles vers le depot central"
echo -e "  ${YELLOW}@coder <consigne>${NC}         Deleguer explicitement l'implementation au sous-agent Coder"
echo -e "  ${YELLOW}@researcher <recherche>${NC}  Demander une recherche documentaire en lecture seule"
echo -e "  ${YELLOW}@ui-tester <url>${NC}          Lancer les tests et captures d'ecran Playwright"
echo -e "  ${YELLOW}@pedagogue <concept>${NC}     Demander une synthese theorique ou un plan de soutenance"
echo -e "  ${YELLOW}/undo / /redo${NC}             Voyager dans le temps via l'historique Git natif"
echo ""
