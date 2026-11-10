---
name: tech-tutor
description: Point the learner to the technical tutor prompt and exercise in Prompts.md, then check the pasted FINAL ANSWER against the key in BACKLOG.md, ask the Variant, and log. Use whenever technical is next, or the learner says "technical", "next item", or pastes a finished tutor chat. Haiku task.
---

# tech-tutor

## Step 1: point to the prompt

Say only: "Technical: copy the tutor prompt and exercise <T-number> from
`Prompts.md` into Gemini." <T-number> = the next unticked item in the
technical queue of `BACKLOG.md`. Never print, write or change a prompt,
and never show the key. If the exercise is missing from `Prompts.md`,
add one line to `Proposals.md` and give the next task.

## Step 2: check and log

1. Compare FINAL ANSWER with the key's Answer and Check.
   - A formula or expression that gives the key's number counts as the
     number. Units: if the formula's quantities carry them, that is enough.
   - Words: every Check point is there, in any wording. Extra true points
     are fine.
2. Match: ask the key's `Variant:` once, one message, no hints. A formula
   counts here too. Right: tick the item in `BACKLOG.md`, write both
   answers on its `Result:` line. Wrong: one line on what is wrong; one
   Handoff line; it comes back next session.
3. No match: one line naming the missing Check point; the learner goes
   back to Gemini. Do not teach it.
4. Not sure: do not tick; log "check for Opus", one line to
   `Proposals.md`, give the next task.
5. Log in `Learned/log/technical.md`: date, item, final answer, HINTS.
