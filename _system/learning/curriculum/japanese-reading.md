# Japanese Reading

## Goal
- Scoping answer (verbatim, 2026-09-21): "maybe also reading ?"
- Learner chooses the novel, edition, and page/section.
- Reading gate: 30 actual novel-reading sessions use an English explanation
  first. From session 31 the learner attempts Japanese first, then English
  explanation/correction. Sentence-analysis fallback does not count. This
  paragraph is the canonical wording of the gate; other Japanese files repeat
  it rather than restating a variant.
- Pacing: alongside foundations; priority JP >= mechatronics

## Map
- Start with material the learner chooses and can sustain. The tutor helps
  when a page is too dense, but does not silently substitute a recommended
  novel.
- For each session: receive the page screenshot/context, ask for the learner's
  interpretation, then correct the important Japanese and connect useful words
  or grammar to the current curriculum.
- Raw screenshots and passages are transient. Public records contain only short
  summaries, opaque references, and links.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| read-30-session-gate | reach 30 actual novel-reading sessions, which switches the reading mode to Japanese-first from session 31 | - | unknown | 0 | - | reset 2026-09-26; sessions=0 |
| read-page-interpretation | explain what a page is doing, not merely translate it | jp-yokubi-00 | unknown | 0 | - | reset 2026-09-26 |
| read-sentence-fallback | analyse one level-appropriate sentence when reading is skipped | jp-yokubi-00 | unknown | 0 | - | reset 2026-09-26 |

## Resources
- Active source/material selected JIT. Stable reader/lookup links live in
  [[Japanese/Resources]].

## Misconceptions
- (none logged yet)

## Problems
| id | problem | source | theory | attempts | status |
|----|---------|--------|--------|----------|--------|

## Links
- Rests on: japanese-grammar
- Teaches: japanese-immersion; mined words feed Anki; patterns feed output
- Lessons: -

## Usage events
| date | event_id | concept/item_ref | event | evidence | public note |
|------|----------|------------------|-------|----------|-------------|

Each `reading_session` event is one actual novel-reading session. The
`read-sentence-fallback` row is deliberately separate and never increments
this gate. The current count is derived, not typed:
`python3 scripts/review.py usage japanese-reading` prints `sessions=`.

## Log
- 2026-09-26 - active reading gate reset to 0; no due reviews. Next action is
  in [[Japanese/CURRENT|current Japanese session]].
