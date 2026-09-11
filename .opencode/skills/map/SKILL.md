---
name: Map
description: Estimate what Kohaku already knows on a topic - scoping question, strand selection, question rounds with floor/ceiling bracketing - and record a provisional map. Use at the start of a new topic, or when he says "test me in" or "what do I already know".
slash: false
---

# Map - approximate the edge

This is an estimate, provisional by design. It never gates teaching. Read
`_system/learning/learner.md` and the topic file first.

## Hard rules (never violate)

- **ONE question per message. Ask, then STOP and wait.** The next question is
  chosen from the answer you get; it does not exist yet. Never batch probes,
  never fire a fixed set, never sweep several strands in parallel. If your draft
  reply contains more than one probe, cut all but the first.
- **One strand at a time.** Bracket strand K (or explicitly pause it) before
  touching K+1. Coarse/overview maps are the same protocol with coarser
  strands - not a batch mode.
- **The cap counts graded probes, not messages.** 6 graded probes per sitting;
  more only if the learner asks.
- **Graded where gradable.** Items with a right answer use the question tool,
  constructed per `_system/learning/quiz-protocol.md`; open conversation is for
  the vague rungs and reasoning that cannot be option-set.
- **Self-report routes; it is never evidence.** "I know that" means test it;
  "no idea" is data.

1. **Scoping question first** (open, no right answer): "What do you want to be
   able to DO with this, and by when?" Store the answer verbatim in the topic
   file `## Goal`.
2. **Field scan**: spawn **scout** with the topic + goal and ask for the
   standard concepts, common framings, and gotchas (no sources needed). Prune
   the list with the learner. The pruned aims seed the `## Concepts` rows
   (state `unknown`).
3. **Question rounds**, one strand at a time: broad open question ("how would
   you approach X?") -> gradable probes -> narrow. Per question: ask -> wait ->
   grade (computable keys by execution) -> pick the next from the answer.
   Binary-search the edge: on a hit, jump difficulty up sharply; on a miss,
   narrow back in. Graded probes use the question tool where the item has a
   right answer (construction: `quiz-protocol.md`); open conversation otherwise.
4. **Bracket** each strand: one floor (a probe they get right) and one ceiling
   (one they miss). All correct -> not done, the ceiling is unfound; escalate
   until something breaks. One miss -> probe around it and characterize (slip,
   gap, or misconception) before concluding. The edge sits between floor and
   ceiling; teaching starts just past the floor (N+1).
5. **Self-report is never evidence.** "I know that" means test it; "no idea"
   is data.
6. **Zero schema** -> stop and hand to **study** for orientation.
7. **Write results** in `## Map`: `provisional (<date>)` notes per strand
   (bracketed: floor + ceiling; or unbracketed) and only unambiguous `state`
   changes. Revise from lesson evidence later. Cross-topic overview maps record
   the same way in `_system/learning/overview-map.md` (strand = unit).

Comfortable learners who say "test me in": start mid-map with one probe; a hit
walks down the unreceipted prerequisites, a miss drops below. Teaching proceeds
immediately with whatever bracket exists.
