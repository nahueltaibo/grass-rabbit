[← Back to plan](README.md)

# 02 — Drive subsystem

Get the robot moving: motors, drivers and encoders mounted in the new chassis, driven by teleop.

Depends on: [00](00-chassis-redesign.md), [01](01-power-and-core-electronics.md).

## BOM

| Part | Qty | Have | Notes |
|---|---|---|---|
| BTS7960 H-bridge module | 2 | buy | One per drive motor |
| JGB37-520 gearmotor with Hall encoder, 12 V | 2 | from 00 | Bought in [00](00-chassis-redesign.md). Encoder powered from 3.3 V |
| 0.1 µF ceramic capacitors | 4 | buy | Across each motor's terminals, cuts brush noise that later hurts the GNSS |
| 16–18 AWG silicone wire, connectors | 1 set | check | |
| Phone or BLE gamepad | 1 | check | Teleop controller |

## Tasks

- [ ] Wire the BTS7960 drivers to the motors and to ESP32-S3 PWM/direction pins
- [ ] Solder a 0.1 µF ceramic capacitor across each motor's terminals
- [ ] Wire each encoder's A/B channels to ESP32-S3 pulse counters, confirm counts increment with rotation and reverse with direction
- [ ] Implement a teleop control loop (WiFi joystick, or BLE gamepad as the fallback from 01)
- [ ] Implement closed-loop speed control using encoder feedback, so both wheels track the same commanded speed
- [ ] Wire a software e-stop command that cuts both motors instantly

## Exit test

The robot drives forward, backward and turns on command, holds a straight line under closed-loop control, and a measured rolled distance matches the encoder count within a set tolerance. The e-stop command halts motion immediately.
