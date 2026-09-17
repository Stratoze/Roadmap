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

## Sources
Levels are the point of this pass: Kalpakjian and Boothroyd are **intermediate**; Bralla is **advanced/practitioner** (an audit-tier handbook to look things up in, not to read linearly); Jensen and LibreTexts are **beginner** and assume nothing.

- rigorous | Manufacturing Engineering and Technology (8th ed., Pearson, 2020) - **intermediate**, 1200+ pp., reference to skim by section | Kalpakjian & Schmid | book: Introduction I.1 "What Is Manufacturing?", I.3 "Design for Manufacture, Assembly, Disassembly, and Service"; ch 10 "Fundamentals of Metal Casting"; ch 12 "Metal Casting: Design, Materials, and Economics"; ch 16 "Sheet-Metal Forming Processes and Equipment"; ch 21 "Fundamentals of Machining"; ch 23 "Machining Processes: Turning and Hole Making"; ch 25 "Machining Centers, Machine-tool Structures, and Machining Economics"; ch 32 "Brazing, Soldering, Adhesive-bonding, and Mechanical Fastening Processes"; ch 34 "Surface Treatments, Coatings, and Cleaning" | - | for m8-1, m8-2, m8-3, m8-4, m8-5, m8-8 | verified 2026-09-15
- rigorous | Product Design for Manufacture and Assembly (2nd ed., Marcel Dekker, 2002) - **intermediate**; ch 3 is self-contained | Boothroyd, Dewhurst & Knight | book: ch 2 "Selection of Materials and Processes"; ch 3 "Product Design for Manual Assembly"; ch 7 "Design for Machining"; ch 8 "Design for Injection Molding"; ch 9 "Design for Sheet Metalworking"; ch 10 "Design for Die Casting"; ch 12 "Design for Sand Casting"; ch 13 "Design for Investment Casting" | - | for m8-1, m8-2, m8-3, m8-4, m8-6 | verified 2026-09-15
- reference | Design for Manufacturability Handbook (2nd ed., McGraw-Hill, 1999) - **advanced/practitioner, audit tier** | James G. Bralla (ed.) | book: Section 1 "General Design Principles for Manufacturability"; Section 3 "Metal Stampings"; Section 4 "Designing for Machining: General Guidelines"; Section 5 "Castings"; Section 7 "Design for Assembly (DFA)" + "Soldered and Brazed Assemblies" + "Adhesively Bonded Assemblies"; Section 8 "Polished and Plated Surfaces", "Other Metallic Coatings", "Organic Finishes" | - | for m8-2, m8-3, m8-4, m8-5, m8-6, m8-8 | verified 2026-09-15
- reference | Introduction to Mechanical Design and Manufacturing (open textbook, CC BY-NC, Univ. of Arkansas Libraries, 2024) - **beginner** | David Jensen | book: ch "Types of Cutting and Machining Process and Tolerances" -> "Machining Cost and Tolerance", "Expected Tolerances" | https://uark.pressbooks.pub/mechanicaldesign/chapter/types-of-cutting-and-machining-pocess-and-tolerances/ | for m8-7 | verified 2026-09-15
- interactive | Design for Various Manufacturing Methods (Engineering LibreTexts, NWTC) - **beginner** | NWTC / LibreTexts | book: ch 2 "DFM Guidelines for Specific Manufacturing Processes" -> "Injection Molding", "Casting", "Sheet Metal Fabrication", "CNC Machining" | https://eng.libretexts.org/Courses/Northeast_Wisconsin_Technical_College/Design_for_Various_Manufacturing_Methods/02%3A_DFM_Guidelines_for_Specific_Manufacturing_Processes | for m8-2, m8-3, m8-4, m8-8 | verified 2026-09-15
- interactive | DFMA: What Is Design for Manufacturing (DFM)? Principles, Examples & Checklist | Boothroyd Dewhurst, Inc. (originators of the method) | page: design-for-manufacturing | https://www.dfma.com/design-for-manufacturing.asp | for m8-6, m8-8 | verified 2026-09-15
- intuitive (substitute) | What is a K-Factor? - Sheet Metal Bend Allowance Explained | TriMech Group | video | https://www.youtube.com/watch?v=kUizKC1gkg0 | for m8-3 | verified 2026-09-15

Edition caveats (do not silently upgrade):
- **Kalpakjian ch 35 is unusable.** In both the 8th-ed preface PDF and the Pearson catalog, ch 35 prints as "Surface Treatments, Coatings, and Cleaning" - duplicating ch 34 - while its subsections are measurement standards and GD&T. It is really "Engineering Metrology and Instrumentation" (Pearson's 9th-ed page prints that title). Ch 35 is cited **nowhere** above. Ch 10/12/16/21/23/25/32/34 titles are identical in the 6th, 8th and 9th editions.
- **Boothroyd edition:** numbers above are the **2nd ed.**, the only edition with a machine-readable printed TOC. The 3rd ed. exists and matches one-for-one on chapter *titles*, but its TOC mislabels two entries, so 3rd-ed chapter numbers are not claimed. If buying one book for this milestone, the 3rd ed. is the better buy; use titles, not numbers, to navigate it.

Gaps (recorded, not papered over):
- **m8-3 K-factor** has no dedicated sheet-metal *design* reference verified at chapter level. Boljanovic *Sheet Metal Forming Processes and Die Design*, Marciniak et al. *Mechanics of Sheet Metal Forming*, and Eary & Reed *Techniques of Pressworking Sheet Metal* all exist but no TOC was fetchable. K-factor rests on Kalpakjian ch 16 + Boothroyd ch 9, which are less explicit than a die-design text.
- **m8-5 passivation** specifically: Bralla Section 8 covers plating/coatings; "passivation" was not a named subsection in the fetched list, so it is covered only implicitly.
- **m8-7 tolerance-cost tiers:** only the open textbook chapter verifies; no print chapter naming a tolerance-cost table was verified (Kalpakjian ch 25 "Machining Economics" is the likely home but its subsection list was not extractable).
- No verified third-party graded exercise set for Boothroyd-Dewhurst part-count reduction. The milestone's own deliverable (bracket -> minimum part count) is the real exercise.

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
