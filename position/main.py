"""
Main file to run other functions
"""

from math import pi
from calculate_position import *
import time
from I2cSensors import Sensors

sens = Sensors() # initalize the class or i get errors there is probably a better way to do this

#imu = Sensors.IMU()
encoders = sens.Encoders()
while True:
    #print(imu())
    print(encoders)
    time.sleep(0.1)


#s_initial = calculate_current_lengths(pi/6, pi/6, 0)
#print(s_initial)

#s_final = calculate_next_position(1900, -600)
#print(s_final)

#s_diff = calculate_position_difference(s_initial, s_final)
#print(s_diff)