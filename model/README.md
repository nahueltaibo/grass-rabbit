# Model

The robot as code. Python in, STEP and STL out.

Each part is a function that returns a solid. Run `build.py` and it writes real
B-rep geometry you can open in any CAD package. The source is diffable text, so
a change to a hole diameter shows up in `git diff` as a changed number instead
of a 1.2 MB binary blob.

## Running it

```bash
python -m venv .venv && .venv/Scripts/activate   # Windows
pip install -r requirements.txt
python build.py                                   # all parts -> build/
python build.py base_plate                        # just one
```

## What's here

| Part | Status |
|---|---|
| `base_plate` | Ported. Outline, keyhole, bulkhead and all 14 M3 holes measured off the legacy file. |
| `nose_plate` | Ported. Trapezoid outline, caster pattern, matching bulkhead half. |
| `motor_template` | Ported faithfully from `Motor Template v4`. |
| `cutter_motor_link` | First cut, not a port — the Fusion component of this name ships with no solid. |

Not modelled yet: side walls, wheel covers, wheels, electronics plate, and the
bumper linkage.

`params.py` holds every dimension. Values were measured by parsing the STEP
geometry in [../.docs/legacy-models/](../.docs/legacy-models/), so they're
as-modelled, not design intent. The three M3 hole sizes are the ones to verify
first: only `M3_CLEARANCE = 3.2` is confirmed.

## Checking it

```bash
python verify.py
```

Compares envelopes, hole counts and diameters against the legacy geometry, and
asserts both plates sit on z=0. Bounding boxes alone won't catch a feature
placed at the origin or a sketch extruded downwards — both of which happened
during the port.

## Two things worth knowing

**The motor bore is off-centre.** 7.5 mm off the bolt-circle centre, consistent
across the whole legacy design. That reads like a geared motor with an offset
output shaft. It's reproduced as found — confirm against the real motor before
cutting a new mount.

**The motor doesn't bolt to the base plate.** The plate carries a 3-bolt Ø40
pattern; the motor's own pattern is 6 bolts on Ø31. `cutter_motor_link` adapts
between the two — that's its whole job, and it's why the legacy assembly has a
component by that name.

**The cutter hole is a keyhole, not a circle.** Ø30 bore with a 10 mm slot
running forward to a rounded end at y=-20. Reproduced as measured.

## Seeing it

Two viewers, and they're good at different things. Run both at once — they
don't conflict.

**VS Code panel** — the fast loop. Live geometry, no file to open, re-render on
demand while you iterate.

```bash
python show.py              # everything, spread out
python show.py base_plate   # just one
```

Open the panel first, or `show.py` will tell you to: Ctrl+Shift+P →
**OCP CAD Viewer: Open viewer**. Needs the *OCP CAD Viewer* extension installed
once.

**FreeCAD** — for measuring, section views, and checking the exported file
rather than the code's idea of it.

```bash
python build.py                                    # refresh the exports first
"$LOCALAPPDATA/Programs/FreeCAD 1.1/bin/freecad.exe" build/base_plate.step
```

FreeCAD runs the same OpenCascade kernel this code does, so it shows exactly
what was built, with no translation in between. It reads the file from disk
though, so re-run `build.py` before reopening — it won't refresh on its own.
