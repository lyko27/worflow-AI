#!/usr/bin/env bash
# ==============================================================================
# Script d'Initialisation & Déploiement Portable de l'Architecture Multi-Agents
# Antigravity CLI (AGY)
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
    echo -e "${PURPLE}"
    echo "  ================================================================"
    echo "   ANTIGRAVITY CLI — MULTI-AGENT ARCHITECTURE SETUP"
    echo "  ================================================================"
    echo -e "${NC}"
}

print_help() {
    echo -e "${CYAN}Usage:${NC}"
    echo "  ./setup_agents.sh [TARGET_DIR]     Installe l'architecture dans le dossier cible (défaut: dossier courant)"
    echo "  ./setup_agents.sh --global         Installe les agents et la config MCP globalement dans ~/.gemini/config/"
    echo "  ./setup_agents.sh --no-settings    Déploie uniquement les fichiers du projet sans modifier ~/.gemini/.../settings.json"
    echo "  ./setup_agents.sh --help           Affiche cette aide"
    echo ""
}

# Gestion des arguments
CONFIGURE_SETTINGS=true

for arg in "$@"; do
    case "$arg" in
        --help|-h)
            print_banner
            print_help
            exit 0
            ;;
        --global)
            INSTALL_GLOBAL=true
            TARGET_DIR="$HOME/.gemini/config"
            ;;
        --no-settings)
            CONFIGURE_SETTINGS=false
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

# 1. Vérification des prérequis système & Installation des navigateurs
echo -e "${BLUE}[1/5] Vérification de l'environnement & des outils QA/MCP...${NC}"

if command -v node >/dev/null 2>&1; then
    NODE_VERSION=$(node -v)
    echo -e "  ${GREEN}✓${NC} Node.js détecté : ${NODE_VERSION}"
else
    echo -e "  ${YELLOW}⚠ Node.js non détecté.${NC} Nécessaire pour exécuter Playwright MCP via npx."
fi

if command -v npx >/dev/null 2>&1; then
    echo -e "  ${GREEN}✓${NC} npx disponible pour @executeautomation/playwright-mcp-server"
    
    # Vérification et installation automatique de Chromium pour Playwright
    if command -v node >/dev/null 2>&1; then
        echo -e "  ${CYAN}ℹ${NC} Vérification / initialisation du navigateur Chromium pour Playwright..."
        npx -y playwright install chromium >/dev/null 2>&1 && \
            echo -e "  ${GREEN}✓${NC} Navigateur Chromium Playwright opérationnel pour les captures et tests QA." || \
            echo -e "  ${YELLOW}⚠ Échec du téléchargement automatique de Chromium. Exécutez 'npx playwright install chromium' manuellement.${NC}"
    fi
else
    echo -e "  ${YELLOW}⚠ npx non détecté.${NC} Installez Node.js/npm pour activer le serveur MCP."
fi

if command -v python3 >/dev/null 2>&1; then
    PY_VERSION=$(python3 --version 2>&1)
    echo -e "  ${GREEN}✓${NC} Python 3 détecté : ${PY_VERSION} (serveurs locaux & scripts)"
else
    echo -e "  ${YELLOW}⚠ Python 3 non détecté.${NC}"
fi

if command -v agy >/dev/null 2>&1; then
    echo -e "  ${GREEN}✓${NC} Antigravity CLI (agy) installé et opérationnel."
else
    echo -e "  ${YELLOW}ℹ Antigravity CLI (agy) non présent dans le PATH.${NC}"
fi

if command -v eog >/dev/null 2>&1 || command -v xdg-open >/dev/null 2>&1; then
    echo -e "  ${GREEN}✓${NC} Outil d'affichage d'images système disponible pour visualiser les captures."
fi

# 2. Préparation du répertoire cible
echo ""
echo -e "${BLUE}[2/5] Initialisation des dossiers cibles dans : ${CYAN}${TARGET_DIR}${NC}"

if [ "$INSTALL_GLOBAL" = true ]; then
    mkdir -p "${TARGET_DIR}/agents/researcher"
    mkdir -p "${TARGET_DIR}/agents/coder"
    mkdir -p "${TARGET_DIR}/agents/ui-tester"
    mkdir -p "${TARGET_DIR}/skills/learn-local"
    mkdir -p "${TARGET_DIR}/skills/learn-global"
else
    mkdir -p "${TARGET_DIR}/.agents/agents/researcher"
    mkdir -p "${TARGET_DIR}/.agents/agents/coder"
    mkdir -p "${TARGET_DIR}/.agents/agents/ui-tester"
    mkdir -p "${TARGET_DIR}/.agents/skills/learn-local"
    mkdir -p "${TARGET_DIR}/.agents/skills/learn-global"
fi

# 3. Déploiement des règles et des définitions d'agents
echo ""
echo -e "${BLUE}[3/5] Déploiement des définitions d'agents, des compétences et de la configuration MCP...${NC}"

if [ "$INSTALL_GLOBAL" = true ]; then
    cp -r "${SCRIPT_DIR}/.agents/agents/"* "${TARGET_DIR}/agents/"
    if [ -d "${SCRIPT_DIR}/.agents/skills" ]; then
        cp -r "${SCRIPT_DIR}/.agents/skills/"* "${TARGET_DIR}/skills/"
    fi
    cp "${SCRIPT_DIR}/.agents/mcp_config.json" "${TARGET_DIR}/mcp_config.json"
    echo -e "  ${GREEN}✓${NC} Configuration globale déployée dans ${TARGET_DIR}"
