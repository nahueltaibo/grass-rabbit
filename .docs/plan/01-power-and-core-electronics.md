[← Back to plan](README.md)

# 01 — Power and core electronics

Bring the battery, BMS and ESP32-S3 up on the bench, independent of the chassis. This is where a wiring mistake is cheapest to find.

Depends on: nothing. Runs in parallel with [00](00-chassis-redesign.md).

## BOM

| Part | Qty | Have | Notes |
|---|---|---|---|
| ESP32-S3 dev board (N16R8, dual USB-C) | 1 | buy | Pin notes in [hardware-bom.md](../hardware-bom.md) |
| 18650 Li-ion cells | 3 in series (3S) | buy | Matches the 12 V gearmotors |
| Cell holders, or a pre-built pack | 1 | buy | |
| BMS matching the cell count, ≥20 A | 1 | buy | |
| Bench Li-ion charger for that cell count | 1 | buy | Until the dock exists in [07](07-charging-dock.md) |
| Main switch | 1 | on hand | From the current build |
| XT60 connector pair | 1 | on hand | From the current build |
| Fuse holder + blade fuse | 1 | buy | Rated above the motors' stall current |
| 5 V buck regulator, ≥3 A | 1 | buy | |
| USB-C cable, breadboard, jumper wires, multimeter | 1 set | check | Bench tools |

## Tasks

- [ ] Assemble the Li-ion pack and BMS, verify over-discharge protection trips at a safe test current
- [ ] Wire the main switch and fuse
- [ ] Verify the 5 V logic rail holds under load, separate from the motor power rail
- [ ] Flash minimal firmware to the ESP32-S3, confirm boot over USB serial
- [ ] Join WiFi, confirm telemetry reaches a test MQTT broker
- [ ] Confirm BLE advertises (kept as a teleop fallback, no gamepad pairing yet)

## Exit test

Battery → BMS → regulator → ESP32-S3 powers up cleanly on the bench. The board joins WiFi and publishes a test telemetry message. BLE is visible to a phone. None of this is mounted in the chassis yet.
