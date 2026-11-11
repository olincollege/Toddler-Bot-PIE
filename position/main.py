"""
Main file to run other functions
"""

from math import pi
from calculate_position import *
import time
from IMU import *

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

imu = IMU()
while True:
    print(imu.readTilt())
    time.sleep(0.1)


#s_initial = calculate_current_lengths(pi/6, pi/6, 0)
#print(s_initial)

#s_final = calculate_next_position(1900, -600)
#print(s_final)

#s_diff = calculate_position_difference(s_initial, s_final)
#print(s_diff)