---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
---

# Mini-FMEA — {{date}} — System — {{title}}

Complete BEFORE design. Update AFTER fabrication/bring-up with what actually happened.

## Scoring guide

| Score | Severity (S) | Occurrence (O) | Detection (D) |
| ---: | --- | --- | --- |
| 1 | No effect / nuisance | Extremely unlikely (< 1 in 10,000) | Will almost certainly detect before harm |
| 4 | Degraded performance, no safety risk | Possible (1 in 100) | Likely to detect during test |
| 7 | Loss of function, potential damage | Moderate (1 in 20) | May not detect until field use |
| 10 | Safety hazard, injury risk | High (> 1 in 5) | Will NOT detect before harm |

**Risk Priority Number:** RPN = S × O × D.
RPN ≥ 48 or Severity ≥ 9: mitigation is REQUIRED before design proceeds.
RPN 20–47: mitigation recommended. Document if skipped.
RPN < 20: acceptable risk. Monitor.

## FMEA Table

| Item/function | Failure mode | Effect | Cause | S | O | D | RPN | Mitigation | Temporal horizon | Action |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| | | | | | | | | | | |

**Temporal horizon:** does this failure mode worsen over time? If yes, state the
mechanism and approximate timescale.
Examples: fatigue (cycles), creep (hours under load at temperature), corrosion
(exposure time), polymer outgassing (vacuum hours), electromigration (current-hours),
bearing wear (revolutions), connector fretting (vibration cycles), solder joint
fatigue (thermal cycles).
If the failure mode is instantaneous (shoot-through, short circuit), write "t=0".

## Highest risks (RPN ≥ 48 or S ≥ 9)

1.
2.
3.

## Actions before design proceeds

- [ ]

## Post-build update

After fabrication/bring-up, return here. For each verified landmine:

- Was it predicted by this FMEA? If not, add it.
- Was the mitigation sufficient? If not, update.
- What was the actual Severity / Occurrence / Detection?

| Verified landmine | Predicted? | Mitigation worked? | Updated S/O/D |
| --- | --- | --- | --- |
| | | | |
