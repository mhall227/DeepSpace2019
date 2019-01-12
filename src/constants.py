import json
import math
from utils import log

class Constants:
    """Global constants that are accesed throughout the project."""
    CONSTANTS_JSON_PATH = "/home/lvuser/py_constants.json"

    # Motion
    THEORETICAL_MAX_VELOCITY = 60

    # PDP
    PDP_ID = 60

    # Gyro
    GYRO_ID = 6

    # Drive motors
    LS_MOTOR_ID = 1
    LM_MOTOR_ID = 3
    RS_MOTOR_ID = 5
    RM_MOTOR_ID = 2

    # Intake motors
    IR_MOTOR_ID = 6
    IL_MOTOR_ID = 4

    # Wheel measurements
    WHEEL_DIAMETER = 6  # inches TODO update
    WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * math.pi  # inches
    # inches (distance between front and back wheels) TODO update
    WHEEL_BASE = 27.75
    # inches (distance between left and right wheels) TODO update
    TRACK_WIDTH = 27.75

    # Encoder measurements
    DRIVE_ENCODER_TICKS_PER_REVOLUTION_LEFT = 360  # TODO update
    DRIVE_ENCODER_TICKS_PER_REVOLUTION_RIGHT = 360  # TODO update

    # Turn to angle pid values
    TURN_TO_ANGLE_KP = 0.34
    TURN_TO_ANGLE_KI = 0.57
    TURN_TO_ANGLE_KD = 0.0057

    TURN_TO_ANGLE_TOLERANCE =  0.0873

    # Pure pursuit values
    MAX_VELOCITY = 60  # inches/sec
    MAX_ACCELERATION = 10  # inches/sec/sec
    # TODO dynamically change lookahead distance based on the curvature of path/velocity of robot
    LOOKAHEAD_DIST = 24  # shorter == more overshoot, longer == longer to correct
    CURVE_VELOCITY = 0.25  # smaller == slower around turns
    CURVATURE_THRESHOLD = 1e-9

    PURE_PURSUIT_KV = 1 / THEORETICAL_MAX_VELOCITY
    PURE_PURSUIT_KA = 0.002
    PURE_PURSUIT_KP = 0.01

    # Joystick values
    DRIVER_PORT = 0
    OPERATOR_PORT = 1

    DRIVER_X_MOD = 1
    DRIVER_Y_MOD = -1
    DRIVER_Z_MOD = 1

    OPERATOR_X_MOD = 1
    OPERATOR_Y_MOD = 1
    OPERATOR_Z_MOD = 1

    JOYSTICK_DEADZONE = 0.05
    TANK_DRIVE_EXPONENT = 3

    @staticmethod
    def updateConstants():
        try:
            json_file = open(Constants.CONSTANTS_JSON_PATH, "r")
            file_dict = json.load(json_file)
            json_file.close()
            for var_name in file_dict.keys():
                if hasattr(Constants, var_name):
                    setattr(Constants, var_name, file_dict[var_name])
        except FileNotFoundError:
            try:
                class_dict = {key: value for key, value in Constants.__dict__.items(
                ) if not key.startswith("__")}
                class_dict.pop('updateConstants', None)
                with open(Constants.CONSTANTS_JSON_PATH, "w") as json_file:
                    json.dump(class_dict, json_file)
            except FileNotFoundError:
                log.printerr("Failed to dump constants json, probably unit testing")
                return
