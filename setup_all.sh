#!/usr/bin/env bash
# ==============================================================================
# Selecteur de Workflow IA Dual-Stack : Antigravity (AGY) & OpenCode
# ==============================================================================

set -euo pipefail

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${1:-$PWD}"

echo -e "${CYAN}"
echo "  ================================================================"
echo "      DUAL-STACK AI WORKFLOW MANAGER : AGY & OPENCODE"
echo "  ================================================================"
echo -e "${NC}"
echo "Dossier cible : ${TARGET_DIR}"
echo ""
echo "Choisissez le workflow a initialiser :"
echo "  1) OpenCode uniquement (Recommande - Terminal natif & Git undo/redo)"
echo "  2) Antigravity CLI (AGY) uniquement (Workflow originel)"
echo "  3) Dual-Stack (Installer les deux workflows en parallele)"
echo "  4) Quitter"
echo ""

read -rp "Selectionnez une option [1-4] : " CHOICE

case "$CHOICE" in
    1)
        echo -e "${BLUE}Lancement de setup_opencode.sh...${NC}"
        bash "${SCRIPT_DIR}/setup_opencode.sh" "${TARGET_DIR}"
        ;;
    2)
        echo -e "${BLUE}Lancement de setup_agents.sh (AGY)...${NC}"
        bash "${SCRIPT_DIR}/setup_agents.sh" "${TARGET_DIR}"
        ;;
    3)
        echo -e "${BLUE}Installation conjointe des deux workflows...${NC}"
        bash "${SCRIPT_DIR}/setup_agents.sh" "${TARGET_DIR}"
        bash "${SCRIPT_DIR}/setup_opencode.sh" "${TARGET_DIR}"
        echo -e "${GREEN}Les deux workflows cohabitent avec succes dans le projet !${NC}"
        ;;
    4)
        echo "Operation annulee."
        exit 0
        ;;
    *)
        echo "Choix invalide."
        exit 1
        ;;
esac
