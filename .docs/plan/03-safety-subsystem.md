[← Back to plan](README.md)

# 03 — Safety subsystem

Wire the bumpers, tilt/lift cutoff, hardware e-stop and watchdog into the drive loop built in [02](02-drive-subsystem.md). This is the gate everything after it has to pass through — no autonomy and no blade until this holds.

Depends on: [02](02-drive-subsystem.md).

## Tasks

- [ ] Wire the existing bumper microswitches to ESP32-S3 interrupts, confirm each side reports independently
- [ ] Mount the BNO085, confirm pitch/roll readout matches physical tilt
- [ ] Implement tilt/lift cutoff — drive motors stop above a threshold angle
- [ ] Wire the hardware e-stop relay on the blade line, independent of the MCU (blade motor isn't mounted yet — bench-test relay continuity with a multimeter)
- [ ] Implement a watchdog that stops drive if the control loop stalls, and verify it with a simulated hang

## Exit test

Tilting the chassis past the threshold angle stops the drive motors within a defined time budget. Either bumper triggers a stop. The e-stop relay is confirmed with a multimeter to cut the blade power path. A simulated control-loop stall trips the watchdog and stops motion.
