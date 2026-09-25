---
name: Technical
description: Run a technical learning session for math, physics, electronics, or mechatronics - select the next deliverable, request a source, check cold understanding, take a real break, test fresh transfer and implementation, then route evidence to the assessor.
---

# Technical - scheduler, learner, verifier

Compose `map`, `resources`, `study`, `review`, and `assessor`. The learner
finds and reads the material; the agent selects the destination, asks the
checks, verifies the work, and records evidence. Read
`_system/How to Learn.md`, `_system/learning/learner.md`, the active roadmap,
and the topic dossier first.

## Select the next leg

Use, in order:

1. due reviews;
2. the active technical map/topic frontier;
3. the next roadmap milestone whose prerequisites are satisfied;
4. the next deliverable, dependency edge, and concise search keywords.

Do not ask the learner to choose the topic or run a scheduler command. The
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
   asking it, run `python3 scripts/question_signatures.py check "<prompt>" --record <technical-record>`; a non-zero result means the exact prompt was reused.
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
    table, evidence links, and next review. MVM/Full Pass requires the
    assessor's gate output.
    

## Question signatures

Store normalized signatures in the public technical lesson record at
`_system/learning/lessons/<topic>/<YYYY-MM-DD>-<slug>.md`. Use:

```bash
python3 scripts/question_signatures.py signature "<prompt>"
python3 scripts/question_signatures.py check "<prompt>" --record <record>
```

Normalization is Unicode NFKC, lowercase, collapsed whitespace, and stripped
Markdown formatting. The scope is the same topic/claim. A fresh-transfer or
implementation prompt must not exactly match a prior signature; the same
construct with new wording is allowed.

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
