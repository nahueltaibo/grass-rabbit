[← Back to plan](README.md)

# 04 — RTK positioning

Get the LC29H(BA) rover to RTK fixed mode against an LC29H(BS) base station. Bench-testable — doesn't need the chassis to be drivable yet.

Depends on: [01](01-power-and-core-electronics.md).

## Tasks

- [ ] Wire the LC29H(BA) to the ESP32-S3 UART, antenna mounted with a clear sky view
- [ ] Set up the LC29H(BS) as a base station in survey-in mode, confirm RTCM3 output
- [ ] Deliver corrections to the rover (direct wire or WiFi bridge is fine for this bench test)
- [ ] Confirm RTK fixed mode is reached, convergence under 60 s per the datasheet
- [ ] Log position while walking a known distance, compare against the RTK fix delta
- [ ] Wire the AS5600 wheel-tick output into the LC29H(BA) WHEELTICK pin, confirm dead reckoning bridges a short antenna occlusion

## Exit test

The rover reaches RTK fixed mode outdoors with open sky. Reported position matches the datasheet's <10 cm + 1 ppm spec when checked against two known points. Dead reckoning holds a sane position through a brief antenna occlusion test.
