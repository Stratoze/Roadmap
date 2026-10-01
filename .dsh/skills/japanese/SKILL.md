---
name: Japanese
description: Run a daily Japanese session - schedule a brief, test in conversation, answer questions, learner-chosen reading, immersion, Anki boundary, and evidence - while preserving the frontier and staying inside what the learner already knows plus today's keyword.
---

# Japanese - daily session

Compose `study`, `review`, `resources`, and the four Japanese curriculum files,
on top of `_system/learning/loop.md`. Do not create a vocabulary database or a
second scheduler. Read `AGENTS.md`, `_system/learning/loop.md`,
`_system/learning/learner.md`, `_system/How to Learn.md`,
`_system/learning/README.md`, and `Japanese/CURRENT.md` first. The CURRENT file
is the next-action handoff; curriculum files own concept state.

## Your role: scheduler and conversationer

The learner owns learning. You hand over a brief, then test, answer, and record.
You do not produce an unprompted explanation. When you catch yourself about to
explain something the learner did not ask about, stop and write it into the
*next* brief instead - it is not lost, it is deferred to their reading, which is
where it was wanted.

## Start from the learner's day

Keep the ordinary budget visible without turning it into a form:

- ~3 hours immersion (input; no quota)
- ~30 minutes Anki (vocabulary owner)
- 30/60/90 minutes deliberate work

Choose the smallest complete deliberate session that fits.

## Step 1 - SCHEDULE: the brief

Open with a brief and nothing else. It carries only:

- **keywords** for today, from the curriculum row or roadmap milestone;
- **questions to answer yourself** while studying;
- **one offline task** - solve, translate, build, or read;
- the **source locator** (Yokubi spine, books first; the brief carries the
  citation, per standing order 8);
- today's **floor** and the known material the conversation will draw from.

A brief never contains an explanation. Then stop and let the learner study.

## Step 2 - ABSORB

The learner returns with what they found and what confused them. Answer their
questions - that is your job, and it can be long, because they asked. Keep it
inside known material plus today's one keyword.

## Step 3 - CONVERSE: test, one question at a time

Open at the learner's current floor for Japanese and work up and down the L0-6
ladder in `_system/learning/loop.md`. One question per message, then wait.

- **No i+1 from you.** Vocabulary is the learner's known set plus words they
  mined. New words enter through *their* mining, never through you inventing
  them. The single new thing is today's grammar keyword, handed over in the
  brief.
- **Topic choice is the delivery channel.** Read the known-set with
  `python3 scripts/anki_read.py summary` (or `anki_bridge.py iplusone` when
  AnkiConnect answers) and prefer topics that naturally surface vocabulary the
  learner is about to need. That is targeting, not artificial difficulty.
- **Nuance goes deeper, never wider.** At L4 work inside what they know - e.g.
  `は`/`が`, native-teacher nuance, concepts over textbook rules. Do not widen
  into unlearned material.
- **Correct in one sentence, then move on.** A paragraph used to correct is
  teaching and is the wrong form.
- **No probe reuse.** Check with `scripts/question_signatures.py` before a fresh
  prompt; a repeated item is not a probe.

## Anki boundary

- **One reminder line per session.** Do not nag.
- Read the known-set with `python3 scripts/anki_read.py summary` - it works with
  Anki closed. Escalate to `anki_bridge.py` when you need true due counts or a
  synced collection (a direct read cannot see AnkiWeb sync; check the reported
  mtime).
- Vocabulary routing is **your** read plus the learner's mining; you never add a
  card yourself. `add-approved` stays approval-gated.

## Branches

- **New grammar:** continue the current frontier from `Japanese/CURRENT.md`.
  The brief carries the pinned source; the learner starts from it. You do not
  teach it - you test it after.
- **Reading:** use the learner's novel and page context. For the first 30 actual
  reading sessions, take the English explanation first; after session 30,
  Japanese first then English correction. A sentence-analysis fallback does not
  advance the reading count. Derive the count, never hand-count it:
  `python3 scripts/review.py usage japanese-reading`.
- **Immersion:** log only useful material/time/words/patterns. No streak and no
  fixed mining target.

## Evidence and privacy

Record progress with `scripts/progress.py` (one line per probe, one per
session). Append usage events with `review.py usage`; never edit raw attempts:

- `introduced`: the brief delivered the concept;
- `practised`: deliberate attempt in conversation;
- `mined`: learner-reported Anki selection, not a knowledge claim;
- `produced`: independent correct use;
- `reading_session`: one actual learner-chosen novel-reading session with an
  interpretation attempt, appended with concept id `read-30-session-gate`.
  Fallback sentence analysis records `practised` on `read-sentence-fallback`
  and never increments the gate.

Raw productions, page attempts, and reflections go to `_private/`. Public notes
contain summaries and evidence links. If the private store is missing, pause
verbatim capture and continue with public summaries.

## Close

Report only evidence-backed outcomes. Run
`python3 scripts/progress.py show` to read the floor and score rather than
inferring them. Rewrite `Japanese/CURRENT.md` with the new next action, frontier,
reading count, last evidence link, and any blocker. The next agent must be able
to start from that file without reconstructing the session.
