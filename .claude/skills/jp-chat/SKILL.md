---
name: jp-chat
description: Set up and log the learner's daily Japanese written chat (about 25 minutes, at least 5 replies, using only grammar already taught). The chat itself runs in a free chat service outside Claude Code; you hand over the prompt and log what comes back. Use this whenever WEEK.md lists a Japanese chat, the learner asks to "chat in Japanese" or "practice Japanese", pastes a finished chat, or sends a Japanese sentence to check.
---

# jp-chat

The learner is a complete beginner. The chat exists so they produce real
Japanese every day with the grammar they have, and learn what a native would
actually say.

The chat does not run here (changed 2026-10-14). Running it on Sonnet cost
enough that the learner wanted to skip it, and Haiku miscorrected a correct
sentence. So the learner chats in a free chat service, and your job is the
two mechanical ends: hand over the prompt, then log the result. Do not chat
in Japanese yourself.

## Step 1: hand over the prompt

1. Read the ticked grammar in `NEXT.md` and today's opening line in `WEEK.md`.
2. Print the template below in one code block, with the two `{...}` slots
   filled in. Change nothing else in it.
3. Say: "Paste this into your free chat service. Chat about 25 minutes by
   your own clock (5 replies is enough on Mon, Thu or a tight day). Write
   `end`, then paste the whole chat back here."

```
You are my Japanese conversation partner. I am a complete beginner.

1. Write ONE short Japanese line per message, in hiragana/katakana with
   spaces between words. No kanji except 日本, 本, numbers and 時. Then wait.
2. Use only this grammar, with simple everyday words: {ticked grammar points}
3. After each reply of mine:
   - correct and natural: write only your next line. No praise.
   - wrong or unnatural: first one line in English, in this form:
     my line → fixed line. One sentence on what the particle or form marks.
     Then your next line.
4. Before correcting, check that my sentence is really wrong. Short answers
   (うちです) are correct. If my sentence is correct but an odd answer to your
   question, say that; do not rewrite it.
5. If I write a particle by its sound (わ for は, お for を, え for へ), fix it.
6. If a fix needs grammar outside the list, write "(not taught yet)" and give
   only the fix, no lesson.
7. Explain in English by what the particle marks, not by translating it.
8. If you mention an object, say where it is (near you, near me, far away)
   so that これ / それ / あれ make sense.
9. Change the topic every few lines: food, school, family, things in the
   room, yesterday, tomorrow. Keep the grammar inside the list.
10. When I write "end", list every correction you made, one per line, in the
    same form as rule 3, and nothing else.

Start now with this line: {opening line from WEEK.md}
```

## Step 2: log the pasted chat

1. Count the learner's Japanese replies by listing them, numbered. Report
   that number; do not estimate it. Minutes are whatever the learner reports.
2. Copy each correction from the chat's final list into "Chat practice" in
   `Learned/japanese.md`, one line each, with the date and "(external chat)".
   Copy them as written. Do not add corrections of your own.
3. If a correction looks wrong to you, do not overrule it. Add the line with
   "check on Sunday" so Opus looks at it in the weekly audit.
4. Tick the chat in `WEEK.md` with the reply count.

The pasted chat is the learner's raw production: do not commit it anywhere
in the repo (the repo is public). The learner's chat service keeps the
history; on Sunday they paste one chat to Opus for the audit.

## If the learner sends one Japanese sentence to check

Answer directly, in this form:

`<their line> → <fixed line>. <what the particle/form marks, one sentence>.`

- `がっこうに たべます → がっこうで たべます. で marks where the action happens; に marks a point you go to.`
- `ほんを あります → ほんが あります. With あります the thing that exists takes が; を marks something an action is done to.`

Check first that the sentence is really wrong; changing a correct sentence
teaches a false rule. If you are not sure, say "not sure, ask in the chat or
on Sunday" instead of guessing.
