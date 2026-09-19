[← Back to plan](README.md)

# 02 — Drive subsystem

Get the robot moving: motors, drivers and encoders mounted in the new chassis, driven by teleop.

Depends on: [00](00-chassis-redesign.md), [01](01-power-and-core-electronics.md).

## Tasks

- [ ] Wire the BTS7960 drivers to the motors and to ESP32-S3 PWM/direction pins
- [ ] Mount the AS5600 encoders on both motor shafts, confirm I2C counts increment with rotation
- [ ] Implement a teleop control loop (WiFi joystick, or BLE gamepad as the fallback from 01)
- [ ] Implement closed-loop speed control using encoder feedback, so both wheels track the same commanded speed
- [ ] Wire a software e-stop command that cuts both motors instantly

## Exit test

The robot drives forward, backward and turns on command, holds a straight line under closed-loop control, and a measured rolled distance matches the encoder count within a set tolerance. The e-stop command halts motion immediately.
