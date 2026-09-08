# Per-machine Engram env — copy into your shell rc, DO NOT commit filled values.
# Mac (~/.zshrc):
#   export ENGRAM_RUNNER="python3 $HOME/engram/scripts/engram.py"
#   export ENGRAM_HOME="$HOME/Documents/Obsidian/_system/engram"
# Win (~/.bashrc, git-bash):
#   export ENGRAM_RUNNER="python3 $HOME/.config/opencode/scripts/engram.py"
#   export ENGRAM_HOME="$HOME/Documents/Obsidian/_system/engram"
# Adjust ENGRAM_HOME to your actual vault path. AGENT.md session-start refuses
# to run when ENGRAM_RUNNER is unset (verbatim-safe guard).
# Windows console encoding (engram emits UTF-8; the Win cp932 codepage crashes on it —
# verified `UnicodeEncodeError: cp932` without this export):
#   export PYTHONIOENCODING=utf-8
# (Prefix every runner invocation with it if exports don't stick.)
