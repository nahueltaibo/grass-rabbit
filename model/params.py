"""Dimensions recovered from the legacy Fusion design.

Measured by parsing the STEP geometry in ../.docs/legacy-models/, so these are
as-modelled values, not design intent. Anything marked TODO is a conventional
value standing in until the Fusion user parameter is read back.

Axes: X across the robot, Y along it (+Y to the rear, -Y to the nose), Z up.
The legacy file uses Y-up; coordinates here are converted.
"""

# --- Fastener holes ---------------------------------------------------------
# Fusion carries these as named user parameters: M3PassThrowHole,
# M3HoleForBolt, SelfTappingM3ScrewHole. Only the first is confirmed.
M3_CLEARANCE = 3.2
M3_BOLT = 3.4  # TODO confirm against M3HoleForBolt
M3_SELF_TAP = 2.8  # TODO confirm against SelfTappingM3ScrewHole

# --- Shared plate geometry --------------------------------------------------
PLATE_T = 3.0
BULKHEAD_H = 8.0  # lip height above the plate top face
BULKHEAD_W = 4.354  # lip depth, front-to-back
JOINT_Y = -80.0  # where the base plate and nose plate meet

# --- Base plate -------------------------------------------------------------
BASE_W = 160.0
BASE_FRONT_Y = -79.9
BASE_BACK_Y = 80.0

# Keyhole: cutter shaft bore, with a slot running forward to a rounded end.
CUTTER_BORE_D = 30.0
CUTTER_SLOT_D = 10.0
CUTTER_SLOT_Y = -20.0

# The cutter motor link bolts up into the plate here. Note this is NOT the
# motor's own pattern -- the link adapts between the two.
LINK_BCD = 40.0
LINK_BOLT_COUNT = 3
LINK_BOLT_START = 90.0  # degrees, first hole dead aft of the bore

# Structural M3 holes, measured off the legacy plate.
BASE_HOLES = [
    (75.0, 70.0), (75.0, 25.0), (75.0, -25.0), (75.0, -70.0),
    (-75.0, 70.0), (-75.0, 25.0), (-75.0, -25.0), (-75.0, -70.0),
    (60.0, 75.0), (0.0, 75.0), (-60.0, 75.0),
]

# --- Nose plate -------------------------------------------------------------
# Trapezoid: full width at the joint, tapering to the caster at the tip.
NOSE_BACK_Y = -80.1
NOSE_BACK_HALF_W = 79.924
NOSE_TIP_Y = -165.0
NOSE_TIP_HALF_W = 15.0

NOSE_HOLES = [
    (61.56, -95.89), (-61.56, -95.89),
    (20.85, -149.11), (-20.85, -149.11),
]

# Swivel caster bolt pattern, 28 x 35.
CASTER_HOLE_D = 5.0
CASTER_HOLES = [
    (14.0, -107.0), (-14.0, -107.0),
    (14.0, -142.0), (-14.0, -142.0),
]

# --- Motor interface (Motor Template v4) ------------------------------------
# One pattern shared by every motor mount. In Fusion this was an XRef so a
# single edit propagated everywhere; here it's a function in motor_template.py.
MOTOR_FLANGE_D = 36.75
MOTOR_BOLT_BCD = 31.0
MOTOR_BOLT_D = 3.0
MOTOR_BOLT_COUNT = 6
MOTOR_BORE_D = 13.0
# The output shaft is 7.5 off the bolt-circle centre -- a geared motor with an
# offset output, not a modelling slip. Confirm against the real motor.
MOTOR_BORE_OFFSET = 7.5
