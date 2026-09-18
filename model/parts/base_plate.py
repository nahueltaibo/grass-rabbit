"""The main deck. Everything else bolts to this.

Minimal PoC: correct footprint, thickness, cutter clearance and a perimeter
bolt pattern. The real plate has a chamfered outline and raised bosses that
aren't reproduced yet.
"""

from build123d import *

from params import (
    CUTTER_CLEARANCE_D,
    M3_CLEARANCE,
    PLATE_D,
    PLATE_T,
    PLATE_W,
)

MOUNT_INSET = 8.0  # perimeter bolt centres, measured in from the plate edge


def base_plate() -> Part:
    plate = Box(PLATE_W, PLATE_D, PLATE_T)
    through = PLATE_T * 4

    # The cutter shaft drops through here. The motor itself hangs off the
    # Cutter Motor Link, not off this plate -- at Ø31 BCD the mounting bolts
    # would break straight into this hole.
    plate -= Cylinder(CUTTER_CLEARANCE_D / 2, through)

    x = PLATE_W / 2 - MOUNT_INSET
    y = PLATE_D / 2 - MOUNT_INSET
    holes = [(sx * x, sy * y) for sx in (-1, 1) for sy in (-1, 1)]
    holes += [(0, y), (0, -y), (x, 0), (-x, 0)]
    for hx, hy in holes:
        plate -= Pos(hx, hy) * Cylinder(M3_CLEARANCE / 2, through)

    return plate
