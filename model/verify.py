"""Check the ported parts against the legacy Fusion geometry.

    python verify.py

Compares hole counts, diameters and positions with the STEP files in
.docs/legacy-models/. Catches the quiet failures -- a feature placed at the
origin, a sketch extruded the wrong way -- that a bounding box still passes.
"""

import sys
from pathlib import Path

from build123d import Pos, Rectangle

from build import PARTS
from params import BULKHEAD_W, NOSE_BACK_HALF_W, NOSE_BACK_Y

LEGACY = Path(__file__).parents[1] / ".docs" / "legacy-models" / "Robot+Mower+3.stp"

# (part, legacy body id, expected X, Y, Z extent in mm)
ENVELOPES = [
    ("base_plate", 160.0, 159.9, 11.0),
    ("nose_plate", 159.85, 84.9, 11.0),
]

# Holes measured off the legacy plates: (diameter, count).
HOLES = {
    "base_plate": [(3.2, 14)],
    "nose_plate": [(3.2, 4), (5.0, 4)],
}

TOL = 0.05


def cylinder_holes(part):
    """Count distinct hole diameters from the part's cylindrical faces."""
    from collections import Counter

    found = Counter()
    for f in part.faces():
        if str(f.geom_type) != "GeomType.CYLINDER":
            continue
        r = f.radius if hasattr(f, "radius") else None
        if r:
            found[round(r * 2, 2)] += 1
    return found


def main() -> int:
    failures = []

    for name, ex, ey, ez in ENVELOPES:
        size = PARTS[name]().bounding_box().size
        for axis, got, want in (("X", size.X, ex), ("Y", size.Y, ey), ("Z", size.Z, ez)):
            if abs(got - want) > TOL:
                failures.append(f"{name}: {axis} is {got:.2f}, legacy is {want:.2f}")

    for name, expected in HOLES.items():
        found = cylinder_holes(PARTS[name]())
        for dia, count in expected:
            got = found.get(dia, 0)
            if got != count:
                failures.append(f"{name}: {got} holes at Ø{dia}, expected {count}")

    # Both plates must sit on z=0 and rise to the bulkhead -- an inverted
    # extrude still yields the right size, just in the wrong place.
    for name in ("base_plate", "nose_plate"):
        bb = PARTS[name]().bounding_box()
        if abs(bb.min.Z) > TOL:
            failures.append(f"{name}: sits at z={bb.min.Z:.2f}, should start at 0")

    # The nose bulkhead follows the trapezoid's diagonals rather than
    # overhanging them. These are the legacy Y=8 face corners.
    from parts.nose_plate import outline

    strip = Pos(0, NOSE_BACK_Y - BULKHEAD_W / 2) * Rectangle(
        2 * NOSE_BACK_HALF_W, BULKHEAD_W
    )
    got = sorted((round(v.X, 2), round(v.Y, 2)) for v in (outline() & strip).vertices())
    want = sorted(
        [(-79.92, -80.1), (-76.59, -84.45), (76.59, -84.45), (79.92, -80.1)]
    )
    if got != want:
        failures.append(f"nose bulkhead corners {got}, legacy has {want}")

    if not LEGACY.exists():
        print(f"note: legacy reference missing at {LEGACY}", file=sys.stderr)

    for f in failures:
        print("FAIL", f)
    if failures:
        return 1
    print(f"ok - {len(ENVELOPES)} envelopes, {sum(len(v) for v in HOLES.values())} hole groups")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
