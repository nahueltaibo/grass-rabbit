[← Back to plan](README.md)

# 08 — Swarm comms

Get two or more robots talking to each other and to a shared broker. Bench-testable with two bare ESP32-S3 boards before full robots exist.

Depends on: [01](01-power-and-core-electronics.md).

## BOM

| Part | Qty | Have | Notes |
|---|---|---|---|
| ESP32-S3 dev board | 1 | buy | Second peer for the bench test. A third comes from the base bridge in [04](04-rtk-positioning.md) |
| MQTT broker host (PC or Raspberry Pi running Mosquitto) | 1 | check | |
| WiFi access point | 1 | check | |

## Tasks

- [ ] Set up ESP-NOW peer discovery between two boards, measure beacon exchange latency
- [ ] Add an MQTT client on each robot, publish telemetry to a shared broker
- [ ] Implement a simple zone-claim message — first robot to claim a zone owns it
- [ ] Implement a collision-avoidance beacon — a robot backs off when a peer reports itself within a defined distance

## Exit test

Two robots exchange ESP-NOW beacons and MQTT telemetry reliably. A robot backs off correctly when a simulated peer beacon reports it's too close.
