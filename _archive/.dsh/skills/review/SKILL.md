---
name: Review
description: Clear due spaced reviews for the vault learning system - cold free recall first, immediate feedback, transparent ladder scheduling. Use when reviews are due or Kohaku says "review".
---

# Review - the maintain leg

Read `_system/learning/learner.md` (standing orders) and
`_system/How to Learn.md` (the Loop). Use the active curriculum dossier and
usage events; archived build plans are provenance only.

One item per message, in order: recall -> confidence -> feedback -> record.
Never batch items or pre-empt later ones. In the daily sequence, Japanese comes
first; due review is the second block. If the estimated due workload exceeds
30 minutes, work for 30 minutes, record the remaining backlog, and continue to
the chosen target rather than clearing everything.

1. **Load the queue**: `python3 scripts/review.py due`. Cap at 12 items or
   30 minutes per sitting, whichever comes first. Use
   `python3 scripts/review.py usage <topic>` read-only to find naturally stale
   items; usage is a selection signal, not a second schedule.
2. **Natural-use events**: when a learner deliberately practises or produces a
   concept, append an idempotent event with `review.py usage`; passive reading
   or immersion exposure is not an event. `produced` is independent correct use;
   `practised` is an attempt. Never alter `state`, `rung`, or `next_review` from
   a usage event.
3. **Backlog over the cap**: one calm amnesty line ("spacing doing its job, not
   a debt"), then offer capped set / catch-up / not now. No guilt, no streak
   language, no nagging.
4. **Per item**:
   - Show the concept id and its aim only. Then free recall, COLD: no
     re-exposure, no hints, no "remember when". Standing order 7. The answer must include the standard
      term (standing order 10): simple-words reasoning earns the understanding
      half; the canonical term earns the other half. A right idea with a
      wrong or missing term is a `hard`, not a `hit`.
   - They produce. Then collect confidence with the question tool (under 50 /
     ~70 / ~90 / certain) BEFORE any feedback.
   - Immediate feedback: the correct answer plus the exact gap. Specific, about
     the work. For computable answers, compute the key by execution, never by
     inspection.
   - On a lapse: criterion loop - re-derive, put something else in between, ask
     again; max 3 passes, stop at one clean recall.
5. **Record** with `python3 scripts/review.py next <topic> <id> <hit|hard|miss>`:
   - hit -> rung +1 (cap 5); a clean hit at rung >= 4 sets state `solid`
   - hard -> same rung
   - miss -> one rung back (floor 0) plus a same-session relearn attempt; still
     shaky -> `python3 scripts/review.py schedule <topic> <id> 0` (reset)
   - two or more lapses on a concept -> re-encode differently next session
     (new analogy or contrast)
6. **Claims only** (MVM / Full Pass) route to **assessor**. Ordinary reps never
   do.
7. **Close**: items -> outcomes, one honest number only if real growth, next due
   date. No streaks. If the queue was big and they stopped early, say what is
   left, zero guilt.

Rules:

- Never re-expose before the probe. Feedback after retrieval, never before.
- If an item is truly obsolete, offer `retire` style treatment: remove it from
  the table with a `## Log` line, never silently.
- Nothing leaves the session until `review.py` recorded it.
