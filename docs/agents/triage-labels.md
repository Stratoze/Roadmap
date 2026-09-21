# Triage Labels

The skills speak in terms of five canonical triage roles. This file maps those roles to the actual label strings used in this repo's issue tracker.

| Label in mattpocock/skills | Label in our tracker | Meaning                                  |
| -------------------------- | -------------------- | ---------------------------------------- |
| `needs-triage`             | `needs-triage`       | Maintainer needs to evaluate this issue  |
| `needs-info`               | `needs-info`         | Waiting on reporter for more information |
| `ready-for-agent`          | `ready-for-agent`    | Fully specified, ready for an AFK agent  |
| `ready-for-human`          | `ready-for-human`    | Requires human implementation            |
| `wontfix`                  | `wontfix`            | Will not be actioned                     |

When a skill mentions a role (e.g. "apply the AFK-ready triage label"), use the corresponding label string from this table.

Edit the right-hand column to match whatever vocabulary you actually use.

## Wayfinder labels

Used by `/wayfinder` alongside the triage roles (never as substitutes — a ticket
carries exactly one triage-role label plus at most one wayfinder label):

| Label | Meaning |
| ----- | ------- |
| `wayfinder:map` | The single map issue holding Notes / Decisions-so-far / Fog |
| `wayfinder:research` | Child ticket: investigate and report back |
| `wayfinder:prototype` | Child ticket: throwaway build to answer a design question |
| `wayfinder:grilling` | Child ticket: stress-test thinking before deciding |
| `wayfinder:task` | Child ticket: plain unit of work |

When labelling issues, follow the skill rules strictly — no extra mandatory labels.
