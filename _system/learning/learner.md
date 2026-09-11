# Learner - Kohaku

Canonical learner state for the vault learning system. Engram is being retired
(see `.opencode/plan/vault-learning-system.md`); this file replaces its learner
model. Mirrors: OpenViking
`viking://user/default/memories/preferences/user/learning-preferences.md`
(session-start visibility) and a thin pointer in `~/.config/opencode/AGENTS.md`.
Preferences are the learner's own; the system stores no AI inference about the
learner without their words.

## Preferences

- **Interests:** Japanese immersion; mechatronics / robotics builds; philosophy;
  piano; game design; anime piano covers; classical piano repertoire.
- **Multi-lens teaching:** every concept gets an intuitive lens and a rigorous
  lens - `strategy_weights` derivation_first 0.5 / example_first 0.5 (set
  2026-09-03; evidence: learner standing order "teach every concept in multiple
  lenses, intuitive plus rigorous").
- **Challenge band:** `target_success` 0.85 (escalate when checks run above it,
  shrink when far below); `hint_budget` 2 (after two scaffolds, switch strategy
  instead of adding hints).
- **Defaults:** standard session mode; artifacts threshold-only; momentum notes
  on.
- **Sourcing:** established human educators first; never AI-generated videos;
  verify claims before stating them; cite non-trivial claims.

## Standing orders

1. **Multi-lens.** See Preferences.
2. **Verbatim productions.** Raw learner words are quoted unaltered in private
   records; public notes carry summaries and links.
3. **Compressed verifies.** When a prediction already evidences the concept,
   verify with one compressed question - never a full re-ask.
4. **Rigorous means rigorous.** Verify against sources/reflection before
   stating; flag uncertainty explicitly when a check isn't possible.
5. **Video-first modality.** Video (plus an explorable where one exists) ->
   learner questions -> verification probes. Minimal chat tutoring.
6. **No yes-man.** Push back when a better approach exists.
7. **Cold-recall-first reviews.** Probe before any re-exposure; feedback after
   retrieval, never before.

## Commitment cue (verbatim, 2026-08-21)

- Cue: "lunch or the afternoon tomorrow"
- Action: "clear the engram reviews"
- Status: **stale** (names engram). Offer once in the new close ritual; if
  renewed, store the learner's new words verbatim with a new date.
