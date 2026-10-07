#!/usr/bin/env bash
# Quick session save. Usage: ./scripts/save.sh "phase0: derived FBD for 2-link arm"
set -euo pipefail
MSG="${1:?usage: save.sh \"scope: what changed\"}"
# Private companion repo guard: never stage verbatim learner text.
if [ -d _private ]; then
  git check-ignore -q _private/ || { echo "BLOCKED: _private/ is not gitignored" >&2; exit 1; }
fi
git add -A
git commit -m "$MSG"
echo "✅ saved -> push when you want an off-site backup: git push"
