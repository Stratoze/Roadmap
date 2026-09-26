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
  verify claims before stating them; cite non-trivial claims. See standing
  order 8.
- **Daily Japanese budget (2026-09-26):** 4–5 hours total: ~3 hours immersion,
  ~30 minutes Anki, and 30–90 minutes deliberate Japanese work. Weekend surplus
  extends reading/output rather than adding a grammar quota.
- **Reading gate:** 30 actual novel-reading sessions use English-first
  explanation; after the 30th session, Japanese-first explanation. Sentence-
  analysis fallback does not count.
- **Source policy:** books/videos are requested and selected JIT for the
  activated concept. The learner may supply a book; the tutor records only the
  active locator and does not maintain a standing source library.
- **AnkiConnect is local-only, by decision (2026-09-26).** Anki runs on the
  bridge device and Anki's own sync carries the collection between devices;
  there is no remote bridge. Rationale in the learner's words: AnkiConnect is
  fundamentally a local interface, a remote bridge adds networking,
  authentication and availability problems, and a key becomes necessary only
  if the bridge is exposed beyond the local machine. Motive: cross-device
  continuity. `scripts/anki_bridge.py` enforces loopback and keeps `apiKey`
  null while localhost — do not add a hosted bridge without a new decision.
- **Standing order 8, source-first (set 2026-09-15, learner's direction "books
  and videos for each lesson and phase instead of relying on AI"):** every
  concept carries a section-precise citation; the lesson starts there. AI
  exposition only on a documented `blocker`.

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
   **Source picking:** books first; where no book covers the concept, human
   educators only - never AI-generated channels, and verify human authorship
   before linking.
5. **JIT source-first modality.** The active concept gets one verified locator
   when it needs one. Ask the learner for a book/source when needed; use the
   resource scout/verifier on demand. The lesson starts at that locator, then
   the learner's questions, then one check. No standing source library.
6. **No yes-man.** Push back when a better approach exists; correct wrong
   premises, propose the stronger method, say when the requested path is worse.
7. **Cold-recall-first reviews.** Probe before any re-exposure; feedback after
   retrieval, never before. Science: the testing effect (Roediger & Karpicke;
   Butler on feedback; Karpicke) requires retrieval before re-exposure, and
   spacing (Cepeda) sets the schedule. Pre-review rewatching invalidates the
   probe (fluency illusion); re-teach lapses only.
8. **Source-first, AI second** (2026-09-26). Faithfully restating or translating
   the cited source into Japanese is allowed without adding claims. Any
   explanation beyond it requires a logged `blocker`; a missing citation is a
   sourcing gap, never a reason to lecture.
9. **JIT books over stockpiled videos** (2026-09-26). Books remain the first
   source when they cover the activated concept. Videos and interactives are
   verified substitutes or supplements selected at activation, not preloaded
   into roadmaps.
10. **Duo-track terminology.** Simple-language explanations are always accepted -
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
