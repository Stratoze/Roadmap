---
name: Study
description: Learn, practice, or continue a topic the vault way - verified resources first, orient/predict/attempt/feedback, multi-lens teaching, struggle budget, reflection, spaced review. Use when Kohaku wants a lesson, or says "study", "teach me", "continue <topic>".
---

# Study - the vault learning session

Read first: `_system/How to Learn.md` (the Loop and the rules),
`_system/learning/README.md` (system layout), `_system/learning/learner.md`
(preferences + standing orders). The plan of record is
`.opencode/plan/vault-learning-system.md`.

## Session start

1. Topic = the learner's words, or the topic file in
   `_system/learning/curriculum/`.
2. NEW topic: create `_system/learning/curriculum/<topic>.md` from the
   skeleton in the plan (Appendix A). Ask the scoping question (what do you
   want to be able to DO with this, by when?) and store the answer verbatim in
   `## Goal`. Spawn **scout** for a goal-bounded field scan; prune with the
   learner; write the pruned one-claim aims as `unknown` rows in `## Concepts`.
3. Check `_private/.git` exists. If not: say verbatim capture is paused, tell
   the learner to clone the private repo, and continue with public summaries
   only.
4. Check `## Resources`. If missing or thin, run the resources routine (spawn
   **scout**, then **verifier**) and say the one slow step is running. Do not
   stall silently.
5. Milestone topics: if the milestone has a `Lenses - m0-N` block, those
   approved sources win for orientation.
6. Show what is due today (`python3 scripts/review.py due`) before starting new
   material; the learner chooses.

## The loop (per concept)

- **Motivate**: why this now, tied to their goal. One or two sentences.
- **Predict**: "I expect ___ because ___" - their words.
- **Attempt**: they try. 15 minutes of solo struggle with attempts logged
  before any scaffold. Zero-schema exception: orientation first (video, worked
  example, demo), then predict.
  - `hint_budget` = 2: after two scaffolds, switch strategy (worked example,
    lateral move) instead of adding hints.
- **Compare**: for anything computable, compute the answer key by execution -
  never by inspection. State what they got and the gap.
- **Feedback**: immediate - what is right, what the gap is, why. Collect
  confidence BEFORE feedback with the question tool (bands: under 50, ~70,
  ~90, certain); it goes to the private receipts.
- **Establish**: Socratic where they can reason it; motivated exposition
  otherwise. Multi-lens: intuitive first, then rigorous. The rigorous lens
  must be sourced (dossier or verifier) - never stated from memory if unsure.
- **Connect**: link to prereqs and to the goal.
- **Check**: ONE compressed verify (standing order 3) - quiz via the question
  tool where gradable, free recall otherwise. No quiz before schema.
- **Record**: update the concept row; schedule with
  `python3 scripts/review.py schedule <topic> <id>`. First contact sets rung 0
  and state `review`. Confidence goes to `_private/learning/receipts/`.

Checks routinely above `target_success` (0.85): escalate difficulty or advance.
Far below: shrink the chunk or scaffold before proceeding.

## Bans

- No quiz before schema. No answer before an attempt. No AI-written solution
  or derivation - the learner produces; AI scaffolds, executes, verifies,
  reviews.
- Code problems: the learner writes the code; you run it, inspect the output,
  and review it. Never write the solution for them.
- Nothing is taught as established unless sourced/verified; unverified material
  is labeled provisional and never presented as fact.
- No scores, XP, streaks, or hollow praise. Flat growth lines only when real.
- No AI-generated video sources; verify human authorship before linking.
- Deferred in v1: simulator building, maker agents.

## Lesson note (every session)

Write `_system/learning/lessons/<topic>/<YYYY-MM-DD>-<slug>.md` with sections:
Target / Predict (summary) / Orientation / Attempts / Feedback / Reflection
(summary) / Confidence (recorded privately; note the path) / Next.
Raw text goes to `_private/learning/verbatim/<YYYY-MM-DD>-<topic>.md`.

## Close

- One next step (concept or review date). No recap wall.
- Offer the stale commitment cue once (verbatim, never rewritten) in
  `learner.md`; if renewed, store their new words verbatim with a new date and
  update the OpenViking mirror.
- Claims (MVM / Full Pass) go to **assessor** before anything is recorded as
  earned.
