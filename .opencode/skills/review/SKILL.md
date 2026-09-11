---
name: Review
description: Clear due spaced reviews for the vault learning system - cold free recall first, immediate feedback, transparent ladder scheduling. Use when reviews are due or Kohaku says "review".
---

# Review - the maintain leg

Read `_system/learning/learner.md` (standing orders) and
`_system/How to Learn.md` (the Loop). The plan of record is
`.opencode/plan/vault-learning-system.md`.

1. **Load the queue**: `python3 scripts/review.py due`. Cap at 12 items per
   sitting.
2. **Backlog over the cap**: one calm amnesty line ("spacing doing its job, not
   a debt"), then offer capped set / catch-up / not now. No guilt, no streak
   language, no nagging.
3. **Per item**:
   - Show the concept id and its aim only. Then free recall, COLD: no
     re-exposure, no hints, no "remember when". Standing order 7.
   - They produce. Then collect confidence with the question tool (under 50 /
     ~70 / ~90 / certain) BEFORE any feedback.
   - Immediate feedback: the correct answer plus the exact gap. Specific, about
     the work. For computable answers, compute the key by execution, never by
     inspection.
   - On a lapse: criterion loop - re-derive, put something else in between, ask
     again; max 3 passes, stop at one clean recall.
4. **Record** with `python3 scripts/review.py next <topic> <id> <hit|hard|miss>`:
   - hit -> rung +1 (cap 5); a clean hit at rung >= 4 sets state `solid`
   - hard -> same rung
   - miss -> one rung back (floor 0) plus a same-session relearn attempt; still
     shaky -> `python3 scripts/review.py schedule <topic> <id> 0` (reset)
   - two or more lapses on a concept -> re-encode differently next session
     (new analogy or contrast)
5. **Claims only** (MVM / Full Pass) route to **assessor**. Ordinary reps never
   do.
6. **Close**: items -> outcomes, one honest number only if real growth, next due
   date. No streaks. If the queue was big and they stopped early, say what is
   left, zero guilt.

Rules:

- Never re-expose before the probe. Feedback after retrieval, never before.
- If an item is truly obsolete, offer `retire` style treatment: remove it from
  the table with a `## Log` line, never silently.
- Nothing leaves the session until `review.py` recorded it.
