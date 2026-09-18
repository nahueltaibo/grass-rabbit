"""Dimensions recovered from the legacy Fusion design.

Everything here was measured out of .docs/legacy-models/ by parsing the STEP
geometry, so these are as-modelled values, not design intent. Anything marked
TODO is a conventional value standing in until the Fusion user parameter is
read back.
"""

# --- Fastener holes ---------------------------------------------------------
# Fusion carries these as named user parameters: M3PassThrowHole,
# M3HoleForBolt, SelfTappingM3ScrewHole. Only the first is confirmed --
# the Base Plate has 34 holes at 3.2.
M3_CLEARANCE = 3.2
M3_BOLT = 3.4  # TODO confirm against M3HoleForBolt
M3_SELF_TAP = 2.8  # TODO confirm against SelfTappingM3ScrewHole

# --- Motor interface (Motor Template v4) ------------------------------------
# One pattern shared by every motor mount. In Fusion this was an XRef so a
# single edit propagated everywhere; here it's a function in motor_template.py.
MOTOR_FLANGE_D = 36.75
MOTOR_BOLT_BCD = 31.0
MOTOR_BOLT_D = 3.0
MOTOR_BOLT_COUNT = 6
MOTOR_BORE_D = 13.0
# The output shaft is 7.5 off the bolt-circle centre -- a geared motor with an
# offset output, not a modelling slip. Confirm before cutting a new mount.
MOTOR_BORE_OFFSET = 7.5

# --- Base plate -------------------------------------------------------------
PLATE_W = 160.0
PLATE_D = 164.5
PLATE_T = 3.0
CUTTER_CLEARANCE_D = 30.0
