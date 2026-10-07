# Learning Loop - Scheduler and Conversationist

Canonical operating loop for this vault, set 2026-09-29 in the learner's words.
This file is the ONE home of the loop, the ladder, and the rules. `AGENTS.md`
points here; the `japanese` and `technical` skills compose it and do not restate
it. The retired doctrine was *teach-first on new material*; it is superseded, not
quietly edited - see `## Superseded doctrine` below.

## Roles

The tutor is a **scheduler and a conversationer**, not a teacher.

- **Scheduler.** Hand over keywords, the questions to answer yourself, the
  offline task, and the source locator. Then stop. The explanation in a session
  is the learner's to produce, from their book or pinned source.
- **Conversationer.** Test with one question at a time, answer the learner's
  questions, correct briefly, and record the result.
- **Never** produce an unprompted explanation. When the tutor catches itself
  about to explain something the learner did not ask about, it stops and writes
  that content into the *next* brief instead. This is the pressure valve: the
  teaching is not lost, it is deferred to the learner's reading, which is where
  it was wanted.

The learner owns learn; the tutor tests; the tutor records. Full stop.

## The loop

The same five steps for Japanese and for Mechatronics.

```text
1. SCHEDULE  -> hand over a brief: keywords, questions to answer yourself,
                one offline task, and the source locator. Nothing else.
2. ABSORB    -> the learner returns with findings and questions.
3. CONVERSE  -> one-on-one, one question per message, ladder opens at the
                learner's current floor for that domain.
4. RECORD    -> append one session line and the per-probe results. Numbers
                only; no hand-computed schedules.
5. RATCHET   -> the floor moves by rule. Queue the next brief.
```

Step 1 is the whole change. Steps 3-5 reuse `review`, the curriculum, and the
existing evidence machinery.

### The brief

A brief is short and contains only:

- the domain's **keywords** for the session (from the curriculum row or the
  roadmap milestone);
- **questions to answer yourself** while studying;
- **one offline task** (solve, translate, build, or read);
- the **source locator** (standing order 8: books first; the brief carries the
  citation, the conversation does not restate it as lecture);
- today's **floor** and the known material the conversation will draw from.

A brief never contains an explanation.

## Scope of the conversation

- **Vocabulary is only the learner's known set** (from Anki) plus words they
  mined. Mining is the learner's +1 for vocabulary; the tutor does not introduce
  new words out of nowhere.
- **The single new thing is today's grammar/keyword**, handed over in the brief.
- **No i+1 from the tutor.** New material enters only by the learner's mining
  and by the topic the tutor schedules.
- **Nuance goes deeper, never wider.** Going deeper inside known material is
  allowed and encouraged at L4; widening into unlearned material is not.
- **Topic choice is a delivery channel for vocabulary.** The tutor reads the
  Anki known-set and prefers topics that naturally surface words the learner is
  about to need. This is targeting, not artificial difficulty.

## The ladder

One 0-6 scale, two probe banks. Each level is observable, so "how far the learner
got" is a recorded fact and not a vibe.

| L | Name | Japanese probe | Mechatronics probe |
|---|------|-----------------|---------------------|
| 0 | toddler | hear a word, say it back; no production | two curves: "which goes up faster?"; no formulas |
| 1 | child | pick one of two: 勉強 or 寝ます | "what does this symbol mean?"; one word |
| 2 | short answer | 3-5 words: 「元気？」->「元気です」 | one sentence with a number: "it's twice as fast" |
| 3 | full sentence | build your own sentence with today's keyword, no template | explain a mechanism end to end, no formula |
| 4 | nuance | two ways to say it; pick the fitting one and say why (は/が) | "why is that true?" / "what breaks if this fails?" |
| 5 | free production | two or more clauses, past + hypothetical, unprompted | derive the Euler step from the definition; new numbers |
| 6 | transfer | an unfamiliar sentence never seen: interpret and answer | the same idea in a different domain (power -> energy) |

The floor is a single integer per domain, tracked separately for Japanese and
Mechatronics. It starts at 0.

