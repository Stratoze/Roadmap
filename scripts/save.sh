#!/usr/bin/env bash
# Quick session save. Usage: ./scripts/save.sh "phase0: derived FBD for 2-link arm"
set -euo pipefail
MSG="${1:?usage: save.sh \"scope: what changed\"}"
git add -A
git commit -m "$MSG"
echo "✅ saved -> push when you want an off-site backup: git push"
