---
name: jp-chat
description: Give the learner the Japanese chat prompt (printed by Prompts/give.sh) and save and log what they paste back. Use whenever chat is next, the learner asks to "chat in Japanese" or "practice Japanese", or pastes a finished chat.
---

# jp-chat

The chat is for fun and real use, not a test. It runs in Gemini.

## Step 1: give the prompt

1. Run `bash Prompts/give.sh chat` (from the repo root).
2. Put its output in your reply, in one code block, character for
   character. Nothing added, nothing removed. You never write a prompt.
3. Then one line: "Paste this into Gemini. When done, write `end` and
   paste the block back here."

## Step 2: what comes back

1. Save the paste verbatim to `Sessions/YYYY-MM-DD-chat.md` (add `-2`
   if it exists). Commit and push it.
2. Copy CORRECTIONS into "Chat practice" in `Learned/log/japanese.md`,
   as written, dated, "(external chat)". NEW WORDS into "Vocabulary".
3. A slip that repeats a weak spot or shows a new one: update "Weak
   spots" in `Learned/japanese.md`.
4. A correction that looks wrong: log it with "check for Opus" and add
   one line to `Proposals.md`.

No reply count, no minutes, no questions about the chat.
