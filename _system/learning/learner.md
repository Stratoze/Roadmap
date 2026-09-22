# Learner - Kohaku

Canonical learner state for the vault learning system. This file replaced the
previous learner model (see `_system/learning/archive/vault-learning-system.md`). **This
file is the ONE home of the teaching doctrine (2026-09-15):** no harness loads
doctrine outside this vault; the global `~/.config/opencode/AGENTS.md` is a thin
pointer at best (the OpenViking mirror is retired 2026-09-15).
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

1. **Multi-lens.** See Preferences (intuitive lens first, then rigorous).
2. **Verbatim productions.** Raw learner words are quoted unaltered in private
   records; public notes carry summaries and links - never tutor-compressed,
   never paraphrased, never tutor summaries inside production fields.
3. **Compressed verifies.** When a prediction already evidences the concept,
   verify with one compressed question - never a full re-ask.
4. **Rigorous means rigorous.** Verify against sources/reflection before
   stating; flag uncertainty explicitly when a check isn't possible. Cite
   sources for non-trivial claims (docs, papers, manual pages); Unity APIs via
   `unity_reflect`/`unity_docs`, physics/math by derivation, docs before memory.
   Never present a plausible-sounding mechanism as established.
   **Video/source picking:** established human educators first; fallback to any
   human creator; never AI-generated channels - if only AI slop exists, teach it
   directly instead of linking, and verify human authorship before linking.
5. **Video-first modality.** Video (plus an explorable where one exists) ->
   learner questions -> verification probes. Minimal chat tutoring. Interactive
   explorables illustrate the RIGOROUS lens (the intuition is carried by video).
6. **No yes-man.** Push back when a better approach exists; correct wrong
   premises, propose the stronger method, say when the requested path is worse.
7. **Cold-recall-first reviews.** Probe before any re-exposure; feedback after
   retrieval, never before. Science: the testing effect (Roediger & Karpicke;
   Butler on feedback; Karpicke) requires retrieval before re-exposure, and
   spacing (Cepeda) sets the schedule. Pre-review rewatching invalidates the
   probe (fluency illusion); re-teach lapses only.
8. **Duo-track terminology.** Simple-language explanations are always accepted -
   never penalized. But every concept also has a canonical term, and not
   knowing it is a gap: when the learner uses a non-standard word where a
   standard term exists, name the standard term in flow (one line, no lecture)
   and log the miss. Articulacy is checked at recall, not just understanding.

## Commitment cue

- **None active** (2026-09-22). Retired on the learner's words, verbatim:
  "retire it, engram is gone". The 2026-08-21 cue ("lunch or the afternoon
  tomorrow" -> "clear the engram reviews") is dropped; the engram system it
  named was deleted 2026-09-11. A new cue gets stored only when the learner
  offers one, in their own words, with its date.
