[← Back to plan](README.md)

# 03 — Safety subsystem

Wire the bumpers, tilt/lift cutoff, hardware e-stop and watchdog into the drive loop built in [02](02-drive-subsystem.md). This is the gate everything after it has to pass through — no autonomy and no blade until this holds.

Depends on: [02](02-drive-subsystem.md).

## BOM

| Part | Qty | Have | Notes |
|---|---|---|---|
| MPU-6050 (GY-521) breakout | 1 | buy | Roughly $2–3. Cheaper stand-in for the BNO085 — pitch/roll only |
| Ball tilt switch, normally closed | 1 | buy | Hardware backup, wired into the e-stop chain |
| NC mushroom e-stop button | 1 | buy | |
| 30 A automotive relay + socket | 1 | buy | Blade line only |
| 1N4007 diode | 1 | buy | Flyback across the relay coil |
| Bumper microswitches | 2 | on hand | Already fitted in [00](00-chassis-redesign.md) |

## Tasks

- [ ] Wire the existing bumper microswitches to ESP32-S3 interrupts, confirm each side reports independently
- [ ] Mount the MPU-6050, run a complementary filter, confirm pitch/roll matches a phone-measured tilt
- [ ] Implement tilt/lift cutoff — drive motors stop above a threshold angle
- [ ] Wire the hardware e-stop relay on the blade line, independent of the MCU (blade motor isn't mounted yet — bench-test relay continuity with a multimeter)
- [ ] Wire the ball tilt switch and the e-stop button into the relay chain, confirm either one drops the relay with the MCU unpowered
- [ ] Implement a watchdog that stops drive if the control loop stalls, and verify it with a simulated hang

## Exit test

Tilting the chassis past the threshold angle stops the drive motors within a defined time budget. Either bumper triggers a stop. The e-stop relay is confirmed with a multimeter to cut the blade power path. A simulated control-loop stall trips the watchdog and stops motion.
