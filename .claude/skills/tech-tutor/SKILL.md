---
name: tech-tutor
description: Give the learner the next technical item (phone T-item, or laptop milestone A1.1 / M1.1) with its search keywords and ready tutor prompt (printed by Prompts/give.sh), then save the pasted session, check FINAL ANSWER against the key in BACKLOG.md, ask the Variant, and log. Use whenever technical is next, or the learner says "technical", "next item", or pastes a finished tutor chat. Haiku task.
---

# tech-tutor

## Step 1: resource and prompt

1. The item = the next unticked one in the technical queue of `BACKLOG.md`.
2. Run `bash Prompts/give.sh <T-number>` (from the repo root).
3. "MISSING": add one line to `Proposals.md`, give the next task.
4. Otherwise reply with:
   - the SEARCH line as "Optional, YouTube or Google: <keywords>". If the
     item's `Learn:` line has a URL, give it too. Never search for or
     invent other links.
   - everything below the "copy below" line, in one code block,
     character for character. You never write or change a prompt, and
     never show the key.
   - "Paste this into Gemini. When done, write `end` and paste the block
     back here."

## Step 2: what comes back

1. Save the paste verbatim to `Sessions/YYYY-MM-DD-<T-number>.md`.
   Commit and push it.
2. Compare FINAL ANSWER with the key's Answer and Check.
   - A formula that gives the key's number counts as the number.
   - Words: every Check point is there, in any wording. Extra true
     points are fine.
3. Match: ask the key's `Variant:` once, one message, no hints; a
   formula counts. Right: tick the item, write both answers on its
   `Result:` line. Wrong: one line on what is wrong; one Handoff line.
4. No match: one line naming the missing Check point; back to Gemini.
   Do not teach it.
5. Not sure: do not tick; "check for Opus", one line to `Proposals.md`.
6. Log in `Learned/log/technical.md`: date, item, final answer,
   MISCONCEPTIONS and HINTS as written.

## Laptop milestones (A and M)

Next milestone = the first unticked one in `AI/PROJECTS.md` or in
"M1 in simulation" in `Mechatronics/ROADMAP.md` (the learner picks the
track). Step 1 as above with its number (`give.sh A1.1`). When the end
block is pasted: save it to `Sessions/YYYY-MM-DD-<number>.md`, log it in
`Learned/log/technical.md`, and tick the milestone with its EVIDENCE on
the `Result:` line if STATUS is done and the evidence meets "Done when".
No key, no Variant; the learner's evidence stands.
