# Mechatronics — Current Target Handoff

**Updated:** 2026-09-26
**Status:** no active target selected.

This is the mutable technical next-action file. The ROADMAP owns deliverables,
dependencies, keywords, safety, and status. This file owns the currently chosen
capability, the dependency frontier, and the next technical session.

## Start here next time

1. Invoke the `technical` skill.
2. If the learner has named a target such as “make a robot arm,” ask one scoping
   question, then write the target here.
3. Map the target to required capabilities and compare them with existing
   curriculum evidence.
4. Select the smallest missing prerequisite that actually gates the target.
5. Teach that prerequisite in the target's context, then return to the target.
6. Rewrite this file at the end of the technical session.

## Selection rules

- Goal-driven, not fixed-textbook-driven.
- Existing evidence is preserved and used as a dependency input.
- Phase-0 priority is a tie-breaker among required items:
  math → physics → electronics → software/embedded → other mechatronics
  dependencies.
- A Phase-0 item that the chosen target does not require is not a gate.
- A required Phase-0 item is taught before attempting the dependent target.
- Prerequisites are explained both generally and through the chosen target.
- After the foundational phase, choose one target capability/MVM, list its
  dependencies and keywords, then run the technical learning cycle.

## Technical session cycle

```text
source/read
→ cold conceptual check
→ 20–30 minute foreground pause
→ fresh transfer with new values/conditions
→ implementation or theory test
→ Feynman repair if needed
→ assessor/review
```

The same construct may be revisited, but the same test item, value set, or
lab condition may not be reused for fresh transfer or implementation. Full
Pass requires a new scenario and new evidence.

## Current known dependency frontier

- ROADMAP milestone 0.3 Calculus Intuition is the first open Phase-0
  deliverable; its keywords include derivative, accumulation, net change, and
  Euler step.
- The 2026-09-22 ODE lesson produced review evidence for c1 and c4–c7, but it
  never taught the c2 → c3 chain underneath them (slope field, solution
  curves). The evidence is real; the foundation below it is not.
- `review.py due` therefore withholds c4 and c7, because both depend on c3 and
  c3 is still `unknown`. This is the queue working, not missing data.
- If the chosen target requires 0.3, teach c2 → c3 first, then return to the
  target. Do not re-probe c4–c7 cold; they are already in review state.

## Current target

- Target: none selected
- Target artifact/capability:
- Required capabilities:
- Existing evidence reused:
- Missing prerequisite frontier:
- Safety/evidence boundary:
- Source requested/selected:
- Last technical evidence:
- Next action:

## Close contract

Before ending a technical session, update:

- target/artifact and current dependency frontier;
- missing prerequisite and next action;
- source locator or blocker;
- last evidence path and assessor result;
- the daily checklist state.

Do not leave this file describing work that has already happened.

## Daily order

The daily resolver uses:

```text
Japanese → Anki/due review → target-driven technical work
```

Use `python3 scripts/session_state.py today` for the daily checklist and next
action. Do not infer completion from elapsed time; update the checklist
explicitly.
