#!/usr/bin/env zsh
# ==============================================================================
# macOS LaTeX & AI Starter Kit for Educators
# Automated Installer & Environment Bootstrap
# Target OS: macOS (Apple Silicon & Intel)
# ==============================================================================

set -e

# Visual Formatting Constants
BOLD="\033[1m"
GREEN="\033[1;32m"
BLUE="\033[1;34m"
YELLOW="\033[1;33m"
CYAN="\033[1;36m"
RED="\033[1;31m"
RESET="\033[0m"

REPO_SLUG="${GITHUB_REPO:-chrismitsacopoulos/LaTeX-For-Education}"
TARGET_DIR="${HOME}/Documents/Teaching-LaTeX"
TEX_PATH="/Library/TeX/texbin"

print_banner() {
    clear 2>/dev/null || true
    echo "${CYAN}${BOLD}"
    echo "=================================================================="
    echo "       macOS LaTeX & AI Starter Kit for Educators"
    echo "       Automated Environment & Template Installation"
    echo "=================================================================="
    echo "${RESET}"
    echo "This installation utility configures a native LaTeX typesetting"
    echo "environment pre-loaded with educational templates and system prompts"
    echo "for artificial intelligence coding assistants."
    echo ""
}

print_sudo_notice() {
    echo "${YELLOW}${BOLD}[NOTICE] Administrator Privileges Required${RESET}"
    echo "Installing the BasicTeX typesetting framework into system directories"
    echo "requires administrative authorization via sudo."
    echo ""
    echo "${BOLD}Security Note:${RESET} Keystrokes entered for password prompts in macOS"
    echo "Terminal are masked and will not display visual characters or bullets."
    echo "Type your account password and press Enter to continue."
    echo ""
    
    # Authenticate sudo upfront and maintain session keepalive in background
    sudo -v
    while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &
    SUDO_PID=$!
    trap 'kill $SUDO_PID 2>/dev/null || true' EXIT
}

setup_workspace() {
    echo "\n${BLUE}${BOLD}[1/4] Initializing Workspace Directory...${RESET}"
    echo "Target directory path: ${TARGET_DIR}"
    mkdir -p "${TARGET_DIR}"

    SCRIPT_DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)"
    if [ -d "${SCRIPT_DIR}/templates/statistics" ]; then
        echo "Synchronizing template assets from local repository..."
        cp -R "${SCRIPT_DIR}/templates" "${TARGET_DIR}/" 2>/dev/null || true
        cp -R "${SCRIPT_DIR}/.vscode" "${TARGET_DIR}/" 2>/dev/null || true
        cp "${SCRIPT_DIR}/AGENTS.md" "${TARGET_DIR}/" 2>/dev/null || true
        cp "${SCRIPT_DIR}/.cursorrules" "${TARGET_DIR}/" 2>/dev/null || true
        cp "${SCRIPT_DIR}/.gitignore" "${TARGET_DIR}/" 2>/dev/null || true
        cp "${SCRIPT_DIR}/README.md" "${TARGET_DIR}/" 2>/dev/null || true
    else
        echo "Retrieving latest template repository from remote source: ${REPO_SLUG}..."
        TARBALL_URL="https://github.com/${REPO_SLUG}/archive/refs/heads/main.tar.gz"
        TEMP_TAR="/tmp/teaching_latex_starter.tar.gz"
        
        if curl -fsSL "${TARBALL_URL}" -o "${TEMP_TAR}"; then
            echo "Unpacking remote repository archive..."
            tar -xzf "${TEMP_TAR}" -C "/tmp"
            EXTRACTED_DIR="/tmp/$(tar -tf "${TEMP_TAR}" | head -1 | cut -f1 -d"/")"
            if [ -d "${EXTRACTED_DIR}" ]; then
                cp -R "${EXTRACTED_DIR}/"* "${TARGET_DIR}/"
                [ -d "${EXTRACTED_DIR}/.vscode" ] && cp -R "${EXTRACTED_DIR}/.vscode" "${TARGET_DIR}/"
                [ -f "${EXTRACTED_DIR}/.cursorrules" ] && cp "${EXTRACTED_DIR}/.cursorrules" "${TARGET_DIR}/"
            fi
            rm -rf "${TEMP_TAR}" "${EXTRACTED_DIR}"
        else
            echo "${YELLOW}[WARN] Remote archive retrieval failed; initializing default structure.${RESET}"
        fi
    fi

    echo "${GREEN}[SUCCESS] Workspace configured at: ${TARGET_DIR}${RESET}"
}

install_latex() {
    echo "\n${BLUE}${BOLD}[2/4] Validating LaTeX Typesetting Engine...${RESET}"
    
    export PATH="${TEX_PATH}:${PATH}"

    if command -v pdflatex >/dev/null 2>&1 || [ -f "${TEX_PATH}/pdflatex" ]; then
        echo "${GREEN}[SUCCESS] Pre-existing LaTeX distribution detected on PATH.${RESET}"
    else
        echo "Downloading CTAN BasicTeX distribution package (~130 MB)..."
        PKG_URL="https://mirror.ctan.org/systems/mac/mactex/BasicTeX.pkg"
        PKG_TMP="/tmp/BasicTeX.pkg"

        curl -L "${PKG_URL}" -o "${PKG_TMP}" --progress-bar

        echo "Executing silent system package installer for BasicTeX..."
        sudo installer -pkg "${PKG_TMP}" -target /
        rm -f "${PKG_TMP}"
        echo "${GREEN}[SUCCESS] BasicTeX installed successfully.${RESET}"
    fi

    echo "Configuring persistent system PATH variables in shell profiles..."
    for PROFILE in "${HOME}/.zprofile" "${HOME}/.zshrc"; do
        if [ -f "${PROFILE}" ]; then
            if ! grep -q "${TEX_PATH}" "${PROFILE}" 2>/dev/null; then
                echo "export PATH=\"${TEX_PATH}:\$PATH\"" >> "${PROFILE}"
            fi
        else
            echo "export PATH=\"${TEX_PATH}:\$PATH\"" > "${PROFILE}"
        fi
    done
}

install_packages() {
    echo "\n${BLUE}${BOLD}[3/4] Resolving Educational LaTeX Dependencies via tlmgr...${RESET}"
    
    TLMGR_CMD="${TEX_PATH}/tlmgr"
    if [ ! -f "${TLMGR_CMD}" ]; then
        TLMGR_CMD="$(command -v tlmgr 2>/dev/null || true)"
    fi

    if [ -n "${TLMGR_CMD}" ] && [ -x "${TLMGR_CMD}" ]; then
        echo "Updating TeX Live package manager metadata..."
        sudo "${TLMGR_CMD}" update --self --quiet 2>/dev/null || true
        
        PACKAGES=(
            beamertheme-metropolis
            biblatex
            biber
            natbib
            microtype
            tcolorbox
            environ
            trimspaces
            tikzfill
            listings
            listingsutf8
            enumitem
            exam
            parskip
            csquotes
            makecell
            booktabs
            colortbl
            multirow
            xurl
            etoolbox
            pgf
            sourcesanspro
            fontawesome5
        )

        echo "Installing required template packages: ${PACKAGES[*]}..."
        sudo "${TLMGR_CMD}" install "${PACKAGES[@]}" 2>/dev/null || true
        echo "${GREEN}[SUCCESS] LaTeX packages installed and synchronized.${RESET}"
    else
        echo "${YELLOW}[WARN] tlmgr executable not found; skipping supplemental package installation.${RESET}"
    fi
}

configure_editors() {
    echo "\n${BLUE}${BOLD}[4/4] Configuring IDE Integrations (VS Code & Cursor)...${RESET}"
    
    VSCODE_APP="/Applications/Visual Studio Code.app"
    CURSOR_APP="/Applications/Cursor.app"
    
    # 1. VS Code Extension Configuration
    if [ -d "${VSCODE_APP}" ]; then
        echo "Visual Studio Code installation detected."
        VSCODE_BIN="${VSCODE_APP}/Contents/Resources/app/bin/code"
        if command -v code >/dev/null 2>&1; then
            echo "Installing James-Yu.latex-workshop extension via system code CLI..."
            code --install-extension James-Yu.latex-workshop --force >/dev/null 2>&1 || true
        elif [ -x "${VSCODE_BIN}" ]; then
            echo "Installing James-Yu.latex-workshop extension via application binary..."
            "${VSCODE_BIN}" --install-extension James-Yu.latex-workshop --force >/dev/null 2>&1 || true
        fi
        echo "${GREEN}[SUCCESS] LaTeX Workshop configured for Visual Studio Code.${RESET}"
    fi

    # 2. Cursor Extension Configuration
    if [ -d "${CURSOR_APP}" ]; then
        echo "Cursor IDE installation detected."
        CURSOR_BIN="${CURSOR_APP}/Contents/Resources/app/bin/cursor"
        if command -v cursor >/dev/null 2>&1; then
            echo "Installing James-Yu.latex-workshop extension via system cursor CLI..."
            cursor --install-extension James-Yu.latex-workshop --force >/dev/null 2>&1 || true
        elif [ -x "${CURSOR_BIN}" ]; then
            echo "Installing James-Yu.latex-workshop extension via application binary..."
            "${CURSOR_BIN}" --install-extension James-Yu.latex-workshop --force >/dev/null 2>&1 || true
        fi
        echo "${GREEN}[SUCCESS] LaTeX Workshop configured for Cursor.${RESET}"
    fi
}

finish_handoff() {
    echo "\n${GREEN}${BOLD}=================================================================="
    echo "       INSTALLATION COMPLETED SUCCESSFULLY"
    echo "==================================================================${RESET}"
    echo ""
    echo "Teaching repository location:"
    echo "Path: ${CYAN}${BOLD}${TARGET_DIR}${RESET}"
    echo ""
    echo "${BOLD}Available Templates:${RESET}"
    echo "  - templates/presentation/presentation.tex : 16:9 Modern Editorial Slides (Beamer)"
    echo "  - templates/report/report.tex             : Academic and Technical Report"
    echo "  - templates/exam/exam.tex                 : Examination with Solution Key Toggle"
    echo "  - templates/homework/assignment.tex       : Problem Set with Rubrics and Solutions"
    echo "  - templates/syllabus/syllabus.tex         : Course Syllabus and 15-Week Milestone Calendar"
    echo ""
    echo "${BOLD}Operational Instructions:${RESET}"
    echo "1. Open any template .tex file in Visual Studio Code or Cursor."
    echo "2. Press Cmd + S to compile the document automatically."
    echo "3. Consult AGENTS.md for AI prompt templates compatible with LLM assistants."
    echo ""

    if [ -d "/Applications/Visual Studio Code.app" ]; then
        open -a "Visual Studio Code" "${TARGET_DIR}" 2>/dev/null || open "${TARGET_DIR}"
    elif [ -d "/Applications/Cursor.app" ]; then
        open -a "Cursor" "${TARGET_DIR}" 2>/dev/null || open "${TARGET_DIR}"
    else
        open "${TARGET_DIR}"
    fi
}

# Execution Pipeline
print_banner
print_sudo_notice
setup_workspace
install_latex
install_packages
configure_editors
finish_handoff
