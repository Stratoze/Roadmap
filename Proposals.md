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
   - The learner says Haiku accepted a wrong answer → "Move <task type> to
     Sonnet?"
4. At session start, if **Open** has any item, say once:
   - "Call Opus now: <item>." when an item blocks today's work (the next
     queue item has no key, a wrong answer was accepted), or **Open** has 3
     or more items.
   - Otherwise: "Opus inbox: N open (top: <first item>)."
   Say it once per session; then carry on with the work.

## Open

- 2026-11-11, learner request (sequencing rule, for `AGENTS.md` "Daily plan"): on the phone, interleave Japanese grammar and technical unless asked otherwise (last one done → the other next). On the PC: if no Japanese or technical done today, do 1 of each first, then Python (laptop milestones), unless asked otherwise. Opus: write it into AGENTS.md.
- 2026-11-11, learner proposal (source order for grammar pages, `AGENTS.md` "Japanese"): search in this order, Tofugu, then Cure Dolly (https://kellenok.github.io/cure-script/), then yoku.bi, then Imabi; first page that covers the item wins. Applied from 2026-11-11 unless Opus overrules.
- 2026-11-11, check for Opus: G18 key. Q4 "It is not good." is vague (わるくないです is also natural; key accepts only よくない). Q2 and the rest fine. Decide the score and fix the key's wording. Also: Tofugu page for G18 covers くない but not くなかった; check the past form before the redo, and say which page covers it. Recurring problem (learner, 11-11): vague questions and unchecked pages. Opus: write a rule for when Haiku must send a key to Opus instead of scoring it.

## Done

Decided items move to `Decisions.md` (last: 2026-11-02, system check).
