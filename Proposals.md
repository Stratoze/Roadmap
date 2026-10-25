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
   Last audit: 2026-10-25 (Opus).
4. If **Open** has any item, tell the learner once at session start:
   "Opus inbox: N open (top: <first item>)." Do not push further.

## Open

### Refill: chat openers and grammar keys
- Chat openers: 10 left. Grammar keys: G12b-G26 (15 items, ~5-8 sessions
  at current pace). Technical keys run to S4 (18 items). Not urgent; do it
  at the next Opus call so no queue runs dry. Grammar keys from G27,
  technical from T29, then M1-M4 after T43.

## Done

Decided items move to `Decisions.md`.
