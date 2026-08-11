# Phase 5 — Portfolio & Delivery

## Outcome

Documentation, media, and presentation that make the engineering process visible.
Not marketing — a technical record that proves you can think, build, debug, and explain.

This phase is deload-shaped. The learning is in the doing: refactoring reveals what you
didn't understand, documentation reveals what you skipped, presentation reveals what you
can't yet explain.

**Physical artifacts of this phase:**
1. Exploded-View Pedestal — one QDD actuator disassembled and presented in assembly order on laser-cut acrylic, every component labeled
2. Bench Museum — a single display holding every phase artifact, telling the dependency-tree story

**Fabrication & safety envelope (Phase 5):** laser-cut acrylic/wood via service, hand assembly, LED lighting. Ventilation if sanding acrylic; eye protection. No electronics fabrication. Do NOT disassemble the arm's actuators until the final demo video is recorded.

### Assessment Philosophy

The portfolio is not evaluated on "did it work." It is evaluated on the **process of
arriving at the solution**. Engineering judgment is the ability to draw conclusions,
make decisions under uncertainty, and weigh trade-offs based on incomplete information.
The portfolio must make that process visible.

The assessment framework is **criterion-referenced**, not pass/fail. Each domain below
is rated on a rubric (see `templates/portfolio_rubric.md`). The rubric evaluates
observable behaviors, not just artifacts.

### Portfolio Domains (from `templates/portfolio_rubric.md`)

1. **Design Process & Requirements Analysis** — Did you elicit, document, and trace
requirements? Can you justify design choices against them?
2. **Modeling & Analysis** — Were physical models appropriate? Were simulations validated?
Were failure modes identified via FMEA?
3. **Experimental Validation & Failure Analysis** — Did you design relevant experiments?
Did you compare predictions to reality (Hypothesis Loop)? Did you conduct root-cause
analysis on discrepancies?
4. **Systems Integration & Trade-off Analysis** — Were subsystems integrated cleanly?
Did you navigate competing constraints (cost, weight, performance, reliability)?
5. **Communication & Professionalism** — Are reports, diagrams, and presentations clear?
Are decisions documented? Are limitations acknowledged honestly?

---

## Phase Pass Condition

### MVM
- [ ] 20+ page engineering report exists
- [ ] One demo video: workcell running
- [ ] Code repo clean and navigable
- [ ] Verification matrix completed (`templates/verification_matrix.md`)
- [ ] **Physical:** exploded view assembled, ≥ 5 labeled components

### Full Pass
- [ ] Report: requirements → design → build → test → results → lessons
- [ ] All hand calcs, FEA, schematics, firmware architecture included
- [ ] FMEA compiled and updated with actual failure modes encountered
- [ ] Decision records and Verified Landmines compiled
- [ ] Calibration records, interface contracts, and test evidence paths compiled
- [ ] **Verification matrix completed:** every requirement → test → evidence → result,
with calibration/uncertainty records. Use `templates/verification_matrix.md`.
- [ ] **Portfolio rubric self-assessed:** rate yourself on all 5 domains using
`templates/portfolio_rubric.md`. Identify your weakest domain. Write one paragraph
on what you'd do differently to strengthen it.
- [ ] **Stress inoculation completed:** at least one timed debugging exercise using
`templates/stress_inoculation.md`. Document what broke under pressure and what
survived.
- [ ] Video: well-lit, stable, shows cold-boot → run → shutdown
- [ ] Code refactored, consistent naming, no dead code, tagged `v1.0-release`
- [ ] Resume: 4–6 metric-driven bullets
- [ ] 5-minute presentation practiced and delivered
- [ ] **Physical:** exploded-view pedestal complete; Bench Museum assembled and photographed; narrated walkthrough video
- [ ] **Metacognitive reflection completed** (see below)

---

# Milestone 5.1 — Portfolio + Documentation

> [!info] 📚 Resources — Portfolio & Delivery
> Self-work: compile decision records, captures, retros.
> Use `_templates/mech/verification_matrix.md`, `portfolio_rubric.md`, `stress_inoculation.md`.

## Deliverable

Complete engineering documentation package: report, video, clean repo, resume bullets,
practiced presentation, verification matrix, rubric self-assessment, and metacognitive
reflection.

## Pass Condition

### MVM
- [ ] Report draft: overview, block diagram, key calcs, key decisions, test results
- [ ] One video: full cycle
- [ ] README.md: what this is, how to build it, what I learned
- [ ] Verification matrix started: at least the top 5 requirements traced

