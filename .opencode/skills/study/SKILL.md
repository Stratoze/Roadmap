---
name: Study
description: Learn, practice, or continue a topic the vault way - verified resources first, orient/predict/attempt/feedback, multi-lens teaching, struggle budget, reflection, spaced review. Use when Kohaku wants a lesson, or says "study", "teach me", "continue <topic>".
slash: false
---

# Study - the vault learning session

Read first: `_system/How to Learn.md` (the Loop and the rules),
`_system/learning/README.md` (system layout), `_system/learning/learner.md`
(preferences + standing orders). The plan of record is
`.opencode/plan/vault-learning-system.md`.

## Session start

1. Topic = the learner's words, or the topic file in
   `_system/learning/curriculum/`. If neither: derive the next action yourself -
   due reviews first, then intake for pre-system milestones, else the next
   unchecked milestone (map, then study). Never ask the learner to choose.
2. NEW topic: create `_system/learning/curriculum/<topic>.md` from the
   skeleton in the plan (Appendix A). Ask the scoping question (what do you
   want to be able to DO with this, by when?) and store the answer verbatim in
   `## Goal`. Spawn **scout** for a goal-bounded field scan; prune with the
   learner; write the pruned one-claim aims as `unknown` rows in `## Concepts`.
   New topic with plausible priors (school, work, an earlier milestone): offer
   `map` first - scoping question + bracket - then teach from the floor; the
   comfort branch probes as you go, and mapping never blocks.
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

## Intake (pre-system topics)

Knowledge that predates the system (completed milestones with boxes already
checked, migrated tracks): rows come from the milestone's checked pass
conditions; skip scoping and scout. Per concept, one compressed cold verify -
no priming, confidence picked before feedback. Clean pass ->
`review.py schedule <topic> <id> 2`; effortful pass -> rung 1; miss -> run the
normal loop (teach from the scaffold), then schedule at rung 0. Never re-teach
a passing verify (standing order 3); evidence gets the probe date. Cap 6
verifies per sitting; continue only if asked.

## The loop (per concept)

Default modality (standing orders 5-6): video/explorable first (from the
dossier), then the learner's questions, then probing - minimal chat tutoring;
wrong premises are named and dislodged, never papered over. Zero-schema
concepts: orientation before any question.

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
- **Connect**: link to the prereqs, to the theory it rests on (see the
  topic-tree link map), and to the goal. Links are the point. State the
  mechanism for each link ("why does this follow?"); label conventions as
  conventions; never manufacture a link.
- **Check**: ONE compressed verify (standing order 3) - quiz via the question
  tool where gradable (construction: `_system/learning/quiz-protocol.md`),
  free recall otherwise. No quiz before schema.
- **Record**: update the concept row; schedule with
  `python3 scripts/review.py schedule <topic> <id>`. First contact sets rung 0
  and state `review`. Confidence goes to `_private/learning/receipts/`. Add or
  update the problem row and write the links both ways (lesson <-> topic <->
  theory <-> problems; theory files get an `Applied in:` line).

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
(summary) / Confidence (recorded privately; note the path) / Links / Next.
`## Links` names: the topic, the theory it rested on, the problem ids, and the
previous lesson. Raw text goes to
`_private/learning/verbatim/<YYYY-MM-DD>-<topic>.md`.

## Close

- One next step (concept or review date), named by category + content + link
  (e.g. "vectors & frames - math; feeds kinematics"), never a bare vault id.
  No recap wall.
- Offer the stale commitment cue once (verbatim, never rewritten) in
  `learner.md`; if renewed, store their new words verbatim with a new date and
  update the OpenViking mirror.
- Claims (MVM / Full Pass) go to **assessor** before anything is recorded as
  earned.
