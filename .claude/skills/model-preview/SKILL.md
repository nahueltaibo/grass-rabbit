---
name: model-preview
description: Use after editing any CAD source under model/ (params.py, parts/*.py, build.py). Rebuilds the affected part and pushes it to the OCP CAD Viewer in VS Code so the change is visible on screen. Also use when asked to show, preview, or display a part.
---

# Model preview

A geometry change nobody can see isn't finished. After editing anything under
`model/`, rebuild and push the result to the viewer in the same turn — don't
wait to be asked.

## Every time

**1. Rebuild.** Name the part to keep it quick; omit it to build everything.

```bash
python build.py base_plate
```

Run this from `model/`, using the project venv (`model/README.md` covers setup).
A traceback here means the change is broken — fix it before going further.

**2. Check whether the viewer is listening.** It sits on port 3939.

```bash
python -c "import socket;s=socket.socket();s.settimeout(0.3);print('up' if s.connect_ex(('127.0.0.1',3939))==0 else 'down')"
```

**3a. If it's up, push the part.**

```python
from ocp_vscode import show
from parts.base_plate import base_plate
show(base_plate(), name="base_plate")
```

Push every part you touched, not just the last one. `show_all()` is fine when
several changed.

**3b. If it's down, say so in one line** and give the user the fix:

> Open the viewer: Ctrl+Shift+P → **OCP CAD Viewer: Open viewer**

Then carry on. A viewer that isn't running is not a reason to stop working, and
not a reason to keep retrying the connection.

## Report what changed

State the dimensions that moved, from the `build.py` output — bounding boxes are
already printed. "Plate is now 170 × 164.5 × 3" beats "updated the plate".

## Notes

- The viewer needs the **OCP CAD Viewer** VS Code extension installed once.
  If port 3939 is down and the user says the extension isn't installed, point
  them at the Extensions panel rather than debugging it further.
- `show()` replaces what's on screen; `show_all()` sends everything in scope.
- FreeCAD opens the exported `build/*.step` for measuring or a second opinion.
  It's a fallback, not the loop — the viewer is faster and needs no file open.
