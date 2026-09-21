# scripts

## The loop (used every session)
- `review.py due | schedule <topic> <id> [rung] | next <topic> <id> hit|hard|miss | selftest` — transparent spaced-review scheduler (ladder 1, 3, 7, 16, 35, 90 days). Rows are created only by the `study` skill; this script never upserts. Topic names are the `curriculum/<domain>-<slug>.md` stem (e.g. `math-odes`).
- `diagnose.py` — vault link health (broken links + orphan notes). Exit 0 = clean. The `EXEMPT` block at the top is authoritative for carried failures. Ignores code fences; `_templates/`, `Daily/`, `Changelog/`, `_private/` never count as orphans.

## Evidence (milestone workflow)
- `save.sh "scope: what changed"` — `git add -A` + commit. Refuses if `_private/` exists and isn't gitignored.
- `milestone.sh <tag> "<what proves it>"` — signed tag on a clean tree (e.g. `m0.1-mvm`). Then flip ⬜→✅ in `Mechatronics/ROADMAP.md` and save again.

## Diagnostics (as needed)
- `versions.sh`, `cold_tools.sh` — toolchain checks; see `AGENTS.md` Toolchain section.

Windows git-bash notes: invoke shell scripts with `bash scripts/*.sh` (not `+x`);
Python output needs `PYTHONIOENCODING=utf-8`. Repo is LF (`* text=auto eol=lf`).
