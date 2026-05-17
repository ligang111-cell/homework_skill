#!/usr/bin/env bash
set -euo pipefail

CYAN='\033[36m'
GREEN='\033[32m'
YELLOW='\033[33m'
RED='\033[31m'
RESET='\033[0m'

echo -e "${CYAN}==========================================${RESET}"
echo -e "${CYAN}          Auto Deploy Script${RESET}"
echo -e "${CYAN}==========================================${RESET}"
echo

echo -e "${YELLOW}[1/4] Adding changes...${RESET}"
git add .

echo
echo -e "${YELLOW}[2/4] Committing changes...${RESET}"
if git diff --cached --quiet; then
  echo -e "${YELLOW}No staged changes to commit.${RESET}"
else
  timestamp="$(date '+%Y-%m-%d %H:%M:%S')"
  git commit -m "Site update ${timestamp}"
fi

echo
echo -e "${YELLOW}[3/4] Pushing to remote...${RESET}"
if ! git push; then
  echo
  echo -e "${RED}Error: Git push failed.${RESET}"
  exit 1
fi

echo
echo -e "${GREEN}==========================================${RESET}"
echo -e "${GREEN}          Deploy Success!${RESET}"
echo -e "${GREEN}==========================================${RESET}"
