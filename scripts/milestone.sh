#!/usr/bin/env bash
# The evidence trait. Usage: ./scripts/milestone.sh <tag> "<what proves it>"
# Example: ./scripts/milestone.sh m0.1-mvm "0.1 MVM: blinky flashed, toolchain ok, Anki deck created"
set -euo pipefail
TAG="${1:?usage: milestone.sh <tag> \"<message>\"}"
MSG="${2:?usage: milestone.sh <tag> \"<message>\"}"
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "⚠️  uncommitted changes - commit the evidence first (./scripts/save.sh), then re-run."
  git status --short; exit 1
fi
git tag -a "$TAG" -m "$MSG"
echo "✅ tagged $TAG"
echo "   1) flip the milestone ⬜→✅ in Mechatronics/ROADMAP.md"
echo "   2) ./scripts/save.sh \"roadmap: mark $TAG complete\""
echo "   3) git push origin main --tags"
