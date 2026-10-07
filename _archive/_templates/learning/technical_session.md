---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
topic: "{{topic}}"
type: technical
---

# Technical session — {{date}} — {{title}}

## Target and source

- Deliverable:
- Dependencies:
- Search keywords:
- Active source locator:
- Safety/evidence boundary:

## Learner-produced attempt

Summary only; raw production belongs in `_private/`.

## Cold conceptual check

- Prompt:
- Normalized signature: (sha256 from `python3 scripts/question_signatures.py signature "<prompt>"`)
- Response summary:
- Result:

## Break

Record the real start and end around an actual break. A break that is not
timestamped leaves the record incomplete: the post-break stages cannot be
claimed, and the record is not valid gate or milestone evidence.

- Start (ISO):
- End (ISO):
- Elapsed minutes:
- Verified 20-minute interval: (yes only when Start/End above prove at least 20 minutes)

## Question variants

Every cell of every row is required: exact prompt, the values/conditions used,
the context, and both signatures. An empty cell or a placeholder signature means
the record is incomplete and cannot back a gate. Fill the row before asking the
question, then paste the signatures the check printed.

Concepts and recipes are free to reuse — the approach is from first principles.
What is bounded: the same question *with the same values and scenario* must not
happen twice, ever; and a question alone may be asked at most twice, never
inside 30 days. `reused?` is where a justified exception goes — write the reason
there. A bare `yes` only records that a repeat happened; it is not a reason and
does not unlock anything.

| stage | prompt | values/conditions | context | prompt signature | variant signature | reused? |
|-------|----------------|------------------|---------|------------------|------------------|---------|
| cold | | | | | | |
| fresh transfer | | | | | | |
| implementation | | | | | | |

## Implementation/theory test

- Prompt:
- Values/conditions:
- Context/fixture:
- Artifact/evidence path:
- Execution or inspection result:

## Feynman repair

- Triggered: yes/no
- Learner explanation summary:
- Fresh repair task/result:

## Assessor

- Requested gate: mvm/full/none
- Verdict:
- Per-criterion results:
- gate_met: yes/no
- gate_earned: mvm/full/none
- Blockers:

## Evidence and next

- Public evidence links:
- Usage events appended:
- Next review/action:

## Record validity

- Break timestamps present and at least 20 minutes apart:
- Every question-variant row filled with prompt, values/conditions, context, and both signatures:
- No variant row marked reused:
- `python3 scripts/validate_learning.py` passes for this record:

A record fails the technical gate while any line above is unfilled. Do not
describe an unfinished record as a completed session or as milestone evidence.
