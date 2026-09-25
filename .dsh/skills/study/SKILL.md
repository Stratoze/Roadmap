---
name: Study
description: Learn, practice, or continue a topic the vault way - verified resources first, orient/predict/attempt/feedback, multi-lens teaching, struggle budget, reflection, spaced review. Use when Kohaku wants a lesson, or says "study", "teach me", "continue <topic>".
---

# Study - the vault learning session

Read first: `_system/How to Learn.md` (the Loop and the rules),
`_system/learning/README.md` (system layout), and `_system/learning/learner.md`
(preferences + standing orders). Use the active topic dossier for its current
source; do not preload resources from a roadmap.

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
4. Check the active concept's `## Resources` dossier. If it is missing, run
   the JIT resources routine (ask for a book/source, then scout/verifier) and
   say that the source step is running. A bare title or inactive roadmap list
   is not an active locator.
5. Milestone topics may retain approved lenses as historical/curriculum
   guidance, but the activated curriculum dossier is the source authority.
6. Technical work routes to `.dsh/skills/technical/SKILL.md`; generic study
   handles concepts that do not need the technical session sequence.
7. Show what is due today (`python3 scripts/review.py due`) before starting new
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

Default modality: the active concept's cited locator first. Ask for or verify
one source JIT when needed, read it, then take the learner's questions and
probe. A faithful translation/restatement into Japanese may add no new claims;
an explanation beyond the source is a documented blocker. Wrong premises are
named and dislodged, never papered over. Zero-schema concepts: orientation
before any question.

- **Source**: open the concept's active locator from `## Resources` (`for <concept id>`).
  - If no active locator exists, ask for a book/source and run the resources
    scout/verifier routine. Do not lecture from memory.
  - A learner-supplied book is valid when its edition and locator are recorded.
  - Videos/interactives are verified substitutes or supplements, selected at
    activation rather than stockpiled.

- **Motivate**: why this now, tied to their goal. One or two sentences.
- **Predict**: "I expect ___ because ___" - their words.
- **Attempt**: they try. 15 minutes of solo struggle with attempts logged
  before any scaffold. Zero-schema exception: orientation first (video, worked
  example, demo), then predict.
  - `hint_budget` = 2: after two scaffolds, switch strategy (worked example,
    lateral move) instead of adding hints.
  - **AI unblocks only on a block**: if the source genuinely does not cover the
    blocker, answer it, then log `- blocker <YYYY-MM-DD> <concept id>: "<what
    the source missed>"` under `## Resources` and refill or mark
    `no source found`. Never a blocker just because the source is longer than
    reading it would take.
- **Compare**: for anything computable, compute the answer key by execution -
  never by inspection. State what they got and the gap.
- **Feedback**: immediate - what is right, what the gap is, why. Collect
  confidence BEFORE feedback with the question tool (bands: under 50, ~70,
  ~90, certain); it goes to the private receipts.
- **Establish**: Socratic where they can reason it; motivated exposition
  otherwise. Multi-lens: intuitive first, then rigorous. The rigorous lens
  must be sourced (dossier or verifier) - never stated from memory if unsure.
  Name the locator used.
- **Connect**: link to the prereqs, to the theory it rests on (see the
  topic-tree link map), and to the goal. Links are the point. State the
  mechanism for each link ("why does this follow?"); label conventions as
  conventions; never manufacture a link.
- **Name it** (standing order 8): state the canonical term alongside the
  simple-words version ("the standard word for this is ___"); the learner
  produces the term once from memory before moving on. Term misses get a
  one-line in-flow correction plus a dated line in the topic file
  (`## Misconceptions` or `## Log`), so reviews can re-probe them.
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
- No probe before the locator (learner standing order, 2026-09-25): every
  study attempt names its cited section first (book ch/§, or the labeled
  substitute); a missing citation runs the sourcing routine — never a lecture,
  never a cold probe on unsourced ground.
- No AI exposition of ground a cited source covers - source first; a source
  that fails is logged as a `blocker`, not quietly replaced by a lecture.
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

## Session log (AGENTS.md; agent drafts, learner owns)

- **No pre-work gate.** Start with the lesson - never ask for Targets or
  Predictions up front.
- **Close**: draft `Daily/YYYY-MM-DD.md` (template `_templates/daily.md`) from
  evidence - worked-on threads, Got, Gap (proposals; the learner's correction
  owns them), one next step, evidence links. Got vague or faulty -> say so and
  ask once, then drop till tomorrow. Agent activity goes to `Changelog/`,
  never the Daily.

## Close

- One next step (concept or review date), named by category + content + link
  (e.g. "vectors & frames - math; feeds kinematics"), never a bare vault id.
  No recap wall.
- Offer the stale commitment cue once (verbatim, never rewritten) in
  `learner.md`; if renewed, store their new words verbatim with a new date.
- Claims (MVM / Full Pass) go to **assessor** before anything is recorded as
  earned. Graded-path rule (learner standing order, 2026-09-25): every
  milestone/project DONE names its ≥1 NEW transferable skill at intake; a claim
  teaching nothing new routes to the example pool, never the graded path.
