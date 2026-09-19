[← Back to plan](README.md)

# 00 — Chassis redesign

Redesign the mechanical platform from scratch: simpler than the current build, and every part swappable without redesigning its neighbors. Sized to fit the electronics chosen in [hardware-bom.md](../hardware-bom.md) — GNSS antenna mast, electronics tray, Li-ion pack, dual motor mounts with encoder clearance, bumper linkage, dock contacts.

Depends on: nothing. Runs in parallel with [01](01-power-and-core-electronics.md).

## BOM

| Part | Qty | Have | Notes |
|---|---|---|---|
| PETG or ASA filament | ~1 kg | check | Structural parts outdoors |
| M3 and M4 screws, nuts, heat-set inserts | 1 assortment | check | Hole sizes are named parameters in the CAD |
| JGB37-520 gearmotor with Hall encoder, 12 V | 2 | buy | Needed now for the motor-pocket fit check. Pick rpm from the wheel diameter, see [hardware-bom.md](../hardware-bom.md) |
| Swivel caster | 1 | on hand | The salvaged one works for now |
| Wheel tread (TPU strip or rubber band) | 2 | buy | Bare plastic slips on damp grass |
| Bumper microswitches | 2 | on hand | Reused from the current build |

## Tasks

- [ ] Fix the chassis footprint — reuse the old 196×245 mm envelope or resize it
- [ ] Reserve mounting zones for: battery box, electronics tray, antenna mast, motor pockets, bumper linkage, dock pogo-pin contacts
- [ ] Design the motor mount as a standalone bolt-in part, not fused into the side wall
- [ ] Design the electronics tray as a lift-out plate, not a fixed internal shelf
- [ ] Carry over the named hole parameters from the old design (`M3HoleForBolt`, etc.) instead of re-deriving them
- [ ] Print the updated parts
- [ ] Dry-fit every part and every electronic component, no wiring yet
- [ ] Confirm both wheels spin freely by hand with everything mounted

## Exit test

Every part assembles without interference, all electronics sit in their dry-fit positions, and both wheels rotate freely by hand. No wiring exists yet.
