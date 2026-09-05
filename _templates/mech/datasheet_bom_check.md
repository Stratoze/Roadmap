---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
---

# Datasheet + BOM Check — {{date}} — {{title}}

Paper gate BEFORE schematic freeze / BOM order. Wrong parts burn weeks, not hours.

## Checks

- [ ] Every line has MPN, supplier SKU, stock + lead time; substitutes named for long-lead parts
- [ ] Absolute-maximum headroom verified per part (voltage, current, temperature, ESD rating)
- [ ] Gate driver: bootstrap, deadtime, sequencing requirements extracted to the schematic notes
- [ ] Encoder: gap spec, magnet type, keep-out distances on the layout notes
- [ ] Contactors/fuses: DC rating cited from the datasheet, sized for stall + inrush
- [ ] Bearings: dynamic load rating + L10 life vs target hours on the sheet
- [ ] No "equivalent" part substituted without re-checking pinout and ratings

## Verdict

- [ ] PASS to order / FAIL with rework list:
