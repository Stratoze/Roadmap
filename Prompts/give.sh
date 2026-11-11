#!/bin/bash
# Prints a ready prompt or key question, never an answer.
# Usage: bash Prompts/give.sh chat | T11 | A1.1
#        bash Prompts/give.sh quiz G19     (quiz questions, answers cut)
#        bash Prompts/give.sh variant G13  (Variant question, answer cut)
#        bash Prompts/give.sh page G19     (the page to read)
cd "$(dirname "$0")" || exit 1

# The key block of one BACKLOG item, from its ### line to the next ###.
item() { awk -v id="$1" '/^### /{on = ($0 ~ "\\] " id " ")} on' ../BACKLOG.md; }

case "$1" in
  quiz|variant|page)
    block=$(item "$2")
    [ -n "$block" ] || { echo "MISSING: no BACKLOG item $2"; exit 1; } ;;
esac

case "$1" in
  chat) cat chat.txt ;;
  quiz) echo "$block" | awk '/^Quiz:/{q=1;next} /^[A-Z][a-z]*:/{q=0} q' | sed 's/ *→.*//' ;;
  variant)
    v=$(echo "$block" | grep '^Variant:' | sed 's/^Variant: *//; s/ *→.*//')
    [ -n "$v" ] && echo "$v" || { echo "MISSING: $2 has no Variant"; exit 1; } ;;
  page)
    p=$(echo "$block" | grep '^Page:' | sed 's/^Page: *//')
    [ -n "$p" ] && echo "$p" || { echo "MISSING: $2 has no Page line (add to Proposals.md)"; exit 1; } ;;
  *)
    [ -f "$1.txt" ] || { echo "MISSING: $1 has no prompt file"; exit 1; }
    case "$1" in A*|M*) head=mentor.txt ;; *) head=tutor.txt ;; esac
    grep '^SEARCH:' "$1.txt"; echo "----- copy below into Gemini -----"
    cat "$head"; grep -v '^SEARCH:' "$1.txt" ;;
esac
