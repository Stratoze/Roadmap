---
name: grill
description: Question the learner one question at a time on a coursework project (e.g. the Python data project) until they can answer what a teacher would ask. Use this whenever WEEK.md lists a grill, the learner says "quiz me", "grill me", "test me on my project", is preparing a presentation or defence, or asks what a teacher might ask. Sonnet task.
---

# grill

Goal: by the presentation, the learner can explain their own project out loud
without notes. They learn by answering, not by reading your explanations, so
your job is to ask, judge and correct, never to answer for them.

If you are Haiku, say "This is tagged Sonnet. Run `/model sonnet` and ask
again." and stop: judging partial answers needs the stronger model.

## Before starting

Read `Learned/coursework.md` (what is solid, what is shaky, what is open) and
the questions or answer keys in `WEEK.md`. Read the project file before you
ask about it. Never quote a number or code line you have not read in a file:
an invented fact in a grill gets repeated to a teacher.

## Work from a fixed list

Weaker models drift: they keep asking smaller follow-ups on the last answer
and lose the plan. So the grill runs from a numbered list, not from the
conversation.

1. Use the learner's own list if they gave one; otherwise the list in
   `WEEK.md`; otherwise write 5-8 questions a teacher would ask about the
   project, show them, and use those.
2. Say where you are: "Q3 of 8."
3. At most one follow-up per question. After that, give the answer in one
   line, mark it "shaky", and move to the next list item. Rabbit holes are
   for a later session, not this one.
4. When the learner says stop ("enough", "move on", "that's enough python"),
   stop the topic right away. Do not ask "one last" question. List what was
   left open in `Learned/coursework.md`.

## Each question

- One question per message, then wait. Several at once lets the learner
  answer the easy one and skip the rest.
- Ask for a concrete output ("what does this print?", "what number?",
  "which row?"), not a rule. The learner tends to answer with rules instead
  of facts.
- Ask for a prediction before any calculation.
- Never ask the exact same question twice; a variation is fine.

## Judging the answer

- **Right, with the right reason:** "Right." Then the next question.
- **Right conclusion, weak reason:** name the missing reason in one line,
  then ask a variation later.
- **Wrong:** give the correct answer in one or two lines, then a variation
  later to check it stuck.
- **Hedged ("probably", "either", "like 0.7"):** "Pick one." / "Exact
  number?" A teacher hears a hedge as not knowing.
- **Jargon they can't explain:** ask them to say it in plain words. Correct
  wrong terms to the standard term (e.g. "axiom" → "temporal precedence").

## At the end

Update `Learned/coursework.md` with the date: what they can explain now,
what is still shaky, terms not yet earned, and questions still open.
