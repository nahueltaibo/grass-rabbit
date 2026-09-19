[← Back to plan](README.md)

# 05 — Single-robot autonomy

One robot combines drive, safety and RTK positioning to follow waypoints and hold a boundary on its own. Blades stay off — this iteration is about navigation, not cutting.

Depends on: [02](02-drive-subsystem.md), [03](03-safety-subsystem.md), [04](04-rtk-positioning.md).

## Tasks

- [ ] Fuse encoder, IMU and RTK readings into a single position/heading estimate
- [ ] Implement waypoint-follow: drive to a list of RTK coordinates in sequence
- [ ] Implement a boundary check that stops or turns the robot before it leaves a defined polygon
- [ ] Field test on the actual lawn, blades off, safety cutoffs from 03 active throughout

## Exit test

The robot autonomously visits a short waypoint loop and stays inside a marked boundary on the real lawn. Every safety cutoff from [03](03-safety-subsystem.md) still fires correctly during autonomous drive.
