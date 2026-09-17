# Problem-Solving Framework + Toolchain (m0-1)

## Goal
- From `Mechatronics/ROADMAP.md` Phase 0: the reasoning base everything else depends on, at "Applied" level.
- This milestone is already complete (MVM + Full Pass, August) - this file exists so later lessons have verified sources, not to re-teach it.

## Map
- Pre-system topic: knowledge predates the system, so this opens through **intake** (compressed cold verify per concept), never a full re-teach (standing order 3).
- No bracket recorded; the milestone's own pass conditions are the probe source.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| m1-1 | toolchain bring-up + blinky (compile and flash one program; stop when it blinks) | - | unknown | 0 | - | - |
| m1-2 | git baseline (repo init, first meaningful commit, save script used) | - | unknown | 0 | - | - |
| m1-3 | review queue baseline (Anki deck plus first vault review item scheduled) | - | unknown | 0 | - | - |
| m1-4 | input/output/transformation framing (state I, O, and transformation for any system) | m1-1 | unknown | 0 | - | - |
| m1-5 | functional decomposition (black boxes with interfaces precise enough to build independently) | m1-4 | unknown | 0 | - | - |
| m1-6 | first-principles reasoning (identify the conservation law doing the work) | m1-5 | unknown | 0 | - | - |
| m1-7 | Fermi estimation (order-of-magnitude answer before computing) | m1-1 | unknown | 0 | - | - |
| m1-8 | binary-search debugging (halve the fault space on a simple failure) | m1-4 | unknown | 0 | - | - |

## Sources
- rigorous | How to Solve It: A New Aspect of Mathematical Method | George Polya | book: ch 6 "Four phases" | https://press.princeton.edu/books/paperback/9780691164076/how-to-solve-it | for m1-4, m1-5, m1-6 | verified 2026-09-15
- rigorous | The Sciences of the Artificial (3rd ed.) | Herbert A. Simon | book: ch 8 "The Architecture of Complexity: Hierarchic Systems" | - | for m1-5 | verified 2026-09-15
- rigorous | Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems | David J. Agans | book: ch 8 "Divide and Conquer" (also ch 4 "Make It Fail") | - | for m1-8, m1-4 | verified 2026-09-15
- reference | Classical Mechanics 8.01SC (MIT OpenCourseWare, free) | MIT (Chakrabarty, Dourmashkin, Tomasik, Frebel, Vuletic) | course: Week 7 "Kinetic Energy and Work" (Lesson 20 "Kinetic Energy and Work in 1D"); Week 8 "Potential Energy and Energy Conservation" (Lesson 23 "Potential Energy", Lesson 24 "Conservation of Energy") | https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/week-8-potential-energy-and-energy-conservation/ | for m1-6 | verified 2026-09-15
- reference | Pro Git (2nd ed.) | Scott Chacon & Ben Straub | book: ch 1 "Getting Started" | https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control | for m1-2 | verified 2026-09-15
- reference | Anki Manual | Ankitects (official docs) | docs: getting-started | https://docs.ankiweb.net/getting-started.html | for m1-3 | verified 2026-09-15
- reference | Anki Manual - Deck Options | Ankitects (official docs) | docs: deck-options | https://docs.ankiweb.net/deck-options.html | for m1-3 | verified 2026-09-15
- interactive | Blink (Built-in Examples) | Arduino (official docs) | interactive: built-in-examples/basics/Blink | https://docs.arduino.cc/built-in-examples/basics/Blink/ | for m1-1, m1-4 | verified 2026-09-15
- interactive | Wokwi - Online Arduino/ESP32 Simulator | Wokwi B.V. | interactive: arduino | https://wokwi.com/arduino | for m1-1, m1-8 | verified 2026-09-15
- intuitive | Astable 555 timer - 8-bit computer clock, part 1 | Ben Eater | video | https://www.youtube.com/watch?v=kRlSFm519Bo | for m1-8, m1-4 | verified 2026-09-15
- intuitive | The Science of Thinking | Veritasium (Derek Muller) | video | https://www.youtube.com/watch?v=UBVV8pch1dM | for m1-6 | verified 2026-09-15
- intuitive | A clever way to estimate enormous numbers | TED-Ed (Michael Mitchell) | video | https://www.youtube.com/watch?v=0YzvupOX8Is | for m1-7 | verified 2026-09-15
- intuitive | Git and GitHub for Beginners - Crash Course | freeCodeCamp.org | video | https://www.youtube.com/watch?v=RGOj5yH7evk | for m1-2 | verified 2026-09-15
- intuitive | Learning how to learn | Barbara Oakley (TEDxOaklandUniversity) | video | https://www.youtube.com/watch?v=O96fE1E-rf8 | for m1-3 | verified 2026-09-15

No source found: **m1-7** has no verified rigorous book (`Guesstimation`, Weinstein & Adam, could not be TOC-verified); TED-Ed's *A clever way to estimate enormous numbers* is the only verified locator. Re-run the sourcing routine when a lesson blocks there.

Closed 2026-09-15: **m1-6** (the conservation-law framing) now has a verified locator - MIT 8.01SC Weeks 7-8. The earlier gap note was accurate at the time: `feynmanlectures.caltech.edu` still returns 403 to automated fetch, so Feynman stays uncited and MIT carries the concept instead.

## Misconceptions
-

## Problems
| id | problem | source | theory | attempts | status |
|----|---------|--------|--------|----------|--------|
| - | - | - | - | - | - |

## Links
- Rests on: none (foundation track)
- Teaches: feeds every later milestone's reasoning - decomposition (0.4, 3.1), Fermi (0.6, 0.10), binary-search debugging (all phases)
- Lessons: -

## Log
- 2026-09-15 - file created for the Phase 0 foundational sourcing pass (plan §11). Concept rows from the milestone's own pass conditions; sources pinned at section granularity by scout + verifier, verdicts dated 2026-09-15. Polish/nonbreaking-space and Unicode forms normalized to the vault convention. No reviews scheduled - intake only (standing order 3: never re-teach a passing verify).
