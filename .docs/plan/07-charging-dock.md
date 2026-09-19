[← Back to plan](README.md)

# 07 — Charging dock

The robot finds, docks at and charges from its own base station without help.

Depends on: [02](02-drive-subsystem.md), [04](04-rtk-positioning.md).

## BOM

| Part | Qty | Have | Notes |
|---|---|---|---|
| ESP32-S3 dev board | 1 | buy | Dock supervisor: IR beacon, charge switching, MQTT status |
| 940 nm IR LEDs | 3 | buy | Dock side, driven at 38 kHz |
| TSOP38238-class IR receivers | 3 | buy | Robot side: left, centre, right |
| High-current pogo pins | 2 | buy | Dock side |
| Brass or stainless contact pads | 2 | buy | Robot side |
| Hall sensor (A3144) + small magnet | 1 | buy | Docked-state detect |
| CC/CV charger supply for the pack, ≥2 A | 1 | buy | 12.6 V for the 3S pack |
| MOSFET or relay for the charge contacts | 1 | buy | Keeps the contacts dead until docked |
| Reverse-polarity protection diode | 1 | buy | |
| Outdoor enclosure for the dock electronics | 1 | check | |

## Tasks

- [ ] Build the dock: IR emitter beacon, spring-loaded pogo-pin contacts, dock-side charge controller
- [ ] Implement RTK-guided approach toward the dock's known coordinate
- [ ] Implement IR homing for final-meter alignment once RTK gets it close
- [ ] Detect docked state with a hall-effect or limit switch, enable charging on contact
- [ ] Verify charge termination and a clean undock on command

## Exit test

The robot navigates from a distance to the dock and docks successfully from at least three different approach angles. Charging starts automatically on contact, and the robot undocks cleanly on command.
