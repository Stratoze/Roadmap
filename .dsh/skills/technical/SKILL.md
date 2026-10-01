---
name: Technical
description: Run a technical learning session for math, physics, electronics, or mechatronics - select the next deliverable, hand over a brief, test cold understanding and fresh transfer at the learner's floor, take a real break, verify, then route evidence to the assessor.
---

# Technical - scheduler, conversationer, verifier

Compose `map`, `resources`, `study`, `review`, and `assessor`, on top of
`_system/learning/loop.md`. The learner owns learning; you schedule the brief,
test, answer their questions, verify, and record. Read `AGENTS.md`,
`_system/learning/loop.md`, `_system/How to Learn.md`,
`_system/learning/learner.md`, the active roadmap, `Mechatronics/CURRENT.md`,
and the topic dossier first.

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

0. **Floor:** read the learner's current Mechatronics floor with
   `python3 scripts/progress.py show` (owned by `progress.py`; never
   hand-compute). Open every probe at or near that floor on the L0-6 ladder in
   `_system/learning/loop.md`.
1. **Scope:** name the next deliverable and its hard prerequisite/failure mode.
2. **Brief:** hand over keywords, the questions to answer yourself, one offline
   task, and the source locator (books first, per standing order 8). Then stop
   and let the learner work. Do not put an explanation in the brief, and do not
   write the learner's solution while they read.
3. **Learner reads:** let the learner choose how to read/watch the material.
4. **Cold conceptual check:** one Socratic question at a time, one message at a
   time. Do not re-expose the material before the attempt. Record the prompt and
   its signature. Correct in one sentence, then move on - a paragraph used to
   correct is teaching and is the wrong form.
5. **Break:** record ISO start/end timestamps around an actual 20-minute break.
   If the interval is not evidenced, do not claim the post-break stage is
   complete.
6. **Fresh transfer:** ask the same construct in a different context. Before
   asking it, run `python3 scripts/question_signatures.py check "<prompt>" --values "<values>" --context "<context>" --record _system/learning/lessons`; a non-zero result means the exact prompt or test variant was already used. Pass `--stage cold` when running the check for a conceptual probe instead — a cold check is allowed to re-ask a concept and the check will report the match without blocking.
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
    table, evidence links, and next review. Append the progress ledger with
    `python3 scripts/progress.py probe ...` per probe and one
    `... session ...` line. Rewrite `Mechatronics/CURRENT.md`
    with the target, dependency frontier, and next action. MVM/Full Pass
    requires the assessor's gate output.

## Record validity

A technical record is evidence only when it carries real evidence:

- `## Break` records ISO start and end at least 20 minutes apart. An unverified
  interval means the post-break stages are not complete, and the record is not
  gate or milestone evidence.
- Every `## Question variants` row (cold, fresh transfer, implementation) holds
  the exact prompt, its values/conditions, its context, and both signatures. An
  empty cell or a placeholder signature makes the record incomplete, not partial
  credit. See *Question and test variants* below for what `reused?` means.
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

**What may be reused, and what may not** (learner's decision, 2026-09-26).
Concepts and recipes are **free** — the approach is from first principles, so
re-deriving the same idea is the point, not cheating. Two things are bounded:

- **The same question, the same values, and the same scenario must not happen
  twice.** Not after a week, not after a year. Change any one of the three and
  it is a different test. "Why would you want to use the same value anyway —
  at least change up the number."
- **A question on its own** may be asked at most twice, and a repeat inside
  30 days is a failure: *"it gets annoying to see the same questions again and
  again."*
- **Any of that may be overridden** by writing the reason in the `reused?`
  column. A bare `yes` is disclosure that a repeat happened; it is not a
  reason, and does not unlock anything. Text in the cell is the reason.

`scripts/validate_learning.py` enforces exactly this: an instance (question +
values + context) used more than once with no reason fails, a third use of a
question fails, and a question repeated inside the cooldown fails. It is
checked across every topic in the corpus, not just within one. A validator
failure here is a real violation; if you believe it is not, the record or the
model is wrong, not the check.

Record the values/conditions and context in the technical session record so a
future agent can detect a repeated test instance, not merely a repeated
sentence.

## Boundaries

- Technical work is not a second concept tracker; concept state remains in the
  curriculum and review ladder.
- You schedule and test; you do not teach unprompted. An explanation you were
  about to volunteer belongs in the next brief (see `_system/learning/loop.md`).
- `ROADMAP.md` is the only active milestone status. Checkboxes are frozen
  acceptance history.
- Safety and red-zone hardware work remain mastery-gated and independently
  verified.
- Raw learner work stays in `_private/`; public records contain summaries and
  links.
- No background timer, silent wait, or invented elapsed time.
