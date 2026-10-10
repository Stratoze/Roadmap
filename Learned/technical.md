# Technical: what I've learned

Claude updates this at the end of each session. Status: done = matched its check; shaky = still mixing up; parked = not needed now.

## Done
- 0.1, 0.2
- 0.3 Euler step: new = old + rate × dt. α constant, ω changes each pass, θ uses the ω from before the pass. Loop matched the hand table for all three dt.
- 0.3 2-link forward kinematics: tip = (l1 cos θ1 + l2 cos(θ1+θ2), l1 sin θ1 + l2 sin(θ1+θ2)), θ2 relative to link 1. Predicted (1, 1) for θ1 = 0, θ2 = π/2.
- Pass counting: ω = 1, dt = 0.125 → 12–13 passes to reach π/2.

## Shaky
- Unit circle, radian values, position vs displacement

## Parked
- Closed-form sum for θ after n passes (series algebra, not needed for the loop)

## Not earned (explain in plain words instead)
- "first-order"
