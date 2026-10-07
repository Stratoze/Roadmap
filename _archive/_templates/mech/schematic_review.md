---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
---

# Schematic Review — YYYY-MM-DD — Board

## Board

Name:

Revision:

## Power

- [ ] Input voltage range defined
- [ ] Fusing / protection checked (fuse present, DC-rated, sized per SAFETY_CARD)
- [ ] Reverse polarity checked (survives a backwards plug or is keyed against it)
- [ ] Regulator thermal checked (dissipation math per rail, not a feeling)
- [ ] All rails named consistently

## MCU / digital

- [ ] Programming header correct
- [ ] Boot pins handled
- [ ] Reset circuit checked
- [ ] Clock source checked
- [ ] Decoupling on every power pin

## Motor / power stage

- [ ] Gate driver datasheet reviewed
- [ ] Deadtime computed and verified on scope (not just "known")
- [ ] Bootstrap / inrush / sequencing VALUES computed (C_boot, NTC/soft-start, enable order) — not copied from a reference
- [ ] Current-sensing topology documented
- [ ] Sense resistor power checked
- [ ] ADC input range protected

## Layout constraints to carry forward

- Ground return:
- High-current loops:
- Sensitive analog:
- Differential / comms:

## Review result

Proceed / hold:

Issues:
