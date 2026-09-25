# Manufacturing Processes + DFMA (m0-8)

## Goal
- From `Mechatronics/ROADMAP.md` Phase 0: look at a part and name the manufacturing process that made it, and write a personal DFM/DFA checklist specific enough to audit Phase 3 designs.
- Phase 0 fabrication envelope: cardboard, hand tools, 3D printer only. This milestone is vocabulary and constraints, not shop time.

## Map
- No bracket yet - this topic opens at first contact.
- Concepts are the milestone's own pass-condition topics. Every concept has a book-tier locator; no concept is book-less.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| m8-1 | manufacturing family taxonomy (machining, forming, casting, molding; name the process that made a part) | - | unknown | 0 | - | - |
| m8-2 | 3-axis CNC constraints (internal sharp corners, undercuts, unreachable faces; DFM-annotated bracket sketch) | m8-1 | unknown | 0 | - | - |
| m8-3 | sheet metal constraints (bend radius, K-factor, grain direction; redesign the L-bracket) | m8-1 | unknown | 0 | - | - |
| m8-4 | casting/molding constraints (draft angles, fillets, uniform wall, ribs; sink marks and warpage) | m8-1 | unknown | 0 | - | - |
| m8-5 | joining and surface treatments (adhesives, brazing, rivets; anodize, powder coat, plating, passivation) | m8-1 | unknown | 0 | - | - |
| m8-6 | Boothroyd-Dewhurst DFA (minimize part count, z-axis assembly, self-locating features, minimize fasteners) | m8-2, m8-3, m8-4 | unknown | 0 | - | - |
| m8-7 | tolerance-cost tiers (+/-0.5 mm nearly free vs +/-0.01 mm expensive; tighten only where function demands) | m8-2 | unknown | 0 | - | - |
| m8-8 | personal DFM/DFA checklist (5 DFM + 3 DFA rules specific enough to audit Phase 3 designs) | m8-6, m8-7 | unknown | 0 | - | - |

## Resources

Active source selected JIT through the `resources` skill when the concept activates. Historical candidates and verification decisions are in [[_system/learning/archive/source-ledger|source ledger]].

## Usage events
| date | event_id | concept/item_ref | event | evidence | public note |
|------|----------|------------------|-------|----------|-------------|

## Misconceptions
-

## Problems
| id | problem | source | theory | attempts | status |
|----|---------|--------|--------|----------|--------|
| - | - | - | - | - | - |

## Links
- Rests on: 0.7 (materials and selection - process choice follows material and volume), 0.9 (mechanisms constrain what geometry is possible)
- Teaches: feeds 3.1 (QDD CAD, DFM, prototype-before-CNC gate), 3.2 (PCB is a different manufacturing family), 4.5 (printed joint wear)
- Lessons: -

## Log
- 2026-09-15 - file created for the Phase 0 foundational sourcing pass (plan §11), then re-run book-first under §11b. Every m8 concept has a book-tier locator. Two source defects recorded rather than smoothed: Kalpakjian ch 35 is mislabeled in the publisher's own preface and is therefore uncited, and Boothroyd's 3rd-ed TOC mislabels two entries so only 2nd-ed chapter numbers are claimed. One video substitute total. No reviews scheduled - rows stay `unknown` until taught.
