"""
Contains class to manage IMU and to get current tilt angle.
Requires CircuitPython and Adafruit LSM6DS module.
"""

from numpy import arctan2
import time
import board
from adafruit_lsm6ds.lsm6dso32 import LSM6DSO32

class IMU:
    def __init__(self):
        i2c = board.I2C()  # uses board.SCL and board.SDA
        # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
        self.sensor = LSM6DSO32(i2c)

    def readTilt(self):
        accel_x, _, accel_z = self.sensor.acceleration
        tilt = 0.0
        for i in range(100):
            tilt += arctan2(accel_x, accel_z)
        tilt /= 100.0
        return tilt