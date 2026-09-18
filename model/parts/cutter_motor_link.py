"""Carries the cutter motor and bolts to the underside of the base plate.

This is the part that consumes the shared motor pattern, which is the whole
point of keeping that pattern in one place. The Fusion design has a component
by this name but it ships with no solid, so this is a first cut, not a port.
"""

from build123d import *

from params import LINK_BCD, LINK_BOLT_COUNT, LINK_BOLT_START, M3_CLEARANCE, MOTOR_FLANGE_D
from parts.motor_template import motor_cutout

LINK_T = 4.0
LINK_MARGIN = 6.0  # material left outside the motor flange


def cutter_motor_link() -> Part:
    body = Cylinder((MOTOR_FLANGE_D + 2 * LINK_MARGIN) / 2, LINK_T)
    through = LINK_T * 4

    body -= motor_cutout(through)

    # Bolts up into the base plate. This pattern is the plate's, not the
    # motor's -- adapting between the two is the whole job of this part.
    for loc in PolarLocations(LINK_BCD / 2, LINK_BOLT_COUNT, start_angle=LINK_BOLT_START):
        body -= loc * Cylinder(M3_CLEARANCE / 2, through)

    return body
