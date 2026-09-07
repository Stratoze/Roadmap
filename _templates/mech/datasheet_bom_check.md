---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
---

# Datasheet + BOM Check — {{date}} — {{title}}

Paper gate BEFORE schematic freeze (not Gerber time — package/footprint errors found later cost a respin). Board-level parts only: passives, ICs, connectors, regulators, FETs, shunts. Mechanical life (bearings L10) and panel-level contactors/fuses belong to their own gates (3.1 sizing, 4.3 PDU), not here.

## Checks

- [ ] Every line has MPN, supplier SKU, stock + lead time with a DATE STAMP; substitutes named for long-lead parts; re-check stock at order time (snapshots rot in days)
- [ ] Absolute-maximum headroom verified per part (voltage, current, temperature) with derating
- [ ] Gate driver: bootstrap, deadtime, sequencing requirements extracted to the schematic notes — and the VALUES computed (C_boot, inrush, sequence order), not copied
- [ ] Encoder: gap spec, magnet type, keep-out distances on the layout notes
- [ ] Board-level fusing: present, DC-rated, sized per SAFETY_CARD
- [ ] No "equivalent" part substituted without re-checking pinout and ratings

## Verdict

- [ ] PASS to order / FAIL with rework list:
