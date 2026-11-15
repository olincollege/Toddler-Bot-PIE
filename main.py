from numpy import array
from position.calculate_position import *

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

points = [(914.0, -400.0, 0), (914.0, -600.0, 1), (445.0, -488.0, 1), (1340.0, -643.0, 1)]
current_lengths = (915.0, 915.0)

for point in points:
    next_lengths = calculate_next_position(*point[:2])
    diff_lengths = calculate_position_difference(current_lengths, next_lengths)
    # move motors to pull string by diff_length
    current_lengths = next_lengths