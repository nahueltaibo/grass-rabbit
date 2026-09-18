"""Push parts to the OCP CAD Viewer in VS Code.

    python show.py              # everything, in assembly position
    python show.py base_plate   # just one
    python show.py --spread     # pulled apart, for looking at one at a time

Open the viewer first: Ctrl+Shift+P -> "OCP CAD Viewer: Open viewer".
"""

import socket
import sys

from build123d import Pos

from build import PARTS

PORT = 3939
SPACING = 200  # mm between parts when spread


def viewer_is_up() -> bool:
    with socket.socket() as s:
        s.settimeout(0.3)
        return s.connect_ex(("127.0.0.1", PORT)) == 0


def main(argv: list[str]) -> int:
    spread = "--spread" in argv
    names = [a for a in argv if not a.startswith("-")]

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
    parts = [PARTS[n]() for n in names]
    if spread:
        parts = [Pos(i * SPACING, 0, 0) * p for i, p in enumerate(parts)]

    show(*parts, names=names)
    print(f"sent to viewer: {', '.join(names)}{' (spread)' if spread else ''}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
