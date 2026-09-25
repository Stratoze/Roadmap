# scripts

## The loop (used every session)
- `review.py due | schedule <topic> <id> [rung] | next <topic> <id> hit|hard|miss | selftest` — transparent spaced-review scheduler (ladder 1, 3, 7, 16, 35, 90 days). Rows are created only by the `study` skill; this script never upserts. Topic names are the `curriculum/<domain>-<slug>.md` stem (e.g. `math-odes`).
- `review.py usage <topic>` — read-only derived usage freshness; usage events never change review state.
- `review.py usage <topic> <id> <introduced|practised|produced|mined|reading_session> <evidence-path> [public-note]` — append an idempotent usage event; the evidence path must exist. `reading_session` counts only an actual novel-reading session; fallback analysis uses `practised` on its separate concept.
- `diagnose.py` — vault link health (broken links + orphan notes). Exit 0 = clean. The `EXEMPT` block at the top is authoritative for carried failures. Ignores code fences; `_templates/`, `Daily/`, `Changelog/`, `_private/` never count as orphans.
- `question_signatures.py signature "<prompt>"` / `check "<prompt>" --record <technical-record>` — exact technical prompt normalization and non-reuse check.
- `python3 -m unittest discover -s scripts/tests -p "test_*.py"` — executable tests for review usage, question signatures, source schema, and technical-session records.
- `validate_learning.py` — read-only checks for canonical curriculum resource headings, stale references, and protected paths.

## Evidence (milestone workflow)
- `save.sh "scope: what changed"` — `git add -A` + commit. Refuses if `_private/` exists and isn't gitignored.
- `milestone.sh <tag> "<what proves it>"` — after committing the evidence and the completed ROADMAP checkbox, create the signed tag on that clean commit. Full Pass tags separately.

## Diagnostics (as needed)
- `versions.sh` — toolchain snapshot; run before toolchain-dependent work.
- `diagnose.py` — link/orphan check; run after structural changes.

Windows git-bash notes: invoke shell scripts with `bash scripts/*.sh` (not `+x`);
Python output needs `PYTHONIOENCODING=utf-8`. Repo is LF (`* text=auto eol=lf`).
