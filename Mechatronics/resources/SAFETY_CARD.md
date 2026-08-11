# Safety Card

Read before real power, soldering, batteries, rotating parts, or anything that can move unexpectedly.
This is not a complete safety manual. It is the quick card.

**Safety knowledge is progressive.** You learn each hazard when it enters your workspace, not before.

---

## Phase Safety Envelopes

| Phase | Hazards present | You must know | Hard limits |
| --- | --- | --- | --- |
| 0 | Hobby knife, clipped wire ends | Cut away from body, eye protection when clipping | No soldering, no power tools, USB/5V only |
| 1 | Soldering iron 350 °C, low-voltage DC, spinning motors | Burn care, current limiting, entanglement | ≤ 24 V DC, through-hole only, no mains |
| 2 | Phase 1 + moving mechanisms with kinetic energy | Pinch points, travel limits, first-motion discipline | ≤ 24 V DC, 10% duty first motion |
| 3 | Phase 2 + 48 V bus, hotplate 250 °C, machined burrs | DC arc awareness, fusing, capacitor discharge, deburring | 48 V ceiling, fuse before power, discharge caps |
| 4 | Phase 3 + gravity-loaded arm, high current | Lockout, crush zones, hardwired safety verified with MCU dead | E-stop must work with MCU power pulled |
| 5 | Acrylic dust, adhesives | Ventilation, eye protection | Laser cutting done by service, not you |

## Stop immediately

Kill power now if there is:
- heat you did not expect
- smoke
- burning smell
- sudden current jump
- motor motion you did not command
- LiPo swelling
- loose probe/wire near high current or rotating parts

Explain after power is off.

## First power-on

- Current limit set before connection.
- Load disconnected unless intentionally testing it.
- One hand near power switch or supply output enable.
- DMM ready on expected rail.
- Know what current you expect before turning on.
- If current is wrong, power off first.

Use `templates/first_power_on.md` for real bring-up.

## Motors and motion

- Clear mechanical path.
- No loose clothing, wires, sleeves, hair, or tools near rotating parts.
- Current limit below destructive level.
- Motor mounted or constrained before torque tests.
- E-stop / power removal path known.
- First motion should be low voltage, low duty, low speed.

Use `templates/pre_motion_check.md` before motor tests.

## Soldering (enters Phase 1)

- Iron in its stand, always. Never on the bench.
- Ventilation: fan or open window. Flux fumes are harmful.
- Wash hands after leaded solder.
- Eye protection when clipping leads — they fly.
- Burn: cool running water 10 minutes. No ice.
- Unplug when done. The iron stays hot long after.

## 48 V DC bus (enters Phase 3)

- 48 V DC does not electrocute through dry skin, but it ARCS (DC arcs don't self-extinguish) and a short melts copper in milliseconds.
- Always fused. Fuse rated for stall current, not nominal.
- Always current-limited supply during bring-up.
- Capacitors store energy. After power-off, wait 30 s or bleed with a 1 kΩ resistor on insulated leads. Measure < 1 V before touching.
- One-hand rule when probing live circuits.
- Never work tired.

## Mains and high voltage

**Mains is OUT OF SCOPE for this entire roadmap.** Use bench supplies and purchased
certified AC-DC bricks. If a future job requires mains work, that is trained, certified,
supervised work — not self-taught, not in this vault.

## LiPo / batteries

- Non-flammable surface.
- Never charge unattended.
- Never use swollen cells.
- Do not puncture.
- Isolate damaged packs outdoors if safe to do so.
- Use correct charger and current limit.

Use `templates/lipo_check.md` only if LiPo enters scope.

## Mechanical work

- Safety glasses when drilling, cutting, clipping, grinding.
- Deburr sharp edges (CNC parts arrive sharp — deburr before handling, Phase 3).
- Clamp workpieces.
- Keep hands out of stored-energy paths: springs, falling links, belts, pinches.
- Gravity-loaded arm (Phase 4): verify the fall path is clear before first power.

## The rule

If the test requires courage, the setup is wrong.
Redesign the test until it feels boring.
