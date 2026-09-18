"""The main deck. Everything else bolts to this.

Ported from the legacy Base Plate: outline, keyhole, bulkhead lip and all
fourteen M3 holes are measured, not invented.
"""

from build123d import *

from params import (
    BASE_BACK_Y,
    BASE_FRONT_Y,
    BASE_HOLES,
    BASE_W,
    BULKHEAD_H,
    BULKHEAD_W,
    CUTTER_BORE_D,
    CUTTER_SLOT_D,
    CUTTER_SLOT_Y,
    LINK_BCD,
    LINK_BOLT_COUNT,
    LINK_BOLT_START,
    M3_CLEARANCE,
    PLATE_T,
)


def keyhole() -> Sketch:
    """Cutter bore plus a slot running forward to a rounded end. The slot walls
    leave the bore tangentially, which is what makes the widths line up."""
    bore = Circle(CUTTER_BORE_D / 2)
    end = Pos(0, CUTTER_SLOT_Y) * Circle(CUTTER_SLOT_D / 2)
    throat = Pos(0, CUTTER_SLOT_Y / 2) * Rectangle(CUTTER_SLOT_D, abs(CUTTER_SLOT_Y))
    return bore + end + throat


def base_plate() -> Part:
    length = BASE_BACK_Y - BASE_FRONT_Y
    mid_y = (BASE_BACK_Y + BASE_FRONT_Y) / 2

    deck = Pos(0, mid_y) * Rectangle(BASE_W, length)
    deck -= keyhole()
    for x, y in BASE_HOLES:
        deck -= Pos(x, y) * Circle(M3_CLEARANCE / 2)
    for loc in PolarLocations(LINK_BCD / 2, LINK_BOLT_COUNT, start_angle=LINK_BOLT_START):
        deck -= loc * Circle(M3_CLEARANCE / 2)

    plate = extrude(deck, PLATE_T)

    # Transverse bulkhead along the front edge. Its other half sits on the nose
    # plate; together they make one continuous wall at the joint.
    lip = Pos(0, BASE_FRONT_Y + BULKHEAD_W / 2) * Rectangle(BASE_W, BULKHEAD_W)
    plate += Pos(0, 0, PLATE_T) * extrude(lip, BULKHEAD_H)

    return plate
