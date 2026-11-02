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

- 2026-11-02, Opus audit (learner asked: teaching, neuroscience, engineering,
  AI-management lenses). One item: the learner picks which fixes to adopt.
  Evidence: technical 0 items since 10-23; Japanese floor confirmed met on
  3 of 17 noted days since 10-14 (most say "not reported"); 66 of 158
  commits since 10-01 changed rules, skills or decisions.
  1. Retrieval: a ticked item never comes back (Teaching rule 3). Each
     session opens with one question from an item passed a week or more
     ago; every key gets a `Variant:` question for it.
  2. Delayed quiz: read the grammar page this session, take its quiz at
     the start of the next (tests memory, not the page just read).
  3. Tutor honesty: after a tutor pass, Haiku asks the key's `Variant:`
     question itself; the tutor's own summary is the only proof now.
  4. Hardware now: buy Arduino Uno, two 10 kΩ potentiometers, breadboard,
     jumpers, multimeter; build a crude cardboard arm early and let the
     theory items serve the build.
  5. Scope: at ~1 item per 4 days, the ~54 listed items end around June
     2027, beside JLPT. Park items the passive arm doesn't need (T25 FEM,
     T45-T50 power/thermal, T53-T58 materials). Give the capstone a pass
     line (tip within ±1 cm of the FK prediction).
  6. Kaishi: no new words since 10-08, due rising (~1500). Count reviews
     per day, not minutes, and set a date for new cards (N4 ≈ 1500 words).
  7. Chat NEW WORDS are logged and never seen again: into Anki, or stop
     logging them.
  8. Missing minutes: the first question each session is the last
     session's minutes, if not reported.
  9. One fixed cue: a set time and place for the session, the learner's
     choice.
  10. Rule budget: a new rule replaces an old one; rule changes only on
      Opus days.
  11. Network: allow khanacademy.org, tofugu.com, openstax.org in the
      environment so lesson pages are opened, not judged from search
      snippets.

## Done

Decided items move to `Decisions.md` (last: 2026-11-02, system check).
