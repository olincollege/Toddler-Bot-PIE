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

# Declare an named instance of class pass a name and type of motor
# type of motor(Nema) is case sensitive
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")


def main():
    """main function loop"""
    # ====== tests for motor L298STepTest ====
    # Connect GPIO to [IN1 , IN2 , IN3 ,IN4] on Motor PCB
    gpio_pins_1 = [6, 13, 19, 26]
    gpio_pins_2 = [12, 16, 20, 21]

    #Arguments  for motor run function
    #(GPIOPins, stepdelay, steps, counterclockwise, verbose, steptype, initdelay)
    mymotortest.motor_run(gpio_pins_1,.01, 50, True, False,"full", 0)
    mymotortest.motor_run(gpio_pins_2,.01, 50, True, False,"full", 0)

# ===================MAIN===============================

if __name__ == '__main__':

    print("START")
    main()
    sys.exit()
# =====================END===============================