### Full Pass
- [ ] Report 20+ pages with all technical content
- [ ] FMEA: what can fail, what happens, what mitigates (updated with real data)
- [ ] Decision records compiled from milestone files
- [ ] Verified Landmines compiled: what actually tripped me
- [ ] Calibration records, interface contracts, and capture paths compiled into appendix
- [ ] **Verification matrix complete:** every requirement from Phase 0–4 that fed the
capstone is traced to a test, evidence artifact, and result. Use
`templates/verification_matrix.md`.
- [ ] **Rubric self-assessment:** rate all 5 domains. Identify weakest. Write improvement
paragraph. Use `templates/portfolio_rubric.md`.
- [ ] **Stress inoculation:** at least one timed fault-injection debugging exercise.
Document: what you expected, what actually happened under time pressure, what
debugging strategy you defaulted to, whether it worked. Use
`templates/stress_inoculation.md`.
- [ ] Video: narrated or captioned
- [ ] Code: refactored, tagged `v1.0-release`
- [ ] Resume bullets: specific tools, specific metrics
- [ ] 5-min presentation: what it is, how it works, one trade-off, one surprise,
what I'd do differently
- [ ] **Metacognitive reflection:** answer ALL of the following in the report or a
dedicated appendix section. These are not marketing. They are evidence that you
can think about your own thinking, which is what engineering judgment actually is.

### Metacognitive Reflection Prompts

Answer each one. 2–5 sentences per prompt. Be specific. Reference actual milestones,
actual bugs, actual decisions.

1. **What did I think I knew at the start that turned out to be wrong?**
Name the specific assumption. Name the milestone where it broke. Name what replaced it.
2. **What debugging strategy did I use most, and when did it fail me?**
Name the strategy (binary search? scope-first? git diff? ask AI?). Name the specific
failure where it didn't work. Name what you switched to.
3. **Where did my mental model diverge most from physical reality?**
Name the specific prediction that was most wrong. Name the gap. Name what updated
your model.
4. **What would I need to remember if I encountered this project again in 6 months?**
Write it as if you're leaving a note for future-you. What's the one thing you'd
forget first?
5. **What prior knowledge did I apply that was the WRONG knowledge?**
Name the concept. Name where you applied it. Name why it was wrong for this context.
This is "galvanic interference" — a concept from one domain corroding another.
6. **If I were mentoring someone through this project, what would I tell them to
do differently?**
Not "study more." Be specific. "Do X before Y." "Don't trust Z until you've
verified W."

> [!warning] ⚠️ Landmines
> 1. **Documentation is the last engineering task, not "writing it up."** `[HYPOTHESIS]`
> Explaining the system reveals gaps in understanding. If you can't explain why you
> chose star grounding, you don't understand why.
>
> 2. **Don't write from scratch. Compile.** `[HYPOTHESIS]`
> Decision records, verified Landmines, hand calcs, FEA plots, retros — already written
> in milestone files. The report assembles them.
>
> 3. **The video needs to be real, not polished.** `[HYPOTHESIS]`
> Phone on tripod, good lighting, 60-second cold-boot-to-run. Show one failure and
> recovery if you have it. Authenticity > production.
>
> 4. **Resume bullets are evidence, not job descriptions.** `[HYPOTHESIS]`
> Not: "Worked on a robotic arm project."
> Instead: "Designed custom STM32 FOC controller achieving ±20mA Id tracking; designed
> 4-layer PCB; implemented dual-channel hardware E-Stop per IEC 62061 principles."
>
> 5. **The verification matrix is not busywork.** `[HYPOTHESIS]`
> If you can't trace a requirement to a test to an evidence artifact, you don't have
> evidence. You have a claim. The matrix is what separates "I built it" from "I can
> prove I built it correctly." This is what a senior engineer at NASA or SpaceX would
> ask for first.
>
> 6. **The rubric self-assessment is not self-grading. It's self-diagnosis.** `[HYPOTHESIS]`
> You're not giving yourself a score to feel good. You're identifying the domain where
> your judgment is weakest. That's the domain to strengthen next. Honesty here is the
> whole point.
>
> 7. **Stress inoculation is not optional polish.** `[HYPOTHESIS]`
> If you've only ever debugged in calm, unhurried conditions, you don't know what your
> debugging process looks like under pressure. The timed exercise reveals your actual
> default strategy, not your theoretical one. This is state-dependent learning: the
> neurochemical state of "the board is smoking and I have 5 minutes" is different from
> "let me think about this over coffee." You need reps in both states.
>
> 8. **The metacognitive reflection is the highest-value artifact in the portfolio.**
> `[HYPOTHESIS]`
> A hiring manager can see your code. They can see your CAD. They can't see how you
> think. The metacognitive reflection is the only artifact that shows your thinking
> process. It's also the only one you can't fake. If you can't answer "what assumption
> was wrong?" with a specific example, you didn't actually learn. You just completed
> tasks.
>

