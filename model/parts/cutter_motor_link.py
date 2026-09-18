"""Carries the cutter motor and bolts to the underside of the base plate.

This is the part that consumes the shared motor pattern, which is the whole
point of keeping that pattern in one place. The Fusion design has a component
by this name but it ships with no solid, so this is a first cut, not a port.
"""

from build123d import *

from params import M3_CLEARANCE, MOTOR_FLANGE_D
from parts.motor_template import motor_cutout

LINK_T = 4.0
LINK_MARGIN = 6.0  # material left outside the motor flange
FIXING_BCD = MOTOR_FLANGE_D + 2 * LINK_MARGIN - 6.0


def cutter_motor_link() -> Part:
    body = Cylinder((MOTOR_FLANGE_D + 2 * LINK_MARGIN) / 2, LINK_T)
    through = LINK_T * 4

    body -= motor_cutout(through)

    # Three bolts up into the base plate, clocked off the motor pattern.
    for loc in PolarLocations(FIXING_BCD / 2, 3, start_angle=30):
        body -= loc * Cylinder(M3_CLEARANCE / 2, through)

    return body
