[← Back to plan](README.md)

# 09 — Swarm mowing

The capstone iteration: the full swarm mows a shared lawn with zone division, blades on, and every robot returns to a dock on its own.

Depends on: [05](05-single-robot-autonomy.md), [06](06-cutting-deck.md), [07](07-charging-dock.md), [08](08-swarm-comms.md).

## Tasks

- [ ] Define the shared lawn boundary and the zone-split logic across all robots
- [ ] Run coordinated coverage with blades on
- [ ] Verify no-overlap and no-collision behavior under real conditions
- [ ] Verify every robot returns to dock at low battery or on job completion

## Exit test

The swarm mows the full mapped area with no missed sections and no collisions. Every robot ends the run docked and charging.