else
    # Copie du protocole AGENTS.md
    if [ -f "${SCRIPT_DIR}/AGENTS.md" ]; then
        cp "${SCRIPT_DIR}/AGENTS.md" "${TARGET_DIR}/AGENTS.md"
        echo -e "  ${GREEN}✓${NC} Fichier de règles ${CYAN}AGENTS.md${NC} copié."
    fi

    # Copie de la hiérarchie .agents (agents + skills)
    cp -r "${SCRIPT_DIR}/.agents/"* "${TARGET_DIR}/.agents/"
    echo -e "  ${GREEN}✓${NC} Définitions des sous-agents copiées dans ${CYAN}.agents/agents/${NC}"
    echo -e "  ${GREEN}✓${NC} Compétences / Skills copiées dans ${CYAN}.agents/skills/${NC}"
    echo -e "  ${GREEN}✓${NC} Configuration MCP Playwright copiée dans ${CYAN}.agents/mcp_config.json${NC}"
fi

# 4. Configuration de l'autonomie et des permissions (Mode Manager)
if [ "${CONFIGURE_SETTINGS:-true}" = true ]; then
    echo ""
    echo -e "${BLUE}[4/5] Configuration du mode Manager autonome (~/.gemini/antigravity-cli/settings.json)...${NC}"

    if command -v python3 >/dev/null 2>&1; then
        python3 -c "
import json, os, sys

settings_path = os.path.expanduser('~/.gemini/antigravity-cli/settings.json')
try:
    os.makedirs(os.path.dirname(settings_path), exist_ok=True)
    data = {}
    if os.path.exists(settings_path):
        try:
            with open(settings_path, 'r') as f:
                data = json.load(f)
        except Exception:
            data = {}

    data['agentMode'] = 'accept-edits'
    data['toolPermission'] = 'always-proceed'
    data['artifactReviewPolicy'] = 'always-proceed'

    permissions = data.get('permissions', {})
    allow_list = permissions.get('allow', [])
    deny_list = permissions.get('deny', [])

    for rule in ['read_file(*)', 'write_file(*)', 'read_url(*)', 'execute_url(*)', 'mcp(*)', 'command(*)']:
        if rule not in allow_list:
            allow_list.append(rule)

    for rule in ['command(rm -rf)', 'command(sudo)', 'write_file(/etc)', 'write_file(/root)']:
        if rule not in deny_list:
            deny_list.append(rule)

    permissions['allow'] = allow_list
    permissions['deny'] = deny_list
    data['permissions'] = permissions

    with open(settings_path, 'w') as f:
        json.dump(data, f, indent=2)
    print('CONFIG_OK')
except Exception as e:
    print(f'CONFIG_WARN: {e}', file=sys.stderr)
" 2>&1 | grep -q "CONFIG_OK" && echo -e "  ${GREEN}✓${NC} Permissions & Mode Autonome (accept-edits, always-proceed, mcp(*), command(*)) configurés." || echo -e "  ${YELLOW}ℹ settings.json protégé ou non modifiable. Configurez ~/.gemini/antigravity-cli/settings.json ou lancez avec agy --mode=accept-edits.${NC}"
    else
        echo -e "  ${YELLOW}⚠ Python 3 non détecté.${NC} Veillez à configurer ~/.gemini/antigravity-cli/settings.json manuellement."
    fi
fi

# 5. Résumé et validation
echo ""
echo -e "${BLUE}[5/5] Validation de la structure...${NC}"
echo -e "  ${GREEN}✓${NC} Agent @researcher : Recherche web, documentation technique & inspection terrain (anti-hallucination)"
echo -e "  ${GREEN}✓${NC} Agent @coder      : Implémentation atomique, typage strict, règles anti-hallucination & équilibre visuel"
echo -e "  ${GREEN}✓${NC} Agent @ui-tester  : QA, navigation Playwright MCP & captures multi-écrans obligatoires (Desktop/Mobile)"
echo -e "  ${GREEN}✓${NC} Skill /learn-local : Analyse des conversations et adaptation des agents locaux"
echo -e "  ${GREEN}✓${NC} Skill /learn-global: Distillation des améliorations universelles vers le dépôt central"
echo -e "  ${GREEN}✓${NC} Serveur MCP       : @executeautomation/playwright-mcp-server"
echo -e "  ${GREEN}✓${NC} Mode Manager      : Autonomie complète avec barrière séquentielle stricte et inspection visuelle réelle"

echo ""
echo -e "${GREEN}================================================================${NC}"
echo -e "${GREEN}Architecture multi-agents initialisee avec succes !${NC}"
echo -e "${GREEN}================================================================${NC}"
echo ""
echo -e "Pour démarrer votre session de travail assistée par IA :"
echo -e "  ${CYAN}cd ${TARGET_DIR} && agy${NC}"
echo ""
echo -e "Utilisation recommandée en tant que Manager :"
echo -e "  ${YELLOW}/goal <votre ordre>${NC}         Lance la mission complète en autonomie (Phases 1 à 4)"
echo -e "  ${YELLOW}/learn-local${NC}               Analyser la conversation et adapter les agents locaux"
echo -e "  ${YELLOW}/learn-global${NC}              Transférer les améliorations universelles vers le workflow de base"
echo -e "  ${YELLOW}/agents${NC}                    Ouvrir le panneau interactif de gestion des agents"
echo -e "  ${YELLOW}/tasks${NC}                     Suivre les commandes et serveurs en arrière-plan"
echo -e "  ${YELLOW}/diff${NC}                      Visualiser les modifications avant commit"
echo ""
