[← Back to plan](README.md)

# 04 — RTK positioning

Get the LC29H(BA) rover to RTK fixed mode against an LC29H(BS) base station. Bench-testable — doesn't need the chassis to be drivable yet.

Depends on: [01](01-power-and-core-electronics.md).

## BOM

| Part | Qty | Have | Notes |
|---|---|---|---|
| Quectel LC29H(BA) | 1 | on hand | Rover |
| Quectel LC29H(BS) module or breakout | 1 | buy | Base station. Skip if you use an NTRIP service instead |
| Active dual-band L1+L5 GNSS puck antenna | 2 | buy | One rover, one base. Connector must match the module board |
| TXS0104-class 2.8 V ↔ 3.3 V level shifter breakout | 1 | buy | Skip if your LC29H board already shifts |
| ESP32-S3 dev board | 1 | buy | Base-station bridge: forwards RTCM3 from the BS to the rover over WiFi |
| Pole or mast for the base antenna, stakes, tape measure | 1 set | check | Base needs open sky. Stakes and tape mark the known points |
| USB power for the base | 1 | check | |

## Tasks

- [ ] Wire the LC29H(BA) to the ESP32-S3 UART through the level shifter, antenna mounted with a clear sky view
- [ ] Set up the LC29H(BS) as a base station in survey-in mode, confirm RTCM3 output
- [ ] Deliver corrections to the rover over WiFi through the base-station bridge board
- [ ] Confirm RTK fixed mode is reached, convergence under 60 s per the datasheet
- [ ] Log position while walking a known distance, compare against the RTK fix delta
- [ ] Optional: synthesize a wheel-speed pulse train on the ESP32-S3 for the LC29H(BA) WHEELTICK pin, test dead reckoning through a short antenna occlusion

## Exit test

The rover reaches RTK fixed mode outdoors with open sky. Reported position matches the datasheet's <10 cm + 1 ppm spec when checked against two known points. If the optional dead-reckoning experiment was run, it holds a sane position through a brief antenna occlusion.
