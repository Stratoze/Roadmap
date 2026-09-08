# GOAL — QDD 2-DOF arm (DRAFT — pass-1 scaffold, unconfirmed)

- **Name:** QDD 2-DOF arm
- **Actuator type:** quasi-direct-drive (BLDC + low-ratio planetary gearbox + dual encoders — see Phase-3 QDD artifact in [[Mechatronics/milestones/03_mech_pcb_verification|03 ⁠— Model-Based Design & Verification]])
- **DOF:** 2 (shoulder + elbow)
- **Work envelope:** bench-scale 2-link arm; voltage/fabrication ceilings per the phase envelopes in [[Mechatronics/ROADMAP|Roadmap]] (exact envelope set at goal-confirm, pass 2)
- **Success criteria:** two characterized QDD joints integrated into a 2-DOF arm on CAN with Safety PDU + gripper, trajectory tracking demonstrated, portfolio demo recorded (see Phase-4 hero in [[Mechatronics/ROADMAP|Roadmap]])
- **Era slug:** `qdd-arm (2026-08-)`
- **Parked history:** `Mechatronics/goals/parked/` (empty — first goal, nothing parked)

## Checklist

Semantic-pass record — seeded in pass 1, dispositions finalize in pass 2 (post-confirm).
Schema: `- [ ] <coupling> -> <disposition>`; disposition = `keep:<location>` | `parameterize` | `park:<slug>` | `delete+log`.

- [ ] `Mechatronics/resources/CONVENTIONS.md:46-55` (arm frame defaults) -> parameterize
- [ ] `Mechatronics/milestones/00_foundations.md` 0.2/0.4/0.7 arm-flavored procedures ->
- [ ] `Mechatronics/milestones/00_foundations.md` 0.9 backdrivab pedagogy ->
- [ ] `Mechatronics/milestones/00_foundations.md` 0.10 lever-arm metrology ->
- [ ] `Science/Index.md:14` (arm assumptions) ->
- [ ] `DataScience/Index.md:9,13` (arm assumptions) ->
- [ ] `Mechatronics/resources/LAB_INFRASTRUCTURE.md` goal mentions ->
- [ ] `Mechatronics/IDEAS.md` goal mentions ->
- [ ] `Mechatronics/hardware/inventory.md` goal mentions ->

## Appendices

Empty — pass 2 lists each moved chunk here, one line per chunk in this form:

```
- [title](path)
```

- Skills persist in the [[Mechatronics/skills/registry|skill registry]] (rows keep `Evidence tag` + `Goal era`; pre-swap rows backfilled per the Phase-2 plan).
