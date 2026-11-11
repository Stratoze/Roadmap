#!/usr/bin/env bash
# Find grammar lessons that contain every given form.
# Usage: bash Prompts/page.sh かった なかった よかった
# Clones Cure Dolly and yoku.bi (GitHub) once per container, then lists
# the lessons whose text contains all the forms, lowest lesson first.
set -euo pipefail
[ $# -ge 1 ] || { echo "usage: page.sh FORM [FORM...]"; exit 1; }
dir="${TMPDIR:-/tmp}/grammar-src"
mkdir -p "$dir"
fetch() { [ -d "$dir/$2" ] || git clone -q --depth 1 "https://github.com/$1" "$dir/$2"; }
fetch kellenok/cure-script cure-dolly
fetch Morgawr/yokubi yokubi

search() {
  local name=$1 path=$2 f hits=0
  echo "== $name"
  while IFS= read -r f; do
    local ok=1
    for form in "${forms[@]}"; do grep -q -- "$form" "$f" || { ok=0; break; }; done
    if [ $ok = 1 ]; then
      echo "${f#$dir/}  |  $(grep -m1 '^#' "$f" | sed 's/^#* *//')"
      hits=$((hits+1))
    fi
  done < <(find "$dir/$path" -name '*.md' | sort -V)
  [ $hits -gt 0 ] || echo "(none)"
}
forms=("$@")
search "Cure Dolly (https://kellenok.github.io/cure-script/)" cure-dolly/config/docs/en
search "yoku.bi (https://yoku.bi/)" yokubi/src
