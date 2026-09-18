"""The motor mounting interface, shared by every motor mount on the robot.

Replaces the `Motor Template` XRef from the Fusion design. Change it here and
every mount that calls it follows.
"""

from build123d import *

from params import (
    MOTOR_BOLT_BCD,
    MOTOR_BOLT_COUNT,
    MOTOR_BOLT_D,
    MOTOR_BORE_D,
    MOTOR_BORE_OFFSET,
    MOTOR_FLANGE_D,
)


def motor_cutout(depth: float) -> Part:
    """The solid to subtract from a plate to mount a motor: shaft bore plus
    bolt holes. `depth` should comfortably exceed the plate thickness."""
    bore = Pos(0, MOTOR_BORE_OFFSET) * Cylinder(MOTOR_BORE_D / 2, depth)
    bolts = [
        loc * Cylinder(MOTOR_BOLT_D / 2, depth)
        for loc in PolarLocations(MOTOR_BOLT_BCD / 2, MOTOR_BOLT_COUNT)
    ]
    result = bore
    for b in bolts:
        result += b
    return result


def motor_template(thickness: float = 0.6) -> Part:
    """The template disc itself, for checking a motor against the pattern.
    Print one before committing the pattern to a real part."""
    disc = Cylinder(MOTOR_FLANGE_D / 2, thickness)
    return disc - motor_cutout(thickness * 4)
