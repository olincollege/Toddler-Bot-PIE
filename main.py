from numpy import array
from position.calculate_position import *
from motors.stepper_test import MoveMotors

# scan SVG for image

# for point in points:
    # get tilt angle from IMU
    # get string angles from encoders
    # calculate current position from sensor data
    # calculate next position from points
    # if pen-down coord is 1: (can change later for multi-color)
        # put pen down
    # else
        # put pen up
    # use motors to move both strings (async?)
    # stop motors


def write_long_strokes():
    points = [(914.0, -400.0, 0), (914.0, -600.0, 1), (445.0, -488.0, 1), (1340.0, -643.0, 1)]
    current_lengths = (915.0, 915.0)

    for point in points:
        next_lengths = calculate_next_position(*point[:2])
        diff_lengths = calculate_position_difference(current_lengths, next_lengths)
        # move motors to pull string by diff_length
        current_lengths = next_lengths

def write_short_strokes(length, motors):
    points = [(914.0, -400.0, 0), (914.0, -600.0, 1), (445.0, -488.0, 1), (1340.0, -643.0, 1)]
    current_lengths = (915.0, 915.0)

    for point in points:
        next_lengths = calculate_next_position(*point[:2])
        dist = calculate_position_difference(current_lengths, next_lengths)
        diff = split_points_list(dist, length)
        for d in diff:
            print(f"left: {d[0]}, right: {d[1]}")
            motors.move(d)
        current_lengths = next_lengths


motors = MoveMotors((1, 0))
write_short_strokes(5.0, motors)