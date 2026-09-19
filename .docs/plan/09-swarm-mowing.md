[← Back to plan](README.md)

# 09 — Swarm mowing

The capstone iteration: the full swarm mows a shared lawn with zone division, blades on, and every robot returns to a dock on its own.

Depends on: [05](05-single-robot-autonomy.md), [06](06-cutting-deck.md), [07](07-charging-dock.md), [08](08-swarm-comms.md).

## BOM

Each additional robot repeats the robot-side parts of 00, 01, 02, 03, 06, plus the LC29H(BA) rover, antenna and level shifter from [04](04-rtk-positioning.md) and the IR receivers, contact pads and Hall sensor from [07](07-charging-dock.md). The base station and the MQTT broker are shared, so they aren't repeated.

| Part | Qty | Have | Notes |
|---|---|---|---|
| Robots beyond the first | N − 1 | buy | Size N by how much lawn the swarm covers |
| Docks | 1 per robot, or a shared one | buy | Decided in this stage |

## Tasks

- [ ] Define the shared lawn boundary and the zone-split logic across all robots
- [ ] Run coordinated coverage with blades on
- [ ] Verify no-overlap and no-collision behavior under real conditions
- [ ] Verify every robot returns to dock at low battery or on job completion

## Exit test

The swarm mows the full mapped area with no missed sections and no collisions. Every robot ends the run docked and charging.
