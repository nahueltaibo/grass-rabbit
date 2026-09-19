# Grass Rabbit — Hardware BOM

Spec and rationale for the electronics. What to buy, and when, lives in each stage's BOM section — start at the [plan index](plan/README.md). The mechanical BOM (bearings, fasteners, caster, blade) stays in `model/` per the project status doc.

Everything here assumes DC brushed drive motors, which are already on hand.

## Compute & connectivity

| Part | Spec | Qty | Notes |
|---|---|---|---|
| ESP32-S3 dev board | ESP32-S3-WROOM-1, dual USB-C (CH343P UART + native USB), dual-core LX7, WiFi + BLE 5 | 1 per robot, +1 base-station bridge, +1 dock | Fits the project: ESP-NOW, hardware pulse counters for encoders, MCPWM, two I2C buses, three UARTs. Datasheet in [datasheets/](datasheets/). |

Board pin gotchas, from the datasheet pin map:

- GPIO are 3.3 V only, not 5 V tolerant. Power in through the 5V pin or USB.
- The datasheet title says N8R2/N16R8, the photo says N16R8. Check the module label. On N16R8 (octal PSRAM) GPIO35–37 are unusable.
- Avoid strapping pins 0, 3, 45, 46 and the USB pins 19/20 for general I/O.

## Positioning — RTK GNSS

| Part | Spec | Qty | Notes |
|---|---|---|---|
| Quectel LC29H(BA) | DR+RTK rover, autonomous 1 m / RTK <10 cm + 1 ppm, 3.1–3.6 V supply | 1 per robot (1 on hand) | I/O is 2.8 V. Module inputs max out at 3.08 V, so the ESP32-S3's 3.3 V outputs need level shifting. Quectel's reference design uses a diode/transistor shifter, or a TXS0104. Skip it only if your breakout board already shifts. Feed VCC from an LDO, not a switcher. |
| Quectel LC29H(BS) | RTK base station variant, outputs RTCM3 | 1 (shared across swarm) | BA is rover-only. Base mode needs this separate SKU, or an NTRIP subscription instead. |
| Active GNSS antenna | Dual-band L1+L5, RHCP, puck style | 1 per rover + 1 for base | Puck antennas carry their own ground plane, so no chassis metal plate. Passive is fine only within 1 m of the module. |

The BA's internal IMU is not usable as a tilt sensor. The datasheet marks its raw IMU output and the WI warning pin as under development.

## Motion

| Part | Spec | Qty | Notes |
|---|---|---|---|
| BTS7960 H-bridge module | 43 A, brushed DC | 1 per motor (2 drive, +1 blade if brushed) | One module drives one motor. 3.3 V logic inputs usually work, confirm on your board. |
| JGB37-520 gearmotor with Hall encoder | 12 V, 37 mm metal gearbox, quadrature encoder (~11 pulses per channel at the motor shaft) | 2 | Same Ø31 mm six-hole pattern as the old motor pocket. Pick the no-load rpm from the wheel diameter: ~70 rpm at Ø160 mm, ~90 rpm at Ø130 mm. Want ≥4 kg·cm rated torque at that speed. Power the encoder from 3.3 V. The ESP32-S3's pulse counters read it in hardware. Move to a JGB37-545 if the robot ends up heavier than ~3 kg. |

**LC29H WHEELTICK.** The BA has one wheel-tick input for a whole vehicle, and this robot has two wheels. Feeding it means the ESP32-S3 synthesizes a speed pulse train from the average of both wheels. The DR application note that defines the pulse scaling isn't in `datasheets/`. Treat it as an optional experiment in iteration 04, not a dependency.

## Safety

| Part | Spec | Qty | Notes |
|---|---|---|---|
| MPU-6050 (GY-521) | 6-axis accel + gyro, I2C | 1 | Roughly $2–3. Pitch/roll from a complementary or Madgwick filter is enough for a tilt cutoff. |
| Ball tilt switch | Mechanical, normally closed | 1 | Roughly $1. Wired into the e-stop chain so tilt kills the blade with no MCU involved. |
| Microswitch bumpers | Existing hardware | 2 | Already on the robot. |
| INA226 current sensor | I2C, blade motor line | 1 | Jam/stall detection. |
| E-stop button + relay | NC mushroom button, 30 A automotive relay | 1 each | Blade line only, independent of MCU state. |

Cheaper-than-BNO085 IMU options, cheapest first: MPU-6050 (~$2–3), BMI270 or ICM-42688-P breakout (~$6–10, lower gyro noise), BNO055 (~$15+, onboard fusion). Heading has no magnetometer on any of these, so yaw comes from RTK course-over-ground plus gyro between fixes.

## Power

| Part | Spec | Qty | Notes |
|---|---|---|---|
| 18650 Li-ion pack | 3S, matches the 12 V gearmotors | 1 | Li-ion over LiPo for unattended daily charging safety. |
| BMS | Charge-current limiting, matched to pack | 1 | |
| Buck regulator | 5 V, ≥3 A, separate from motor power | 1 | Logic supply. |
| Dock-side charge controller | CC/CV for the pack's cell count | 1 | Lives in the dock, not the robot. |

## Autonomous charging dock

| Part | Spec | Qty | Notes |
|---|---|---|---|
| IR emitter/receiver pair | 38 kHz modulated beacon, Roomba-style | 1 pair | Final-meter homing after RTK gets it close. |
| Pogo-pin contacts | Spring-loaded, funnel-guided | 1 set | Charge connection, tolerant of misalignment. |
| Hall-effect or limit switch | Docked-state confirmation | 1 | Gates charge enable. |

## Swarm comms

ESP-NOW (built into the ESP32-S3) for robot-to-robot, WiFi + MQTT for telemetry. No extra hardware beyond a shared broker on a home server or Pi.

## Open items

- **Wheel diameter and robot mass**: set the gearmotor's rpm and whether the JGB37-520 has enough torque. Weigh the robot with battery and blade motor. Over ~3 kg, or slopes above ~15°, move to the JGB37-545.
- **Swarm size**: sets how many robots' worth of parts to buy. One LC29H(BS) base covers any count.
- **FWD pin**: left unconnected on the BA. Quectel only requires it for 4-wheel vehicles.
