"""The front plate. Carries the swivel caster and tapers towards the nose."""

from build123d import *

from params import (
    BULKHEAD_H,
    BULKHEAD_W,
    CASTER_HOLES,
    CASTER_HOLE_D,
    M3_CLEARANCE,
    NOSE_BACK_HALF_W,
    NOSE_BACK_Y,
    NOSE_HOLES,
    NOSE_TIP_HALF_W,
    NOSE_TIP_Y,
    PLATE_T,
)


def outline() -> Sketch:
    """Counter-clockwise: a clockwise winding faces the sketch normal down and
    extrudes the plate the wrong way."""
    return Polygon(
        (-NOSE_BACK_HALF_W, NOSE_BACK_Y),
        (-NOSE_TIP_HALF_W, NOSE_TIP_Y),
        (NOSE_TIP_HALF_W, NOSE_TIP_Y),
        (NOSE_BACK_HALF_W, NOSE_BACK_Y),
        align=None,
    )


def nose_plate() -> Part:
    shape = outline()

    deck = shape
    for x, y in NOSE_HOLES:
        deck -= Pos(x, y) * Circle(M3_CLEARANCE / 2)
    for x, y in CASTER_HOLES:
        deck -= Pos(x, y) * Circle(CASTER_HOLE_D / 2)

    plate = extrude(deck, PLATE_T)

    # The matching half of the bulkhead at the joint. Clipped to the outline so
    # its ends follow the taper instead of overhanging it -- from above the
    # wall's sides sit flush with the trapezoid's diagonals.
    strip = Pos(0, NOSE_BACK_Y - BULKHEAD_W / 2) * Rectangle(
        2 * NOSE_BACK_HALF_W, BULKHEAD_W
    )
    plate += Pos(0, 0, PLATE_T) * extrude(shape & strip, BULKHEAD_H)

    return plate