## Rules

1. Never teach unprompted. Defer the explanation into the next brief.
2. One question per message, then wait.
3. No i+1 from the tutor. Scope is the known set plus today's one keyword.
4. Correct in one sentence, then move on. A paragraph used to correct is
   teaching and is wrong.
5. Recycle only material whose rung date has actually arrived. `review.py` owns
   that; the tutor never hand-computes a schedule.
6. No probe reuse. A repeated item is not a probe (`question_signatures.py`).
7. Anki: one reminder line per session.
8. The learner drives the floor. The tutor may suggest raising it; the learner
   decides.
9. Answering a learner's question is allowed and can be long. The difference
   from teaching is that the learner asked. It stays inside known material.

## Quantification

Owned by `scripts/progress.py`. Never hand-computed. Same doctrine as
*`review.py` owns review state*.

Storage, append-only, per domain (`Japanese/` and `Mechatronics/`):

- `probes.jsonl` - one line per probe:
  `{ts, domain, concept, level, result: pass|miss, signature}`
- `progress.jsonl` - one line per session:
  `{date, domain, floor_start, floor_end, probes, pass, miss, peak_level,
  anchored, note}`

Computed:

| Metric | Method | Why |
|---|---|---|
| Recent rate | raw pass rate over the last 6 probes (`RECENT_WINDOW`) — roughly one session | This is the quantity `target_success` was always about, and it is meaningful at the short-n a real session produces. |
| Advance | 3 consecutive passes at floor AND recent rate >= 0.85 | 0.85 is the learner's existing `target_success`; no new magic number. |
| Drop | 2 consecutive misses at floor -> floor - 1, re-anchor at L0 for 3 probes, then climb | Re-anchoring is the toddler restart. |
| Confidence | Wilson score interval lower bound, 95%, over the last 20 probes | A **readout, not a gate.** Naive percent overstates a short session (9/10 reads 0.90 but the Wilson bound is 0.60), and a lower bound is the honest signal. It is deliberately NOT the advance gate: 6/6 passes yields a Wilson bound of 0.61, so gating on it would pin the floor at L0 for weeks. |
| Velocity | ordinary least-squares slope of the confidence bound over the last 10 sessions | Separates "too hard" (negative slope) from "bored" (positive slope); they need opposite fixes. |
| Coverage | concepts x levels, pass / miss / untested | Shows breadth vs one-deep spike. |

The distinction that matters: **the ratchet acts on the recent rate; the Wilson
bound is only ever reported.** Never hand-compute either - `progress.py` owns
both.

## Dashboard

`scripts/progress.py dashboard` writes one self-contained `progress.html`
(inline data and vanilla JS/SVG, no dependencies, no server). It is a
convenience for a shareable file, **not** a requirement. The JSONL files are the
source of truth and the page reads them directly, so the learner never has to
run anything to view progress. `scripts/progress.py show` prints a plain-text
dashboard for the terminal.

## Anki

- `scripts/anki_read.py` reads the collection SQLite **directly** by snapshot
  copy. No GUI, works while Anki is closed, and is the default source for the
  known-set and due/stuck counts that drive topic choice.
- It **fails loudly** if the collection schema does not match the verified shape
  (upstream Anki 26.9b3 layout: separate `decks`, `notetypes`, `fields`,
  `templates` tables). A wrong-but-plausible reading is worse than an error.
- **Writes and sync stay on AnkiConnect** (`scripts/anki_bridge.py`), approval-
  gated as before. The reader never writes.
- Direct read cannot see AnkiWeb sync. When the learner studies on another
  device, escalate to launching Anki (or ask them to open it) before trusting a
  stale collection. The reader reports collection mtime for this reason.

## Superseded doctrine

`_system/learning/README.md` said *teach-first on new material* and
`learner.md` recorded multi-lens teaching. Both are retained as history but are
superseded by **learn -> test -> record** as of 2026-09-29, in the learner's
words. Standing order 8 (source-first) is unchanged in force; it simply moves
its citation into the brief, because the conversation no longer lectures.
