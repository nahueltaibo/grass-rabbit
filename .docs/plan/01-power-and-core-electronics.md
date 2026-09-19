[← Back to plan](README.md)

# 01 — Power and core electronics

Bring the battery, BMS and ESP32-S3 up on the bench, independent of the chassis. This is where a wiring mistake is cheapest to find.

Depends on: nothing. Runs in parallel with [00](00-chassis-redesign.md).

## Tasks

- [ ] Assemble the Li-ion pack and BMS, verify over-discharge protection trips at a safe test current
- [ ] Wire the main switch and fuse
- [ ] Verify the 5 V logic rail holds under load, separate from the motor power rail
- [ ] Flash minimal firmware to the ESP32-S3, confirm boot over USB serial
- [ ] Join WiFi, confirm telemetry reaches a test MQTT broker
- [ ] Confirm BLE advertises (kept as a teleop fallback, no gamepad pairing yet)

## Exit test

Battery → BMS → regulator → ESP32-S3 powers up cleanly on the bench. The board joins WiFi and publishes a test telemetry message. BLE is visible to a phone. None of this is mounted in the chassis yet.
