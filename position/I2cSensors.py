"""
Contains class to manage all 12c sensors
1. get current tilt angle form IMU.
2. get angle of both encoders from ESP-32
Requires CircuitPython and Adafruit LSM6DS module.
"""
from smbus2 import SMBus
import time
from numpy import arctan2
from numpy import pi
import time
import board
from adafruit_lsm6ds.lsm6dso32 import LSM6DSO32

class Sensors:
    def __init__(self):
        i2c = board.I2C()  # uses board.SCL and board.SDA
        self.i2c_bus = SMBus(1)
        self.ESP32_addr = 8
        self.imu = LSM6DSO32(i2c)

    def IMU(self):
        accel_x, _, accel_z = self.imu.acceleration
        tilt = 0.0
        for i in range(100):
            tilt += arctan2(accel_x, accel_z)
        tilt /= 100.0
        return tilt
    
    def Encoders(self):
        block = self.i2c_bus.read_i2c_block_data(self.ESP32_addr, 0, 4)
        block = self.i2c_bus.read_i2c_block_data(self.ESP32_addr, 0, 4)
        angle_1, (angle_2 = block[0]*255 + block[1] - 2400)*(2*pi)/2400, (block[2]*255 + block[3] - 2400)*(2*pi)/2400
        return angle_1, angle_2