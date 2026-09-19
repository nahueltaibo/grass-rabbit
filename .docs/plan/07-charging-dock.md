[← Back to plan](README.md)

# 07 — Charging dock

The robot finds, docks at and charges from its own base station without help.

Depends on: [02](02-drive-subsystem.md), [04](04-rtk-positioning.md).

## Tasks

- [ ] Build the dock: IR emitter beacon, spring-loaded pogo-pin contacts, dock-side charge controller
- [ ] Implement RTK-guided approach toward the dock's known coordinate
- [ ] Implement IR homing for final-meter alignment once RTK gets it close
- [ ] Detect docked state with a hall-effect or limit switch, enable charging on contact
- [ ] Verify charge termination and a clean undock on command

## Exit test

The robot navigates from a distance to the dock and docks successfully from at least three different approach angles. Charging starts automatically on contact, and the robot undocks cleanly on command.
