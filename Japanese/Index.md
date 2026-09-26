# Japanese

Japanese is one learning system with four coordinated modes:

- **Grammar:** one usable contrast at a time, with Japanese-first explanation,
  English bridge, neighbouring forms, register, and immediate practice.
- **Output:** i+1 conversation using what is known plus a small useful addition.
- **Reading:** learner-chosen novel; English-first for 30 actual reading
  sessions, Japanese-first afterwards. Sentence-analysis fallback does not
  advance that count.
- **Immersion:** approximately three hours of input with optional, quota-free
  logging. Anki owns vocabulary.

The ordinary day is 4–5 hours: ~3 hours immersion, ~30 minutes Anki, and
30–90 minutes of deliberate grammar/conversation/reading work.

## Start here

Read [[Japanese/CURRENT|current session handoff]] first. It names the next
action, current grammar frontier, reading count, and the last evidence. After
every Japanese session, the tutor rewrites that file before closing.

For a fresh/reset session, do **not** begin with a generic review backlog.
Start with conversation, then one ground-up grammar contrast, then reading or
sentence analysis. The `japanese` skill reads this handoff and the curriculum
frontier.

- [[Japanese/Resources|Resources]] — compact discovery links and JIT source
  request policy; not a source library or tracker.
- Due grammar/output review: `python3 scripts/review.py due`.
- Reading gate count: `python3 scripts/review.py usage japanese-reading` (the `read-30-session-gate` row reports `sessions=`).
- Technical sequencing: [[Mechatronics/ROADMAP|Mechatronics roadmap]].
