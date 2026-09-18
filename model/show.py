"""Push parts to the OCP CAD Viewer in VS Code.

    python show.py              # everything, spread out so nothing overlaps
    python show.py base_plate   # just one, at the origin

Open the viewer first: Ctrl+Shift+P -> "OCP CAD Viewer: Open viewer".
"""

import socket
import sys

from build123d import Pos

from build import PARTS

PORT = 3939
SPACING = 110  # mm between parts, enough to clear the base plate


def viewer_is_up() -> bool:
    with socket.socket() as s:
        s.settimeout(0.3)
        return s.connect_ex(("127.0.0.1", PORT)) == 0


def main(names: list[str]) -> int:
    unknown = [n for n in names if n not in PARTS]
    if unknown:
        print(f"unknown part(s): {', '.join(unknown)}", file=sys.stderr)
        print(f"available: {', '.join(PARTS)}", file=sys.stderr)
        return 1

    if not viewer_is_up():
        print(f"No viewer on port {PORT}.", file=sys.stderr)
        print('In VS Code: Ctrl+Shift+P -> "OCP CAD Viewer: Open viewer"', file=sys.stderr)
        return 1

    from ocp_vscode import show

    names = names or list(PARTS)
    parts = [Pos(i * SPACING, 0, 0) * PARTS[n]() for i, n in enumerate(names)]
    show(*parts, names=names)
    print(f"sent to viewer: {', '.join(names)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
