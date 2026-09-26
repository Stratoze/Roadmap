---
name: Technical
description: Run a technical learning session for math, physics, electronics, or mechatronics - select the next deliverable, request a source, check cold understanding, take a real break, test fresh transfer and implementation, then route evidence to the assessor.
---

# Technical - scheduler, learner, verifier

Compose `map`, `resources`, `study`, `review`, and `assessor`. The learner
finds and reads the material; the agent selects the destination, asks the
checks, verifies the work, and records evidence. Read
`_system/How to Learn.md`, `_system/learning/learner.md`, the active roadmap,
`Mechatronics/CURRENT.md`, and the topic dossier first.

## Select the next leg

The daily resolver calls this skill after the Japanese block and the capped
due-review block. Within technical work:

1. read `Mechatronics/CURRENT.md` for the chosen capability/artifact;
2. map its required capabilities and dependencies;
3. compare those requirements with existing curriculum evidence;
4. select the smallest missing prerequisite that actually gates the target;
5. use the Phase-0 priority only as a tie-breaker:
   `math → physics → electronics → software/embedded → other dependencies`.

Do not ask the learner to choose a topic or run a scheduler command. The
roadmap names the deliverable, dependencies, keywords, and safety/evidence
boundary; it does not contain a source library.

## Session sequence

1. **Scope:** name the next deliverable and its hard prerequisite/failure mode.
2. **Source request:** ask the learner to choose/request a book or source. Use
   `resources` to scout/verify one on demand; record only the active locator.
3. **Learner reads:** let the learner choose how to read/watch the material.
   Do not write the learner's solution while they work.
4. **Cold conceptual check:** one Socratic question at a time. Do not re-expose
   the material before the attempt. Record the prompt and its signature.
5. **Break:** record ISO start/end timestamps around an actual 20-minute break.
   If the interval is not evidenced, do not claim the post-break stage is
   complete.
6. **Fresh transfer:** ask the same construct in a different context. Before
   asking it, run `python3 scripts/question_signatures.py check "<prompt>" --values "<values>" --context "<context>" --record _system/learning/lessons`; a non-zero result means the exact prompt or test variant was already used.
7. **Implementation/theory:** learner derives, calculates, builds, debugs, or
   otherwise performs the work. The agent executes/inspects/verifies; it does
   not author the artifact.
8. **Feynman repair:** if a real gap appears, the learner explains it simply,
   then solves a fresh transfer problem. Do not force a Feynman lecture after a
   clean attempt.
9. **Assessor:** hand the blind assessor the claim, rubric, questions,
   production or permitted public artifact, execution output, and evidence
   pointers. The assessor has no shell access; the parent runs any permitted
   execution first. Raw private context is excluded.
10. **Record:** write the public technical session record at
    `_system/learning/lessons/<topic>/<YYYY-MM-DD>-<slug>.md` (or the active
    technical record named by the template), including the `## Question variants`
    table, evidence links, and next review. Rewrite `Mechatronics/CURRENT.md`
    with the target, dependency frontier, and next action. MVM/Full Pass
    requires the assessor's gate output.

## Record validity

A technical record is evidence only when it carries real evidence:

- `## Break` records ISO start and end at least 20 minutes apart. An unverified
  interval means the post-break stages are not complete, and the record is not
  gate or milestone evidence.
- Every `## Question variants` row (cold, fresh transfer, implementation) holds
  the exact prompt, its values/conditions, its context, and both signatures. An
  empty cell, a placeholder signature, or `reused? = yes` makes the record
  incomplete, not partial credit.
- The record was read back, not written from memory: the learner's own words
  stay in `_private/`, and no timing, signature, or gate is invented.

Run `python3 scripts/validate_learning.py` and confirm the record passes before
calling a session complete or handing the record to `scripts/milestone.sh` as
`--evidence`. Do not repair a failing record by editing the learner artifact.

## Question and test variants

Store normalized prompt signatures in the public technical lesson record at
`_system/learning/lessons/<topic>/<YYYY-MM-DD>-<slug>.md`. Use:

```bash
python3 scripts/question_signatures.py signature "<prompt>" --values "<values>" --context "<context>"
python3 scripts/question_signatures.py check "<prompt>" --values "<values>" --context "<context>" --record _system/learning/lessons
```

`--record` takes a file, a topic directory, or several of them, and reuse is
checked across all of them. Name every record set the question could collide
with: `--record _system/learning/lessons` covers every topic, while naming a
single topic is the narrower, weaker check. A single record file also counts the
sibling records beside it in the same topic directory.

Normalization is Unicode NFKC, lowercase, collapsed whitespace, and stripped
Markdown formatting. Reuse is a whole-record property, not a per-topic one: a
prompt or test instance already used under another topic is still a reuse. The
same construct with new wording is allowed.

Also vary the test instance, not only the wording:

- reuse the concept/equation freely;
- do not reuse the same numerical values, parameter set, lab condition, or
  implementation fixture for fresh transfer or implementation;
- change the surface context and at least one meaningful input/condition;
- Full Pass requires a new scenario and new evidence.

**Severity is graduated, and the stage sets the severity** (learner's direction,
2026-09-26):

- **Cold conceptual check — warning.** The point of the check is retrieval of
  one named concept, so the same concept asked in new words is legitimate
  teaching, not cheating. Warn, name the prior use, and move on.
- **Fresh transfer — hard failure.** A repeated prompt *or* a repeated test
  instance here means the learner was handed the answer they were meant to
  reach. Stop, discard the attempt, and re-ask with a new context and new
  values.
- **Implementation / theory test — hard failure.** Same standard. A reused
  fixture or lab condition is a reused test, regardless of the wording.

Record the values/conditions and context in the technical session record so a
future agent can detect a repeated test instance, not merely a repeated
sentence.

## Boundaries

- Technical work is not a second concept tracker; concept state remains in the
  curriculum and review ladder.
- `ROADMAP.md` is the only active milestone status. Checkboxes are frozen
  acceptance history.
- Safety and red-zone hardware work remain mastery-gated and independently
  verified.
- Raw learner work stays in `_private/`; public records contain summaries and
  links.
- No background timer, silent wait, or invented elapsed time.