## Dependencies that waste your week if hit backwards

- Open all milestone files and pull raw material BEFORE writing. Don't stare at a
blank page.
- Refactor code BEFORE writing the firmware architecture section. The section describes
the refactored version, not the messy one.
- Complete the verification matrix BEFORE writing the report. The matrix is the skeleton.
The report is the flesh.
- Complete the rubric self-assessment BEFORE the metacognitive reflection. The rubric
tells you where you're weak. The reflection explores why.
- Practice the presentation BEFORE recording the video. The practice reveals what you
can't explain; the video captures what you can.
- Do the stress inoculation BEFORE writing the report. The results feed into the
metacognitive reflection.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 5.2 — Exploded-View Pedestal + Bench Museum

> [!info] 📚 Resources — Display Fabrication
> **Visual:** iFixit-style teardown displays; museum exhibit labeling.
> **Interactive:** laser-cut acrylic stand (service), mount components, label, light.
> **Fabrication:** laser-cut 3–5 mm acrylic via service; hand assembly; label maker; LED strip. No machining.

## Deliverable

**Exploded-View Pedestal:** ONE QDD actuator disassembled and mounted in strict assembly
order on acrylic with labels:
- Stator + rotor (what you bought vs. what you designed)
- Planetary gearbox (ratio, backlash spec)
- The Puck (call out gate drivers, STM32G4, shunts, CAN transceiver)
- Output encoder + diametric magnet (gap spec from the datasheet)
- Bearings (fit classes H7/k6, L10 life you calculated)
- CNC housing (material, tolerances, anodize note)
- Output shaft + retaining method
- Fasteners (grade, torque spec)

Each label: name + function + one key spec. The pedestal must read as the assembly
sequence, top to bottom or left to right — not a pile.

**Bench Museum:** one display holding every phase artifact — mechanism testbed module,
VCA, Phase 1 rig, IMU perfboard, haptic knob, pendulum cart (or its photo if too large),
the Puck, the QDD, gripper, tool changer, PDU. Each with a one-line label and (optionally)
a QR code to its capture folder. This is the dependency tree from the ROADMAP, made visible.

## Pass Condition

### MVM
- [ ] Actuator disassembled, components arranged in assembly order
- [ ] Acrylic stand assembled, stable
- [ ] ≥ 5 components labeled

### Full Pass
- [ ] All major components labeled with name + function + key spec
- [ ] Assembly order readable at a glance
- [ ] Backlighting installed
- [ ] Bench Museum assembled: every phase represented, curated (no junk-drawer boxes of failed boards — pick the representative ones)
- [ ] Hero photos: exploded view (multiple angles) + museum wide shot + details
- [ ] 60–90 s narrated walkthrough video
- [ ] Labels legible in photos (high contrast, adequate size)

> [!warning] ⚠️ Landmines
> 1. **Acrylic cracks under impatient drilling.** `[COMMUNITY]`
>    Laser-cut the holes via the service, or drill slow with a sharp bit. Score-and-snap for straight cuts only.
>
> 2. **Order is the whole point.** `[HYPOTHESIS]`
>    Random layout = parts bin. Housing back → bearing → shaft → gearbox → motor → Puck → bearing → housing front. A stranger should trace the assembly with their eyes.
>
> 3. **Don't disassemble the only working actuator before the demo video exists.** `[HYPOTHESIS]`
>    Record the final arm video FIRST. Then disassemble one QDD for the pedestal. Ordering this backwards costs a rebuild.
>
> 4. **The museum is curated, not complete.** `[HYPOTHESIS]`
>    Every artifact displayed must represent a milestone. Tangled jumper-wire relics undermine the story you spent 18 months building.
>
> 5. **Labels are portfolio text.** `[HYPOTHESIS]`
>    They get photographed and zoomed. Write them like resume bullets: specific, metric-bearing, jargon only where the audience (an engineer) earns it.
>

## Dependencies that waste your week if hit backwards

- Final demo video BEFORE disassembly.
- Order laser-cut acrylic BEFORE writing final labels — stand dimensions set label positions.
- Photograph in good light BEFORE the submission deadline. Bad lighting ruins good hardware.

> Log sessions in Daily/ notes using the unified template.

---

# Final Retro

Actual total time vs. range, 12–24 months:
The three things I understand now that I couldn't have imagined at Day 1:
The landmine that cost the most time:
The prediction that was most wrong:
The debugging strategy that failed me most often:
The domain (from the rubric) where my judgment is weakest:
The physical artifact I'm most proud of:
The physical artifact that taught me the most:
What I'd tell Day-1 me:
