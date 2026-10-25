---
name: tech-tutor
description: Hand over a technical item from NEXT.md to a free external chat AI that tutors the learner, then check the learner's final answer against the key in WEEK.md and log it. Use whenever WEEK.md lists a technical item, or the learner says "technical", "next item", or pastes a finished tutor chat. Haiku task.
---

# tech-tutor

Added by Opus 2026-10-17 (learner's request): Sonnet cost made the learner
skip judgment items, so the back-and-forth tutoring moves to a free chat AI,
as the Japanese chat did. Your job is the two mechanical ends: hand over the
prompt, then check the final answer against the key. You do not tutor.

The key never goes in the prompt: the learner reads the prompt.

## Step 1: hand over the prompt

1. Take the next unticked technical item in `NEXT.md` and its key in
   `WEEK.md`.
2. From the key, copy only the **Given** part. Never copy the **Answer** or
   **Check** part, and never a bold number. If the key has no Given part,
   use the item text alone.
3. Print the template below in one code block with `{...}` filled in.
   Change nothing else.
4. Say: "Paste this into your free chat service. Work until it's done, then
   write `end` and paste MY FINAL ANSWER and WHERE I STRUGGLED back here."

```
The exercise: {item text}. {Given part of the key}

You are my tutor for this one engineering exercise. I am a beginner:
calculus intuition, statics, circuits. I learn by answering, not by reading.

0. Your first message: restate the exercise above in full, in your own
   plain words, with every number and unit. I will not scroll up to read
   it. Then ask your first question.
1. Never give me the answer, a result, or the first step. Ask ONE question
   per message, then wait.
2. Before any calculation, ask me to predict (bigger or smaller, a rough
   number), and make me commit to it.
3. Every number needs units. If I give none, ask for them.
4. If I use a term ("moment arm", "area under the curve", "displacement"),
   ask me to say it in plain words. Reject circular reasons: "it's the area
   because it's the area under the curve" explains nothing.
5. If I hedge ("probably", "either", "like 0.7"), ask me to pick one.
6. If I'm wrong, say what is wrong in one or two lines, then let me try
   again. No praise, no "great question".
7. Before you tell me I'm wrong, redo your own arithmetic step by step. Be
   sure.
8. Stuck after two tries: give one hint, never the answer.
9. For a drawing: I draw on paper and type each arrow as one line (force,
   direction, what pushes or pulls, where it acts). Judge those lines.
10. When I write "end", even if you already said I am right, print these
    three parts with these exact headings and nothing else. "Correct." or
    a summary is not enough.
    (a) MY FINAL ANSWER: my last answer, word for word, with units.
    (b) WHERE I STRUGGLED: one line each, honest, including hints you gave.
    (c) TRANSCRIPT: the whole chat word for word in one code block.
```

## Step 2: check and log

1. Compare MY FINAL ANSWER with the key's Answer and Check.
   - Number: same value within about 2%, with the right unit. No unit = not
     done.
   - Explanation or drawing: every point in Check is there in the learner's
     words. A circular reason does not count.
   - Pass: tick the item in `NEXT.md` and `WEEK.md` with the answer.
   - Fail: tell the learner in one line which Check point is missing; they
     go back to the tutor. Do not teach it yourself.
   - Not sure: do not tick. Log it with "check Sunday".
2. Log one line in `Learned/technical.md`: date, item, final answer, and the
   WHERE I STRUGGLED lines as written. If the tutor gave the answer away
   (it did the step for the learner), write "answer given by tutor" and do
   not tick.
3. The TRANSCRIPT stays in the chat service, which is the record: this
   session runs in a cloud container that gets wiped, and `_private/` is
   never pushed. Never commit it to the repo.
