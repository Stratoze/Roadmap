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

- [ ] 2026-11-11, key shown before the learner answered (defect). In the
  review-question step I wrote the answer in brackets next to the question
  (G13 Variant, "I eat at 8 o'clock tomorrow", answer あした 八時に たべます).
  Rule: "Show a key only after the learner answers" (AGENTS.md Teaching 10).
  The review is void for today; replaced by the G15 Variant "I go on
  Sunday." Learner's words: "Now you even leaked the answer." Opus to decide
  whether a rule or check is needed to stop a key appearing in a question.

- [ ] 2026-11-11, grammar resource order not deterministic (G19). Learner:
  "It should probably use some sort of deterministic script... the ordering
  clearly states Tofugu, then Cure Dolly, then yoku.bi, then Imabi." AGENTS.md
  "Japanese / Grammar lesson" gives that order. For G19 the steps are: Tofugu
  (cannot be opened, skipped); Cure Dolly (`Prompts/page.sh かった くなかった
  よかった` lists no lesson, so it fails the form check); yoku.bi (lists
  Lesson8.md, "い-adjectives", which holds the forms). Haiku gave the yoku.bi
  link without showing these steps. Opus to decide: a script that runs the
  order and prints the first passing page with its link, and whether the
  Rule line must hold full forms (たかくなかった) or fragments (くなかった).

- [ ] 2026-11-11, grammar procedure gap (G19). Haiku gave the G19 quiz at
  session start without giving the reading link, and never named G19 as the
  page to read at the end of the previous session. AGENTS.md "Japanese /
  Grammar lesson" requires naming the next item and its link at session end.
  Learner's words: "You never gave me the resources for G19... it seems
  clear that a skill/procedure set is needed." Opus to decide: a grammar
  skill (name the next item, give its checked link, log that it was read,
  then quiz next session) or a Haiku step in the session order.

- [ ] 2026-11-11 (T12 session), procedure drift for Opus to analyze. Learner
  finished technical T12 (tutor check passed, Variant missed) and said "Ok
  next". Haiku offered the T12 Variant again, not the Japanese grammar item.
  AGENTS.md "Daily plan" says on the phone, alternate Japanese grammar and
  technical; the one not done last comes next, so Japanese (G19 quiz) was
  due. Haiku only offered it after the learner asked "did you forget about
  the interleaving rule?". Haiku had earlier also re-asked the same Variant
  after a miss and said "I'll ask at next session", then reopened it in the
  same session. Question for Opus: is the next-item rule written clearly
  enough for Haiku at a "next" request (which queue wins when a technical
  item is open but unpassed), and should the Variant retry wait for the
  next session? Learner's correction, verbatim: "Hmm, did you forget about
  the interleaving rule or ?" Quiz given after: G19 Q1 "Say 'It was
  expensive.' (expensive = たかい)" (not yet answered).

## Done

Decided items move to `Decisions.md` (last: 2026-11-11, Opus inbox).
