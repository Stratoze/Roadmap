# Safety Card

Read before real power, soldering, batteries, rotating parts, or anything that can move unexpectedly.
This is not a complete safety manual. It is the quick card.

---

## Stop immediately

Kill power now if there is:

- heat you did not expect
- smoke
- burning smell
- sudden current jump
- motor motion you did not command
- LiPo swelling
- exposed mains uncertainty
- loose probe/wire near high current or rotating parts

Explain after power is off.

---

## First power-on

- Current limit set before connection.
- Load disconnected unless intentionally testing it.
- One hand near power switch or supply output enable.
- DMM ready on expected rail.
- Know what current you expect before turning on.
- If current is wrong, power off first.

Use `templates/first_power_on.md` for real bring-up.

---

## Motors and motion

- Clear mechanical path.
- No loose clothing, wires, sleeves, hair, or tools near rotating parts.
- Current limit below destructive level.
- Motor mounted or constrained before torque tests.
- E-stop / power removal path known.
- First motion should be low voltage, low duty, low speed.

Use `templates/pre_motion_check.md` before motor tests.

---

## Mains and high voltage

Applies to mains or above 48 V.

- Verified off before touching.
- One-hand rule.
- Never tired.
- No floating exposed conductors.
- Use isolation and proper enclosures where applicable.
- If unsure, stop and get review.

Use `templates/mains_check.md` only if this enters scope.

---

## LiPo / batteries

- Non-flammable surface.
- Never charge unattended.
- Never use swollen cells.
- Do not puncture.
- Isolate damaged packs outdoors if safe to do so.
- Use correct charger and current limit.

Use `templates/lipo_check.md` only if LiPo enters scope.

---

## Soldering / chemicals

- Ventilation on.
- Eye protection when clipping leads.
- Wash hands after leaded solder.
- Resin/solvents: gloves and ventilation.
- Burn: cool water for 10 minutes.

---

## Mechanical work

- Safety glasses when drilling, cutting, clipping, grinding.
- Deburr sharp edges.
- Clamp workpieces.
- Keep hands out of stored-energy paths: springs, falling links, belts, pinches.

---

## The rule

If the test requires courage, the setup is wrong.
Redesign the test until it feels boring.
