"""Build every part and write STEP + STL into build/.

    python build.py            # everything
    python build.py base_plate # one part
"""

import sys
from pathlib import Path

from build123d import export_step, export_stl

from parts.base_plate import base_plate
from parts.cutter_motor_link import cutter_motor_link
from parts.motor_template import motor_template

PARTS = {
    "base_plate": base_plate,
    "cutter_motor_link": cutter_motor_link,
    "motor_template": motor_template,
}

OUT = Path(__file__).parent / "build"


def main(names: list[str]) -> int:
    OUT.mkdir(exist_ok=True)
    unknown = [n for n in names if n not in PARTS]
    if unknown:
        print(f"unknown part(s): {', '.join(unknown)}", file=sys.stderr)
        print(f"available: {', '.join(PARTS)}", file=sys.stderr)
        return 1

    for name in names or PARTS:
        part = PARTS[name]()
        export_step(part, str(OUT / f"{name}.step"))
        export_stl(part, str(OUT / f"{name}.stl"))
        bb = part.bounding_box()
        size = bb.size
        print(f"{name:16s} {size.X:7.2f} x {size.Y:7.2f} x {size.Z:7.2f} mm")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
