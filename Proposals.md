# Opus inbox

Everything waiting on Opus, in one place. Pull-based: nothing runs on its
own, no schedule. Haiku adds items; only the learner calls Opus; when
called, Opus works **Open** top-down and moves each item to **Done** with
its decision. Haiku never acts on an item here.

## How items get here (Haiku)

1. **Proposals** from the learner or from Haiku: one item each, with date
   and source. Never anywhere else (`AGENTS.md` "Files").
2. **Audit lines:** any "check for Opus" (or older "check on Sunday") line in `Learned/` gets an item
   pointing to it.
3. **Pull signals.** At session start, check these; if one is true and not
   already listed, add an item:
   - A `BACKLOG.md` queue (grammar, technical, chat openers) has 5 or
     fewer keyed items left → "Refill <queue>: next keys from <item>."
   - The next item in a queue has no key → "Keys needed from <item>." (That
     item is skipped until then.)
   - 7 days or more since the last audit (see below) → "Audit due: the
     learner pastes one Japanese chat and one tutor chat."
   - The learner says Haiku accepted a wrong answer → "Move <task type> to
     Sonnet?"
   - 7 days or more since the last fitness review (`Learned/fitness.md`)
     → "Fitness review due."
   Last audit: 2026-10-25 (Opus).
4. At session start, if **Open** has any item, say once:
   - "Call Opus now: <item>." when an item blocks today's work (the next
     queue item has no key, a wrong answer was accepted), or **Open** has 3
     or more items, or an audit or fitness review is due.
   - Otherwise: "Opus inbox: N open (top: <first item>)."
   Say it once per session; then carry on with the work.

## Open

### Refill: chat openers and grammar keys
- Chat openers: 10 left. Grammar keys: G12b-G26 (15 items, ~5-8 sessions
  at current pace). Technical keys run to S4 (18 items). Not urgent; do it
  at the next Opus call so no queue runs dry. Grammar keys from G27,
  technical from T29, then M1-M4 after T43.

### Fitness: no scale yet
- The learner has no body weight scale and no food scale (2026-10-27). Weigh-ins and weighed meals are not possible yet. Decide the fallback: label and photo only, or a cheap scale now.

### Kaishi: scheduler changed 10-27
- Anki switched to a new RWKV scheduler on 2026-10-27. Due counts: 980 (10-25), 1300 (10-27). Decide whether the 100-due gate for new cards still holds, or if the count needs a new baseline.

## Done

Decided items move to `Decisions.md`.
