---
name: grammar
description: Run the Japanese grammar steps for the learner's Roadmap: the quiz on the page read last session, scoring and logging it, and giving the next page to read. Use whenever grammar is next, the learner says "grammar", "quiz", "next page", or the session is ending (the next page must be given before it ends). Haiku task.
---

# grammar

Two parts, in two sessions: read a page at the end of one session, take
its quiz at the start of the next. Every question and page comes from
`Prompts/give.sh`; you never type a question, answer or link yourself.

## Start of session: quiz

1. The item = the first unticked G-item in `BACKLOG.md` whose page the
   Handoff or log says was given. No page was given → skip to "End of
   session" now: give the page, no quiz today.
2. Run `bash Prompts/give.sh quiz <G>`. Ask its lines in order, one per
   message, copied exactly. No answer choices, no hints, no answer in
   brackets.
3. After each answer: say right or wrong in one line, with the right
   form if wrong. Score by `AGENTS.md` "Japanese / Scoring".
4. After the last: write the `Result:` line (date, score, slips), tick on
   a pass, update `Learned/japanese.md`, commit, push.
   Fail → no new page today; the same quiz next session.

## Review question

Run `bash Prompts/give.sh variant <G>` and ask its line exactly. Show the
key only after the answer.

## End of session: next page

1. The next item = the first unticked G-item after the one just passed
   (or the failed one again, if its page was never given).
2. Run `bash Prompts/give.sh page <G>`. Give its line exactly:
   "Read this before next session: <line>".
3. "MISSING" → add "Page needed: <G>" to `Proposals.md` and say so. Do
   not search for a page yourself.
4. One line under Handoff in `BACKLOG.md`: "Page for <G> given <date>."
   Commit, push.
