[← Back to plan](README.md)

# 06 — Cutting deck

Mount the blade motor and gate it behind every interlock built in [03](03-safety-subsystem.md). Nothing here should be able to spin the blade unless drive-side safety already agrees it's safe.

Depends on: [03](03-safety-subsystem.md).

## Tasks

- [ ] Mount the blade motor, rotor and blades per the existing mechanical design
- [ ] Wire the blade motor driver/ESC through the hardware e-stop relay from 03
- [ ] Add INA226 current sensing on the blade line
- [ ] Gate blade spin-up behind all four conditions: no tilt fault, no bumper fault, e-stop closed, explicit software command
- [ ] Bench-test stall detection — load the blade against resistance and confirm the cutoff trips

## Exit test

The blade spins only when every interlock is satisfied. Tripping any one of tilt, bumper, e-stop or watchdog stops the blade within a defined time budget. A simulated stall is detected and cuts blade power.
