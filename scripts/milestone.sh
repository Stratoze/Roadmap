#!/usr/bin/env bash
# Create the durable signed milestone tag after evidence + checkbox are committed.
# Usage: bash scripts/milestone.sh <tag> "<what proves it>"
set -euo pipefail
TAG="${1:?usage: milestone.sh <tag> \"<message>\"}"
MSG="${2:?usage: milestone.sh <tag> \"<message>\"}"
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "⚠️  uncommitted changes - commit the evidence and completed ROADMAP checkbox first, then re-run."
  git status --short
  exit 1
fi
git tag -s "$TAG" -m "$MSG"
echo "✅ tagged $TAG"
echo "   ROADMAP checkbox and evidence are already in the tagged commit."
echo "   ./scripts/save.sh is not needed for the tag; push when ready: git push origin main --tags"
