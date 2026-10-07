---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
---

# FEA Acceptance — {{date}} — {{title}}

Evidence gate BEFORE CNC order. A contour plot is decoration until these pass.

## Checks

- [ ] Hand calc first (bending/shear/torsion on the critical feature), documented with numbers
- [ ] Worst-case load value stated; material + yield source cited; FoS computed vs yield (a converged plot that exceeds yield still FAILS)
- [ ] Boundary conditions audited: constraint points and point loads named as idealizations
- [ ] 3 mesh densities run; finest two agree within 5%
- [ ] Peak stress within 20% of hand calc at MATCHED nominal locations (stress concentrations compared separately with Kt explicit — never fudge BCs to force agreement)
- [ ] Single-node spikes read as singularities until proven otherwise (refine, never screenshot-and-ship)

## Verdict

- [ ] PASS to CNC / FAIL with rework list:
