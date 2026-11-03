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

- 2026-11-03 (Haiku, session, process gap): Haiku wrote its own chat prompt and told the learner no master prompt existed. Cause: the `jp-chat` text loaded in this session had no Step 1 template; `.claude/skills/jp-chat/SKILL.md` on disk has it. Haiku did not open the file before handing over the prompt. Fix needed: Opus confirms the loaded skill text matches the file, and Haiku reads the file on disk before any prompt. Learner was given the real template at 11-03.

## Done

Decided items move to `Decisions.md` (last: 2026-11-02, system check).
