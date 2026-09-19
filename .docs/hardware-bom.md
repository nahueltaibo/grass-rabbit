# Grass Rabbit — Hardware BOM

Electronics and sensor BOM for the from-scratch rover redesign. Mechanical BOM (motors, bearings, fasteners, caster, blade) stays in `model/` per the project status doc — this covers compute, sensing, power, and swarm.

Prices are rough, hobbyist-quantity USD. Everything here assumes DC brushed drive motors (confirmed — already on hand).

## Compute & connectivity

| Part | Spec | Qty | Notes |
|---|---|---|---|
| ESP32-S3 dev board | Dual radio, WiFi + BLE, plenty of GPIO | 1 | Runs the safety loop, drive control, swarm comms |

## Positioning — RTK GNSS

| Part | Spec | Qty | Notes |
|---|---|---|---|
| Quectel LC29H(BA) | AG3335A/T chipset, DR+RTK rover, autonomous 1 m / RTK <10 cm + 1 ppm, built-in 6-axis IMU fused with wheel-tick input for DR | 1 per robot (1 on hand) | UART to ESP32-S3, 3.3 V logic, no level shifter needed |
| Quectel LC29H(BS) | RTK base station variant — outputs RTCM3 corrections | 1 (shared across swarm) | Confirmed via datasheet: BA is rover-only, base mode needs the separate BS SKU |
| Active GNSS antenna (puck, magnetic or screw mount) | Dual-band L1+L5, RHCP, integrated ground plane | 1 per rover + 1 for base | Puck antennas carry their own ground plane — no chassis metal plate needed. Passive antenna is fine only if it sits <1 m from the module; active is required beyond that |

## Motion

| Part | Spec | Qty | Notes |
|---|---|---|---|
| BTS7960 dual H-bridge module | 43 A per channel, brushed DC | 1 per wheel (2 total) | Motors confirmed on hand — DC brushed |
| AS5600 magnetic shaft encoder | 12-bit, I2C/PWM, contactless | 1 per drive motor (2 total) | Closed-loop speed control on the ESP32-S3, and pulse output fans out to the LC29H(BA) WHEELTICK pin so the module's own DR fusion gets real wheel-tick data instead of IMU-only |

## Safety

| Part | Spec | Qty | Notes |
|---|---|---|---|
| BNO085 IMU | Onboard sensor fusion, direct pitch/roll output | 1 | Tilt/lift cutoff — separate from the GNSS module's DR-oriented IMU |
| Microswitch bumpers | Existing hardware | 2 | Already on the robot |
| INA226 current sensor | I2C, blade motor line | 1 | Jam/stall detection |
| E-stop relay | Hardware-latched, blade line only | 1 | Kills blade power independent of MCU state |

## Power

| Part | Spec | Qty | Notes |
|---|---|---|---|
| 18650 Li-ion pack | 3S or 4S, sized to motor + blade draw | 1 | Li-ion over LiPo for unattended daily charging safety |
| BMS | Charge-current limiting, matched to pack | 1 | |
| Buck regulator | 5 V rail, separate from motor power | 1 | Logic supply |
| Dock-side charge controller | CC/CV, BQ25798-class or proven 3S/4S smart charger | 1 | Lives in the dock, not the robot |

## Autonomous charging dock

| Part | Spec | Qty | Notes |
|---|---|---|---|
| IR emitter/receiver pair | Roomba-style homing beacon | 1 pair | Final-meter homing after RTK gets it close |
| Pogo-pin contacts | Spring-loaded, funnel-guided | 1 set | Charge connection, tolerant of misalignment |
| Hall-effect or limit switch | Docked-state confirmation | 1 | Gates charge enable |

## Swarm comms

| Part | Spec | Qty | Notes |
|---|---|---|---|
| — | ESP-NOW (built into ESP32-S3) for robot-to-robot | — | No router needed, collision-avoidance beacons |
| — | WiFi STA + MQTT for telemetry/dashboard | — | Shared broker on a home server or Pi |

## Open items

- **Swarm size**: how many robots determines how many LC29H(BA) rover modules and BTS7960/AS5600/motor sets to buy — one LC29H(BS) base station covers the whole swarm regardless of count.
- **FWD pin**: left N/C on the LC29H(BA). It's only needed for 4-wheel vehicles per Quectel's hardware design doc — this is a 2-wheel differential-drive mower.
