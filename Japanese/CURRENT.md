# Japanese — Current Session Handoff

**Updated:** 2026-09-26
**Status:** Fresh reset; no active Japanese review backlog.

This is the single mutable handoff for the next Japanese session. Read it
before choosing a branch. Curriculum files own concept state; this file owns
the **next action** and current session context. Rewrite this file at the end
of every Japanese session so the next agent never has to infer what to do.

## Start here next time

1. Invoke the `japanese` skill.
2. **Do not open with a generic due-review pass.** Begin with a short
   conversation warm-up, then teach/confirm the first usable grammar contrast.
3. First active grammar path: `jp-yokubi-00` → `jp-yokubi-01` →
   `jp-yokubi-02` → `jp-yokubi-03`. Kana are assumed known; the grammar
   sequence starts from sentence anatomy.
4. Use the L1 ramp: Japanese terms/examples with a concise English scaffold;
   move toward Japanese-first as the learner progresses.

## Grammar frontier

- Next concept: `jp-yokubi-00` (Yokubi Lesson 0, sentence anatomy).
- Source locator: <https://yoku.bi/Section1/Part1/Lesson0.html>, reached
  through [[Japanese/SOURCES|the source map]].
- Verify the locator resolves and the spine still matches before teaching.
  `build_japanese_curriculum.py` is **read-only** — it prints
  `verified N Yokubi concept rows` and writes nothing, so run it freely
  mid-session. Only `build_japanese_source_map.py` regenerates and writes
  `Japanese/source-map.json`; it is not a teaching step:

  ```bash
  python3 scripts/build_japanese_curriculum.py
  ```

## Current state

- Active grammar concepts: reset to `unknown`; no Japanese due reviews.
- Reading gate: **0 / 30 actual novel-reading sessions**. Derive the number,
  never hand-count it, with `python3 scripts/review.py usage japanese-reading`.
- Reading mode: English explanation first for sessions 1–30; from session 31
  the learner attempts Japanese first, then English correction. Sentence-analysis
  fallback records `practised` and never counts toward the gate.
- Output: fresh; start with i+1 conversation, not a backlog review.
- Immersion: optional input/logging; no quota.
- Anki: 20–30 minutes; vocabulary owner. If the local bridge is available,
  run `python3 scripts/anki_bridge.py due`; otherwise use Anki directly.
- Active source: the Yokubi spine in [[Japanese/SOURCES|the source map]] owns
  sequencing and lesson locators. The per-lesson locator is opened and verified
  JIT through the `resources` skill; no source text is pre-selected.

## Next action

Run one fresh Japanese session:

```text
conversation warm-up
→ one ground-up grammar contrast
→ immediate practice
→ one small reading or sentence-analysis task
→ append evidence events
→ rewrite this file with the next action
```

## Evidence and archive

- Active usage events: curriculum `## Usage events` tables.
- Last Japanese evidence: none since the 2026-09-26 reset.
- Pre-reset evidence: [[_system/learning/archive/japanese-progress-reset-2026-09-26|archived reset record]].
- Raw learner work: `_private/` only.

## Source notes and blockers

- No sourcing blocker is open. `Japanese/source-map.json` was regenerated from
  the verified private checkout; it carries the current verification block and
  IMABI licence note.

## Close contract

Before ending a Japanese session, update:

- `Updated` date;
- next action and branch (`## Next action`);
- grammar frontier (`## Grammar frontier`);
- reading session count, re-derived from `review.py usage`;
- last evidence link (`## Evidence and archive`);
- any source blocker or unresolved question
  (`## Source notes and blockers`).

Do not leave this file describing a session that has already happened.
