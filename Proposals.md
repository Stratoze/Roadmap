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

- 2026-11-02, from the learner (G15 quiz Q2): the prompt "Ask What day is it today?" is ambiguous in English (date, 何日, or weekday, なんようび). Learner typed 今日は何日ですか and objects that it counts as wrong. Key counts なんようび (the Rule says "what day" is なんようび). Opus to rule: reword the prompt, or accept 何日, and whether the score stands.

- 2026-11-02, from the external chat: "あさは私がたべません → 朝は食べません". The question was 朝何を食べましたか (past), so the fix keeps the present tense (ません, not ませんでした). The chat also explains が as "focus on the subject", which is not in the taught list (4 は vs が). Check the tense and the explanation.
- 2026-11-02, from the external chat: "あしたは土曜日 → 明日は土曜日です". The fix uses です, which is not on the taught list and has no "(not taught yet)" tag. Check whether the fix is needed and whether です is taught.
- 2026-11-02, from the learner: the repo has no rule for learning mechatronics from videos or web pages. AGENTS.md names Japanese sources only (Tofugu, Cure Dolly, yoku.bi, Imabi). Opus to decide: which sources (videos, pages) are allowed for statics and circuits, and whether they teach the idea before the hand exercise or only support it.

## Done

Decided items move to `Decisions.md` (last: 2026-11-01).
