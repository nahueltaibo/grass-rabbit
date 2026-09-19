[← Back to plan](README.md)

# 08 — Swarm comms

Get two or more robots talking to each other and to a shared broker. Bench-testable with two bare ESP32-S3 boards before full robots exist.

Depends on: [01](01-power-and-core-electronics.md).

## Tasks

- [ ] Set up ESP-NOW peer discovery between two boards, measure beacon exchange latency
- [ ] Add an MQTT client on each robot, publish telemetry to a shared broker
- [ ] Implement a simple zone-claim message — first robot to claim a zone owns it
- [ ] Implement a collision-avoidance beacon — a robot backs off when a peer reports itself within a defined distance

## Exit test

Two robots exchange ESP-NOW beacons and MQTT telemetry reliably. A robot backs off correctly when a simulated peer beacon reports it's too close.
