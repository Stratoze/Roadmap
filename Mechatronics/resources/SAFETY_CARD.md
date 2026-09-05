# Safety Card

Read before real power, soldering, batteries, rotating parts, or anything that can move unexpectedly.
This is not a complete safety manual. It is the quick card.

**Safety knowledge is progressive.** You learn each hazard when it enters your workspace, not before — and you do not enter next-phase energy without its section below plus its template first.

---

## Phase Safety Envelopes

| Phase | Hazards present | You must know | Hard limits |
| --- | --- | --- | --- |
| 0 | Hobby knife, clipped wire ends | Cut away from body, eye protection when clipping | No soldering, no power tools, USB/5V only |
| 1 | Soldering iron 350 °C, low-voltage DC, spinning motors | Burn care, current limiting, entanglement | ≤ 24 V DC, through-hole only, no mains |
| 2 | Phase 1 + moving mechanisms with kinetic energy | Pinch points, travel limits, first-motion discipline | ≤ 24 V DC, 10% duty first motion |
| 3 | Phase 2 + 48 V bus, hotplate 250 °C, machined burrs | DC arc awareness, fusing, capacitor discharge, deburring | 48 V ceiling, fuse before power, discharge caps, current-limited bring-up |
| 4 | Phase 3 + gravity-loaded arm, high current | Lockout, crush zones, hardwired safety verified with MCU dead | E-stop must work with MCU power pulled (all Phase-3 electrical rules still apply) |
| 5 | Acrylic dust, adhesives (the 48 V arm + PDU still exist — all Phase 3–4 electrical rules still apply) | Ventilation, eye protection | Laser cutting done by service, not you |

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

Use `_templates/mech/first_power_on.md` for real bring-up.

## Motors and motion

- Clear mechanical path.
- No loose clothing, wires, sleeves, hair, or tools near rotating parts.
- Current limit set below the destructive level of the weakest link (wire ampacity, connector rating, FET/motor stall) — name the number before power.
- Motor mounted or constrained before torque tests.
- E-stop / power removal path known and tested (not just known).
- First motion MUST be low voltage, low duty (≤10% per the Phase-2 envelope), low speed.

Use `_templates/mech/pre_motion_check.md` before motor tests.

## Soldering (enters Phase 1)

- Iron in its stand, always. Never on the bench.
- Ventilation: fan or open window. Flux fumes are harmful.
- Wash hands after leaded solder.
- Eye protection when clipping leads — they fly.
- Burn: cool running water 10 minutes. No ice.
- Unplug when done. The iron stays hot long after.

## ESD (enters Phase 1 — first silicon handling)

- Grounded wrist strap + mat for STM32, encoders, gate drivers. If it's too much trouble to strap on, the board is already dead — you just don't know it yet.

## Heat + resin (enter Phase 3)

- Hotplate 250 °C: burn care as for the iron, plus fume ventilation.
- Resin printing (optional): SDS read first, nitrile gloves, IPA wash + UV cure with ventilation — resin is a sensitizer, not "just plastic".

## 48 V DC bus (enters Phase 3)

- 48 V DC does not electrocute through dry intact skin — but sweat, cuts, jewelry, and probe slips erase that margin, and it ARCS (DC arcs don't self-extinguish) while a short melts copper in milliseconds.
- Always fused. Fuse protects the *wiring*: sized above nominal draw, below wire ampacity, and verified to blow on a dead short. Motor stall/overload protection is separate — a fuse rated at stall current allows sustained stall.
- Always current-limited supply during bring-up.
- Capacitors store energy. After power-off, discharge through a ≥5 W-class resistor (e.g. 1 kΩ/5 W, or 2× 2 kΩ/3 W in parallel) on insulated leads for a fixed 10 s — clipped on first, hands clear, let the body cool before touching it — then remove it. Then measure < 1 V before touching anything; if still above 1 V, repeat and investigate (the bus is bigger than assumed). Waiting alone is NOT a discharge method for large bus caps; "briefly" is not a time. (τ = R·C: 10 s covers mF-class buses; scale up for larger.)
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

Use `_templates/mech/lipo_check.md` only if LiPo enters scope.

## Mechanical work

- Safety glasses when drilling, cutting, clipping, grinding.
- Deburr sharp edges (CNC parts arrive sharp — deburr before handling, Phase 3).
- Clamp workpieces.
- Keep hands out of stored-energy paths: springs, falling links, belts, pinches.
- Gravity-loaded arm (Phase 4): verify the fall path is clear before first power.

## The rule

If the test requires courage, the setup is wrong.
Redesign the test until it feels boring.
