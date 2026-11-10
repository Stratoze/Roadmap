#!/bin/bash
# Prints a ready prompt. Usage: bash Prompts/give.sh chat | bash Prompts/give.sh T11
cd "$(dirname "$0")" || exit 1
if [ "$1" = chat ]; then cat chat.txt; exit; fi
[ -f "$1.txt" ] || { echo "MISSING: $1 has no prompt file"; exit 1; }
grep '^SEARCH:' "$1.txt"; echo "----- copy below into Gemini -----"
cat tutor.txt; grep -v '^SEARCH:' "$1.txt"
