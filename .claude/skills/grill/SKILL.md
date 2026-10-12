---
name: grill
description: Grill the learner on coursework or a project until they can answer the likely teacher questions. Sonnet task. Use when WEEK.md lists a grill or the learner asks to be quizzed on a project.
---

# grill

Model: Sonnet. If you are Haiku, say "This is a Sonnet task. Run `/model sonnet`." and stop.

1. Read `Learned/coursework.md` and the questions or keys in `WEEK.md`. Read the project files you ask about; never quote a number you have not read in a file.
2. One question per message. Wait.
3. Ask for a concrete output, not a rule ("what is printed?", "what number?").
4. Judge the answer:
   - Right with the right reason → say "Right." and the next question.
   - Right conclusion, weak reason → name the missing reason in one line, then a variation.
   - Wrong → the correct answer in one or two lines, then a variation of the same question later.
   - Hedge ("probably", "either") → "Pick one."
5. Never ask the exact same question twice. Never answer for the learner.
6. At the end, update `Learned/coursework.md`: can explain / shaky / not earned, with dates.
