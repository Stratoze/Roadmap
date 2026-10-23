# Technical: what I've learned

Claude updates this at the end of each session. Status: done = matched its check; shaky = still mixing up; parked = not needed now.

## Done
- 0.1, 0.2
- 0.3 Euler step: new = old + rate × dt. α constant, ω changes each pass, θ uses the ω from before the pass. Loop matched the hand table for all three dt.
- 0.3 2-link forward kinematics: tip = (l1 cos θ1 + l2 cos(θ1+θ2), l1 sin θ1 + l2 sin(θ1+θ2)), θ2 relative to link 1. Predicted (1, 1) for θ1 = 0, θ2 = π/2.
- Pass counting: ω = 1, dt = 0.125 → 12–13 passes to reach π/2.
- 0.3 MVM (2026-10-10): power rule (v = 2t → a = 2; p = t³ − 2t → p′ = 3t² − 2, p″ = 6t). Integral of v = 2t over 0–3 s = 9 m via average speed / triangle; found x = t² by fitting x(0)=0, x(1)=1, x(3)=9. Going up loses constants; one known value pins C (p′(0) = −2 → C = −2). Derivative = rate at one instant (6 m/s at t = 3); integral = total over a stretch (9 m).

- 0.4 item 8 (2026-10-13): power → energy. P(t) = 6t W, 0–2 s: energy = area under P(t) = triangle, 1/2 × 2 s × 12 W = 12 J. Units given after a prompt.

- 0.3 item 9 (2026-10-13): area under v(t) = distance. Steady case 2 m/s × 3 s = 6 m; triangle 0→6 m/s over 3 s = 9 m. Said all three parts after hints: thin strip with steady speed, strip area = v × t = distance, strips add to the total. First attempts were circular ("area is distance because...") and a units-only argument; the missing link (rectangle area = height × width = speed × time) needed a nudge. Euler link not said.

- 0.4 item 17 (2026-10-20, tech-tutor, external chat): torque of link weight at 0°, 45°, 90°. Final: 0.049 N·m, 0.0343 N·m, 0 N·m (key 0.049, 0.035, 0; 0.0343 is within 2% using sin 45° ≈ 0.7, which the tutor gave as the one hint). Predicted 0° biggest, 90° smallest (committed after a hedge), 0.05 N·m at 0° (the key's 0.049 within rounding). Center of gravity explained by the learner as "roughly the middle" (not a full definition). Zero at 90° explained first by sin 0 = 0 (formula, rejected), then by force through the pivot (no lever arm), which the tutor accepted. Haiku checked against Answer and Check; ticked.

## Shaky
- Item 17: hedged predictions ("probably", "ish") before committing; first wrote a force formula instead of a torque prediction; sin 45° confused with 1/2 (that is sin 30°); units dropped on the 45° prediction.
- Power vs energy (2026-10-13): predicted 6 J, taking the average power (6 W) as the energy. Energy = area under P(t), not the average. Final answer phrased as a question ("Area under the curve?"): not yet said as a confident sentence.
- First instinct on area under v(t) was right-endpoint steps (2+4+6 = 12 m, overestimate); fixed with average speed
- Answers rules before concrete numbers ("derivative tells you the result…")
- Unit circle, radian values, position vs displacement

- 2026-10-23 item 18 (seesaw: 2 N down at 0.3 m left, find the force down at 0.2 m right): final answer 3 N down. Check passed (number with units). Tutor: DeepSeek web. Answer not given by the tutor: the learner made the torque sides (0.6 N·m), then F = 3 N. Ticked. Where the learner struggled: predicted bigger, about 3 N (right); torque in plain words only after prompting ("further from pivot = more torque"); units before the number; the learner did not read the exercise text and needed each side's sentence quoted back; the unit carried through the division only after a prompt; direction: wanted the left side's direction first, then reasoned that the right side pushes down; final answer needed one line with unit and direction.

## Parked
- Closed-form sum for θ after n passes (series algebra, not needed for the loop)
- 2026-10-15 item 13 (torque of 1 N at 0.1 m, 90°): answer 0.1 N·m, matches the check. First try was 1 N/0.1 m and 10 N/m (divided, and N/m is the wrong unit). Corrected: torque is N·m and distance multiplies. Shaky: the formula F × d × sin θ, written before the number. Not yet earned: "torque" in plain words (it was not explained by the learner). Items 10–12 still open (Sonnet-tagged).
- 2026-10-15 item 14 (1 N at 0.1 m, 45° vs 0°): predicted 90° bigger than 45° (right), computed 0.07 N·m at 45° (right, 0.0707). 0° case: predicted no torque for a force along the arm (right, 0 N·m). Asked "why" in depth (components along vs perpendicular to the arm, distance factor, torque = F·d·sin θ as work per radian); explained by Sonnet this session, learner can't yet say it back. Open: the learner's friction/slide-angle (tan θ > μ), pressure/area and material questions, parked for items 10–11 and 52–60.
- 2026-10-15 item 16 (torque of a 0.2 kg, 0.3 m link's weight about the shoulder, horizontal): W = m g = 1.96 N (method right, number after a prompt); d = 0.15 m from the pivot (first thought d = 0 because the weight acts at the middle, pivot vs center of mass mixed up); torque 1.96 × 0.15 = 0.294 N·m (learner said 0.3 ish, no unit at first); left out sin θ because θ = 90° (right). Learner avoids mental arithmetic; use the phone calculator.

## Not earned (explain in plain words instead)
- "first-order"
- "integral" (says "interval"), "accumulation", "displacement"
