#!/usr/bin/env bash
# ============================================================
# Design Master Agent — Installer
# ينزّل ويثبّت نظام design-master على وكيل AI المختار
# ============================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

REPO_URL="https://github.com/4zobir89-lab/design-master-agent"
REPO_RAW="https://raw.githubusercontent.com/4zobir89-lab/design-master-agent/main"

print_banner() {
    echo -e "${BLUE}"
    echo "╔════════════════════════════════════════════════════════════╗"
    echo "║                                                              ║"
    echo "║         🎨 Design Master Agent — Installer                   ║"
    echo "║                                                              ║"
    echo "║   Turn any LLM into a Senior Creative Director               ║"
    echo "║                                                              ║"
    echo "╚════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_help() {
    print_banner
    echo "Usage: $0 --target <platform>"
    echo
    echo "Platforms:"
    echo "  claude      Install for Claude Code"
    echo "  cursor      Install for Cursor IDE"
    echo "  codex       Install for Codex CLI"
    echo "  gemini      Install for Gemini CLI"
    echo "  copilot     Install for GitHub Copilot (VS Code)"
    echo "  all         Install for all of the above"
    echo
    echo "Options:"
    echo "  --target <p>   Target platform (required)"
    echo "  --help, -h     Show this help"
    echo
    echo "Examples:"
    echo "  $0 --target claude"
    echo "  $0 --target all"
    echo "  curl -fsSL ${REPO_RAW}/scripts/install.sh | bash -s -- --target claude"
}

check_python() {
    if command -v python3 &>/dev/null; then
        PYTHON=python3
    elif command -v python &>/dev/null; then
        PYTHON=python
    else
        echo -e "${RED}❌ Python 3.9+ is required but not found.${NC}"
        echo "Install from: https://python.org/downloads/"
        exit 1
    fi

    version=$($PYTHON --version 2>&1 | awk '{print $2}')
    major=$(echo $version | cut -d. -f1)
    minor=$(echo $version | cut -d. -f2)

    if [ "$major" -lt 3 ] || ([ "$major" -eq 3 ] && [ "$minor" -lt 9 ]); then
        echo -e "${RED}❌ Python 3.9+ required, found $version${NC}"
        exit 1
    fi
    echo -e "${GREEN}✓ Python $version found ($PYTHON)${NC}"
}

check_git() {
    if ! command -v git &>/dev/null; then
        echo -e "${RED}❌ git is required but not found.${NC}"
        exit 1
    fi
    echo -e "${GREEN}✓ git found${NC}"
}

clone_repo() {
    local tmp_dir=$(mktemp -d)
    echo -e "${BLUE}📥 Cloning design-master-agent to $tmp_dir...${NC}"
    git clone --depth 1 "$REPO_URL" "$tmp_dir/design-master-agent"
    echo "$tmp_dir/design-master-agent"
}

install_for_claude() {
    local src=$1
    local target_dir="$HOME/.claude/skills/design-master"

    echo -e "${BLUE}📦 Installing for Claude Code...${NC}"
    mkdir -p "$HOME/.claude/skills"
    rm -rf "$target_dir"
    cp -r "$src" "$target_dir"
    chmod +x "$target_dir/scripts/"*.py 2>/dev/null || true
    echo -e "${GREEN}✓ Installed to: $target_dir${NC}"

    echo
    echo -e "${YELLOW}📋 To activate:${NC}"
    echo "  In Claude Code, say:"
    echo "    'Use the design-master skill to build me a website for X'"
    echo
    echo "  Or explicitly:"
    echo "    'Read ~/.claude/skills/design-master/AGENTS.md and apply the methodology'"
}

install_for_cursor() {
    local src=$1
    local target_dir="$HOME/.cursor/skills/design-master"

    echo -e "${BLUE}📦 Installing for Cursor...${NC}"
    mkdir -p "$HOME/.cursor/skills"
    rm -rf "$target_dir"
    cp -r "$src" "$target_dir"
    chmod +x "$target_dir/scripts/"*.py 2>/dev/null || true
    echo -e "${GREEN}✓ Installed to: $target_dir${NC}"

    echo
    echo -e "${YELLOW}📋 To activate:${NC}"
    echo "  1. Open Cursor Settings → AI → Skills"
    echo "  2. Click 'Add Skill'"
    echo "  3. Select path: $target_dir"
    echo "  4. Enable the skill"
    echo
    echo "  Then in chat: '@design-master build me a website for X'"
}

install_for_codex() {
    local src=$1
    local target_dir="$HOME/.codex/skills/design-master"

    echo -e "${BLUE}📦 Installing for Codex CLI...${NC}"
    mkdir -p "$HOME/.codex/skills"
    rm -rf "$target_dir"
    cp -r "$src" "$target_dir"
    chmod +x "$target_dir/scripts/"*.py 2>/dev/null || true
    echo -e "${GREEN}✓ Installed to: $target_dir${NC}"

    echo
    echo -e "${YELLOW}📋 To activate:${NC}"
    echo "  codex --skill design-master 'build me a website for X'"
}

install_for_gemini() {
    local src=$1
    local target_dir="$HOME/.gemini/skills/design-master"

    echo -e "${BLUE}📦 Installing for Gemini CLI...${NC}"
    mkdir -p "$HOME/.gemini/skills"
    rm -rf "$target_dir"
    cp -r "$src" "$target_dir"
    chmod +x "$target_dir/scripts/"*.py 2>/dev/null || true
    echo -e "${GREEN}✓ Installed to: $target_dir${NC}"

    echo
    echo -e "${YELLOW}📋 To activate:${NC}"
    echo "  gemini --skill design-master 'build me a website for X'"
}

install_for_copilot() {
    local src=$1

    echo -e "${BLUE}📦 Installing for GitHub Copilot (VS Code)...${NC}"

    # Check if in a workspace
    if [ ! -d ".vscode" ]; then
        mkdir -p .vscode
    fi

    local target_dir=".vscode/copilot-skills/design-master"
    rm -rf "$target_dir"
    cp -r "$src" "$target_dir"
    chmod +x "$target_dir/scripts/"*.py 2>/dev/null || true
    echo -e "${GREEN}✓ Installed to: $target_dir${NC}"

    # Update settings.json
    local settings_file=".vscode/settings.json"
    if [ ! -f "$settings_file" ]; then
        echo '{}' > "$settings_file"
    fi

    echo
    echo -e "${YELLOW}📋 To activate:${NC}"
    echo "  Add to .vscode/settings.json:"
    echo '  {'
    echo '    "github.copilot.chat.codeGeneration.instructions": ['
    echo '      "When user asks for a website, read .vscode/copilot-skills/design-master/AGENTS.md and follow the 7-phase methodology"'
    echo '    ]'
    echo '  }'
}

# ============================================================
# Main
# ============================================================

TARGET=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --target)
            TARGET="$2"
            shift 2
            ;;
        --help|-h)
            print_help
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            print_help
            exit 1
            ;;
    esac
done

if [ -z "$TARGET" ]; then
    print_help
    exit 1
fi

print_banner

# Check dependencies
check_git
check_python

# Clone
SRC_DIR=$(clone_repo)
trap "rm -rf $(dirname $SRC_DIR)" EXIT

echo

case "$TARGET" in
    claude)
        install_for_claude "$SRC_DIR"
        ;;
    cursor)
        install_for_cursor "$SRC_DIR"
        ;;
    codex)
        install_for_codex "$SRC_DIR"
        ;;
    gemini)
        install_for_gemini "$SRC_DIR"
        ;;
    copilot)
        install_for_copilot "$SRC_DIR"
        ;;
    all)
        install_for_claude "$SRC_DIR"
        echo
        install_for_cursor "$SRC_DIR"
        echo
        install_for_codex "$SRC_DIR"
        echo
        install_for_gemini "$SRC_DIR"
        ;;
    *)
        echo -e "${RED}Unknown target: $TARGET${NC}"
        echo "Valid targets: claude, cursor, codex, gemini, copilot, all"
        exit 1
        ;;
esac

echo
echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║                                                              ║${NC}"
echo -e "${GREEN}║         🎉 Installation Complete!                            ║${NC}"
echo -e "${GREEN}║                                                              ║${NC}"
echo -e "${GREEN}║   Try: 'Build me a website for X using design-master'        ║${NC}"
echo -e "${GREEN}║                                                              ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
