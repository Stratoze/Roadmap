#!/usr/bin/env bash
# Quick session save. Usage: ./scripts/save.sh "phase0: derived FBD for 2-link arm"
# Solo-vault default is -A with a staging preview below; scope with `git add <paths>` when mixing domains.
# Tags never leave the laptop unless pushed: remember `git push origin main --tags`.
set -euo pipefail
MSG="${1:?usage: save.sh \"scope: what changed\"}"
echo "--- staging preview ---"
git status --short
git add -A
git commit -m "$MSG"
echo "✅ saved -> push when you want an off-site backup: git push (tags: git push origin main --tags)"
