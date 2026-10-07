# Quiz protocol - constructing graded probes

For any probe with a right answer: map rungs, study checks, review recall.
Open conversation is for vague rungs and reasoning that cannot be option-set;
this file covers the graded ones. Construction adapted from Amos Blomqvist's
learn (quiz construction procedure); the vault's grading rules appended.

## Which modality

- **Open** - vague rungs, mechanism/reasoning questions, anything without
  honest options. Grade against a key you computed.
- **Quiz** (question tool with options) - items with a right answer where the
  distractors can carry real confusions, in map rungs and in checks. One
  question per call.
- Never quiz before schema (study ban); never re-expose before a recall probe
  (review ban).

## Construction - the four rules

1. **Every option is a bare claim.** No justification in any option; all "why"
   goes into the feedback after the pick. (The tell is the correct option
   carrying its own reasoning while the distractors stay bare.)
2. **Write the correct claim first, then mutate it into each distractor** -
   same skeleton, grain size, and register. Each distractor is what a specific
   misconception would claim: unambiguous to a knower, tempting to its holder.
3. **No asymmetric bolding or formatting.** Either none, or the parallel term
   in every option.
4. **Cold-read check:** if you can tell the answer without knowing the
   material, regenerate the set - don't patch it. The correct option must not
   be the longest or most qualified; distractors must not be throwaways.

## Grading (vault rules)

- Answer keys for computable items are computed by execution, never by
  inspection.
- Confidence is collected BEFORE feedback (question tool bands: under 50 / ~70
  / ~90 / certain); receipts to `_private/learning/receipts/`.
- Feedback: the correct answer + the exact gap. On a miss, characterize
  (slip / gap / misconception) before concluding.

## Fit with the search

One question per message; the next question is chosen from the answer
(binary search: hit -> jump up; miss -> narrow in). This file governs how the
graded ones are built, not how the search runs.
