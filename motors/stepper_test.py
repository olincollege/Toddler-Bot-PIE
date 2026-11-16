#!/usr/bin/env python3
"""
Example file for RpiMotorLib
Module : RpiMotorLib.py
Class  : BYJMotor
Tested : L298 controller bipolar stepper motor

Pinout used:
    IN1 - GPIO 19
    IN2 - GPIO 26
    IN3 - GPIO 21
    IN4 - GPIO 13

To disable emergency stop, comment out the EmergencyStop lines below.
Wire push button: VCC - PB Pin 1, GPIO 17 - PB Pin 2.
"""

import sys
import time
from RpiMotorLib import RpiMotorLib
from numpy import pi

# Declare an named instance of class pass a name and type of motor
# type of motor(Nema) is case sensitive
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")


class move_motors:
    def __init__(self, motor_side):
        self.motor = RpiMotorLib.BYJMotor("Motor", "Nema")
        if motor_side == (1, 0):
            self.gpio_pins_0 = [12, 16, 20, 21]
            self.gpio_pins_1 = [6, 13, 19, 26]
            self.motor_0_dir = -1
            self.motor_1_dir = 1
            self.motor_0_muplr = 50/(pi*9.87)
            self.motor_1_muplr = 50/(pi*9.71)
        elif motor_side == (0, 1):
            self.gpio_pins_0 = [6, 13, 19, 26]
            self.gpio_pins_1 = [12, 16, 20, 21]
            self.motor_0_dir = 1
            self.motor_1_dir = -1
            self.motor_0_muplr = 50/(pi*9.71)
            self.motor_1_muplr = 50/(pi*9.87)
                        

    def move(self, dist):
        self.motor.motor_run(self.gpio_pins_0,.01, round(abs(dist[0] * self.motor_0_muplr)), self.motor_0_dir*dist[0]>0, False,"full", 0)
        self.motor.motor_run(self.gpio_pins_1,.01, round(abs(dist[1] * self.motor_1_muplr)), self.motor_1_dir*dist[1]>0, False,"full", 0)


#move = move_motors((1, 0))

#move.move((-75, -75))