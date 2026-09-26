#!/usr/bin/env bash
# Create the durable signed milestone tag after evidence + checkbox are committed.
# Usage: bash scripts/milestone.sh <tag> "<what proves it>" --gate mvm|full --evidence <path> [--check-only]
set -euo pipefail
if [ "$#" -lt 2 ]; then
  echo 'usage: milestone.sh <tag> "<what proves it>" --gate mvm|full --evidence <path> [--check-only]' >&2
  exit 2
fi
TAG="$1"
MSG="$2"
shift 2
GATE=""
EVIDENCE=""
CHECK_ONLY=0
while [ "$#" -gt 0 ]; do
  case "$1" in
    --gate) GATE="${2:?--gate needs mvm or full}"; shift 2 ;;
    --evidence) EVIDENCE="${2:?--evidence needs a file path}"; shift 2 ;;
    --check-only) CHECK_ONLY=1; shift ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done
if [ "$GATE" != "mvm" ] && [ "$GATE" != "full" ]; then
  echo "--gate must be mvm or full" >&2
  exit 2
fi
if [ -z "$EVIDENCE" ]; then
  echo "evidence metadata is required: --evidence <path>" >&2
  exit 2
fi
if [ ! -f "$EVIDENCE" ]; then
  echo "evidence file does not exist: $EVIDENCE" >&2
  exit 2
fi

# Canonical assessor gate record: one "gate_met: yes" and one "gate_earned: mvm|full|none"
# line, bullet-prefixed as the record template writes it. The LAST value in the file
# wins, so an older gate claim can never tag over a later lapsed verdict.
last_field() {
  local field="$1" file="$2" value
  value=$(grep -iE "^[[:space:]]*(-[[:space:]]*)?\**${field}\**[[:space:]]*:" "$file" \
    | sed -E 's/^[^:]*:[[:space:]]*//' \
    | sed -E 's/`//g; s/[[:space:]]+$//' \
    | grep -v '^[[:space:]]*$' \
    | tail -n 1 \
    | tr '[:upper:]' '[:lower:]' || true)
  printf '%s' "$value"
}

EARNED="$(last_field gate_earned "$EVIDENCE")"
MET="$(last_field gate_met "$EVIDENCE")"
if [ -z "$EARNED" ]; then
  echo "evidence records no gate_earned value: $EVIDENCE" >&2
  echo "  add the assessor's canonical line, e.g. '- gate_earned: $GATE'" >&2
  exit 2
fi
if [ "$EARNED" != "$GATE" ]; then
  echo "evidence gate_earned is '$EARNED', not '$GATE' (the last gate_earned line wins): $EVIDENCE" >&2
  echo "  a partial/lapsed/none verdict cannot earn a gate; re-run the assessor" >&2
  exit 2
fi
if [ "$MET" != "yes" ]; then
  echo "evidence gate_met is '${MET:-absent}', not 'yes': $EVIDENCE" >&2
  echo "  record the canonical line '- gate_met: yes' beside the earned gate" >&2
  exit 2
fi
if [ "$CHECK_ONLY" = "1" ]; then
  echo "gate ok: $EVIDENCE records gate_met: yes and gate_earned: $GATE"
  exit 0
fi
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "⚠️  uncommitted changes - commit the evidence and completed ROADMAP checkbox first, then re-run."
  git status --short
  exit 1
fi
git tag -s "$TAG" -m "$MSG"
echo "✅ tagged $TAG ($GATE)"
echo "   ROADMAP checkbox and evidence are already in the tagged commit."
echo "   ./scripts/save.sh is not needed for the tag; push when ready: git push origin main --tags"
