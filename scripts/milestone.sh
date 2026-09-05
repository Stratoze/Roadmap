#!/usr/bin/env bash
# The evidence trait. Usage: ./scripts/milestone.sh <tag> <evidence-path> "<what proves it>"
# Example: ./scripts/milestone.sh m0.2-full Mechatronics/milestones/evidence/0.2-3link-fk.md "0.2 Full: 3-link FK, dot-as-projection"
# Order: flip ROADMAP ⬜→✅ + save FIRST, then tag (the tag must contain the ✅ state).
# Signing: SSH signing (git tag -s with gpg.format ssh). One key, documented in LAB_INFRASTRUCTURE.
set -euo pipefail
TAG="${1:?usage: milestone.sh <tag> <evidence-path> \"<message>\"}"
EV="${2:?usage: milestone.sh <tag> <evidence-path> \"<message>\"}"
MSG="${3:?usage: milestone.sh <tag> <evidence-path> \"<message>\"}"
case "$TAG" in
  m[0-9]*.[0-9]*-mvm|m[0-9]*.[0-9]*-full|p[0-9]-complete) ;;
  *) echo "❌ tag must match m<phase>.<n>-(mvm|full) or p<phase>-complete (got: $TAG)"; exit 1 ;;
esac
[ -e "$EV" ] || { echo "❌ evidence path missing: $EV"; exit 1; }
git diff --quiet && git diff --cached --quiet || { echo "⚠️  uncommitted changes - commit first (./scripts/save.sh), then re-run."; git status --short; exit 1; }
git show --stat HEAD | grep -q "$EV" || { echo "⚠️  HEAD does not touch $EV - commit the evidence first."; exit 1; }
git tag -s "$TAG" -m "$MSG"
echo "✅ tagged $TAG — push: git push origin main --tags"
