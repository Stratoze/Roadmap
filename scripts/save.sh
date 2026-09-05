#!/usr/bin/env bash
# Quick session save. Usage: ./scripts/save.sh "phase0: derived FBD for 2-link arm"
# Scoped by habit: prefer `git add <paths>` for the domain you touched; -A is the fallback.
# Tags never leave the laptop unless pushed: remember `git push origin main --tags`.
set -euo pipefail
MSG="${1:?usage: save.sh \"scope: what changed\"}"
echo "--- staging preview ---"
git status --short
git add -A
git commit -m "$MSG"
echo "✅ saved -> push when you want an off-site backup: git push (tags: git push origin main --tags)"
