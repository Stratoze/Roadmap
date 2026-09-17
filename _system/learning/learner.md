# Learner - Kohaku

Canonical learner state for the vault learning system. This file replaced the
previous learner model (see `.opencode/plan/vault-learning-system.md`). Mirrors: OpenViking
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
  verify claims before stating them; cite non-trivial claims. See standing
  order 8.
- **Standing order 8, source-first (set 2026-09-15, learner's direction "books
  and videos for each lesson and phase instead of relying on AI"):** every
  concept carries a section-precise citation; the lesson starts there. AI
  exposition only on a documented `blocker`.

## Standing orders

1. **Multi-lens.** See Preferences.
2. **Verbatim productions.** Raw learner words are quoted unaltered in private
   records; public notes carry summaries and links.
3. **Compressed verifies.** When a prediction already evidences the concept,
   verify with one compressed question - never a full re-ask.
4. **Rigorous means rigorous.** Verify against sources/reflection before
   stating; flag uncertainty explicitly when a check isn't possible.
5. **Read-first modality.** The cited book section first (plus an explorable
   where one exists), then learner questions, then verification probes. Video
   only where no book covers the concept. Minimal chat tutoring.
6. **No yes-man.** Push back when a better approach exists.
7. **Cold-recall-first reviews.** Probe before any re-exposure; feedback after
   retrieval, never before.
8. **Source-first, AI second** (2026-09-15, learner's direction). The lesson
   starts at its cited source; AI is for what the source cannot answer and for
   testing. AI exposition requires a logged `blocker`; a missing citation is a
   sourcing gap, never a reason to lecture.
9. **Books over videos** (2026-09-15, learner's words: "books are more vital,
   with the correct topic I can search the video myself, but it's hard to find
   the correct high quality books"). The dossier's job is to name the right
   book at the right level. A concept gets a video or interactive only as a
   substitute when no book covers it, and the entry says so.

## Commitment cue (verbatim, 2026-08-21)

- Cue: "lunch or the afternoon tomorrow"
- Action: "clear the engram reviews"
- Status: **stale** (names engram). Offer once in the new close ritual; if
  renewed, store the learner's new words verbatim with a new date.
