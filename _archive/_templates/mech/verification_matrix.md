---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
---

# Verification Matrix — {{date}} — Project — {{title}}

Trace every requirement to a test, an evidence artifact, and a result.
If a row is incomplete, the requirement is a claim, not evidence.

## Scoring
- **Pass:** evidence exists, result meets requirement
- **Partial:** evidence exists, result is close but not within tolerance
- **Fail:** evidence exists, result does not meet requirement
- **Untested:** no evidence artifact exists

## Matrix
| Req # | Requirement | Source | Test method | Evidence artifact | Result | Status |
| --- | --- | --- | --- | --- | --- | --- |
| R01 | | Phase 0.4 hand calc | Static load test | `docs/captures/...` | | |
| R02 | | Phase 3 SIL gate | Simulation run | `simulations/python/...` | | |
| R03 | | Phase 3 HIL gate | Fault injection | `docs/captures/...` | | |

## Calibration & Uncertainty Records
| Parameter | Calibrated value | Uncertainty | Method | Date | Artifact |
| --- | ---: | ---: | --- | --- | --- |
| | | | | | |

## Coverage Summary
- Total requirements:
- Tested:
- Partial:
- Failed:
- Untested:

## Gaps & Known Limitations
List any requirement that could not be fully verified and why.
-

## Decision
Matrix complete / incomplete:
Ready for portfolio compilation: yes / no
