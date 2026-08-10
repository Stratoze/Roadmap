#!/usr/bin/env bash
# Snapshot toolchain versions (run at each phase deload).
echo "=== Toolchain versions - $(date +%F) ==="
for cmd in git python3 arm-none-eabi-gcc gcc cmake make openocd kicad-cli; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "%-20s %s\n" "$cmd" "$("$cmd" --version 2>&1 | head -1)"
  else
    printf "%-20s (not installed)\n" "$cmd"
  fi
done
