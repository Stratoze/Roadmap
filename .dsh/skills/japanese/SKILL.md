---
name: Japanese
description: Run a daily Japanese learning session - grammar contrast, i+1 conversation, learner-chosen reading, immersion, Anki boundary, and evidence - while preserving the current frontier and using old material when it fits.
---

# Japanese - daily session

Compose `study`, `review`, `resources`, and the four Japanese curriculum files.
Do not create a vocabulary database or a second scheduler. Read
`_system/learning/learner.md`, `_system/How to Learn.md`,
`_system/learning/README.md`, and `Japanese/CURRENT.md` first. The CURRENT
file is the next-action handoff; curriculum files own state.

## Start from the learner's day

Keep the ordinary budget visible without turning it into a form:

- ~3 hours immersion (input; no quota)
- ~30 minutes Anki (vocabulary owner)
- 30/60/90 minutes deliberate work

Choose the smallest complete deliberate session that fits. Start with the work;
show the four-field brief only when it helps orient the session:

1. relevant grammar known;
2. relevant vocabulary known;
3. new/mined items;
4. today's immersion intention.

## Choose the branch

For a fresh/reset handoff, do not open with a generic due-review pass. Start
with a short conversation warm-up, then teach the first usable grammar
contrast, then use it immediately. Dedicated review is used when the learner
asks for it or after the current concept has actually been taught.

- **New grammar:** open the current frontier from `Japanese/CURRENT` and
  curriculum state, request/verify one source JIT, teach one usable contrast,
  practise it, then use it in conversation.
- **Conversation:** use mostly known grammar with a small useful i+1 addition.
  Reuse old grammar when it fits even if it is not due.
- **Reading:** use the learner's novel and page context. For the first 30
  actual reading sessions, take the English explanation first; after session
  30, take Japanese first and then English correction. A sentence-analysis
  fallback does not advance the reading count.
- **Immersion:** log only useful material/time/words/patterns. No streak and no
  fixed mining target.
- **Anki:** vocabulary lives there. Record only learner-reported mining events
  in the vault; never claim complete knowledge without a bridge.

## Teaching grammar

Read the language ramp in the curriculum. At L1, use Japanese terms and
examples with a concise English scaffold; at L2, alternate bilingual probes; at
L3, lead in Japanese. This preserves the requested Japanese explanation style
without stranding the learner before the schema exists.

Open the cited locator before teaching. Faithfully restate or translate it into
Japanese without adding claims. Explain the point in Japanese first where the
ramp allows, then give the English bridge. Contrast it with the nearest related
form and cover:

- what information the form foregrounds;
- when a speaker chooses it;
- register and pragmatic nuance;
- a minimal contrast;
- a likely learner trap.

Ground-up means rebuilding the dependency explanation from first principles
when needed. It does not erase evidence, reset a map, or abandon an unfinished
re-encode.

## Evidence and privacy

Append usage events with `review.py usage`; never edit raw attempts:

- `introduced`: deliberate teaching/selection;
- `practised`: deliberate attempt;
- `mined`: learner-reported Anki selection, not a knowledge claim;
- `produced`: independent correct use;
- `reading_session`: one actual learner-chosen novel-reading session with an
  interpretation attempt. It increments the 30-session reading gate. Fallback
  sentence analysis records `practised` on `read-sentence-fallback` and never
  increments the gate.

Raw productions, page attempts, and reflections go to `_private/`. Public notes
contain summaries and evidence links. Do not persist novel screenshots or long
passages. If the private store is missing, pause verbatim capture and continue
with public summaries.

At close, report only evidence-backed outcomes and rewrite
`Japanese/CURRENT.md` with the new next action, frontier, reading count, last
evidence link, and any blocker. The next agent must be able to start from that
file without reconstructing the session.
