#!/usr/bin/env bash
# ==============================================================================
# Setup Global — Deploiement des Workflows Compartimentes (OpenCode / Agy)
# ==============================================================================

set -euo pipefail

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGY_SETUP="${SCRIPT_DIR}/workflows/agy/setup_agents.sh"
OPENCODE_SETUP="${SCRIPT_DIR}/workflows/opencode/setup_opencode.sh"

print_banner() {
    echo -e "${CYAN}"
    echo "  ================================================================"
    echo "       WORKFLOW-AI — GESTIONNAIRE DE WORKFLOWS IA COMPARTIMENTES"
    echo "  ================================================================"
    echo -e "${NC}"
}

print_help() {
    print_banner
    echo -e "${CYAN}Usage direct :${NC}"
    echo "  ./setup.sh opencode [OPTIONS]   Deploie le workflow OpenCode natif"
    echo "  ./setup.sh agy [OPTIONS]        Deploie le workflow Antigravity (AGY)"
    echo "  ./setup.sh --help               Affiche cette aide"
    echo ""
    echo -e "${CYAN}Exemples :${NC}"
    echo "  ./setup.sh opencode                    Installe OpenCode dans le dossier courant"
    echo "  ./setup.sh opencode /chemin/projet     Installe OpenCode dans un projet specifique"
    echo "  ./setup.sh opencode --global           Installe OpenCode globalement (~/.config/opencode/)"
    echo "  ./setup.sh agy                         Installe AGY dans le dossier courant"
    echo "  ./setup.sh agy --global                Installe AGY globalement (~/.gemini/config/)"
    echo ""
}

# Mode ligne de commande direct
if [ $# -gt 0 ]; then
    CMD="$1"
    shift
    case "$CMD" in
        --help|-h)
            print_help
            exit 0
            ;;
        opencode)
            if [ -f "$OPENCODE_SETUP" ]; then
                bash "$OPENCODE_SETUP" "$@"
                exit 0
            else
                echo -e "${RED}Erreur: ${OPENCODE_SETUP} introuvable.${NC}"
                exit 1
            fi
            ;;
        agy)
            if [ -f "$AGY_SETUP" ]; then
                bash "$AGY_SETUP" "$@"
                exit 0
            else
                echo -e "${RED}Erreur: ${AGY_SETUP} introuvable.${NC}"
                exit 1
            fi
            ;;
        *)
            echo -e "${RED}Option inconnue: $CMD${NC}"
            print_help
            exit 1
            ;;
    esac
fi

# Mode interactif
print_banner
echo "Deux stacks bien distinctes et compartimentees sont disponibles :"
echo ""
echo "  1) OpenCode     (Dossier: workflows/opencode/ - Terminal TUI, Git undo/redo)"
echo "  2) Antigravity  (Dossier: workflows/agy/      - Orchestration native Google DeepMind)"
echo "  3) Quitter"
echo ""

read -rp "Quel workflow souhaitez-vous initialiser ? [1-3] : " CHOICE

case "$CHOICE" in
    1)
        read -rp "Dossier cible (defaut: dossier courant) : " TARGET
        TARGET="${TARGET:-$PWD}"
        bash "$OPENCODE_SETUP" "$TARGET"
        ;;
    2)
        read -rp "Dossier cible (defaut: dossier courant) : " TARGET
        TARGET="${TARGET:-$PWD}"
        bash "$AGY_SETUP" "$TARGET"
        ;;
    3)
        echo "Operation annulee."
        exit 0
        ;;
    *)
        echo -e "${RED}Choix invalide.${NC}"
        exit 1
        ;;
esac
