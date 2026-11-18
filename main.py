from numpy import array
from position.calculate_position import *
from matplotlib import pyplot as plt
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
    current_lengths = (1035.0, 995.0)

    for point in points:
        next_lengths = calculate_next_position(*point[:2])
        dist = calculate_position_difference(current_lengths, next_lengths)
        diff = split_lengths_list(dist, length)
        for d in diff:
            print(f"left: {d[0]}, right: {d[1]}")
            motors.move(d)
        current_lengths = next_lengths

    return_dist = calculate_position_difference(current_lengths, (1035.0, 995.0))
    return_diff = split_lengths_list(return_dist, length)
    for d in return_diff:
        print(f"left: {d[0]}, right: {d[1]}")
        motors.move(d)


def draw_with_subpoints(motors, points, dist):
    """
    draw by linearly spacing points
    """

    subpoints = []
    for i in range(len(points)-1):
        subpoints += space_points_linearly(points[i], points[i+1], dist)

    for point in points:
        theta_l = 0 #left encoder reading
        theta_r = 0 #right encoder reading
        phi = 0 #IMU reading
        current_pos, _ = calculate_current_position(theta_l, theta_r, phi)
        subpoints = space_points_linearly(current_pos, point)

        for subpoint in subpoints:
            theta_l = 0 #left encoder reading
            theta_r = 0 #right encoder reading
            phi = 0 #IMU reading
            current_pos, current_lengths = calculate_current_position(theta_l, theta_r, phi)
            next_lengths = calculate_next_position(*subpoint, phi)
            diff_lengths = calculate_position_difference(current_lengths, next_lengths)
            # MOVE BY LENGTH DIFFERENCE





motors = MoveMotors((1,0))
draw_with_subpoints(motors, 10.0)