#!/usr/bin/env python3
"""A python 3 library for various
 motors and servos to connect to a raspberry pi"""
# ========================= HEADER ===================================
# title             :rpiMotorlib.py
# description       :A python 3 library for various motors
# and servos to connect to a raspberry pi
# This file is for stepper motor tested on
# 28BYJ-48 unipolar stepper motor with ULN2003  = BYJMotor class
# Bipolar Nema stepper motor with L298N = BYJMotor class.
# Bipolar Nema Stepper motor TB6612FNG = BYJMotor class
# Bipolar Nema Stepper motor A4988  Driver = A4988Nema class
# Bipolar Nema Stepper motor DRV8825 Driver = A4988Nema class
# Bipolar Nema Stepper motor A3967 Easy Driver = A3967EasyNema class
# author            :Gavin Lyons
# Date created      :See changelog at url
# Version           ;See changelog at url
# url               :https://github.com/gavinlyonsrepo/RpiMotorLib
# mail              :glyons66@hotmail.com
# python_version    :3.4.2

# ========================== IMPORTS ======================
# Import the system modules needed to run rpiMotorlib.py
import sys
import time
import Jetson.GPIO as GPIO

# ==================== CLASS SECTION ===============================


class A4988Nema(object):
    """ Class to control a Nema bi-polar stepper motor with a A4988 also tested with DRV8825"""
    def __init__(self, direction_pin, step_pin, mode_pins, motor_type="A4988"):
        """ class init method 3 inputs
        (1) direction type=int , help=GPIO pin connected to DIR pin of IC
        (2) step_pin type=int , help=GPIO pin connected to STEP of IC
        (3) mode_pins type=tuple of 3 ints, help=GPIO pins connected to
        Microstep Resolution pins MS1-MS3 of IC
        (4) motor_type type=string, help=TYpe of motor two options: A4988 or DRV8825
        """
        self.motor_type = motor_type
        self.direction_pin = direction_pin
        self.step_pin = step_pin
        self.mode_pins = mode_pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def resolution_set(self, steptype):
        """ method to calculate step resolution
        based on motor type and steptype"""
        if self.motor_type == "A4988":
            resolution = {'Full': (0, 0, 0),
                          'Half': (1, 0, 0),
                          '1/4': (0, 1, 0),
                          '1/8': (1, 1, 0),
                          '1/16': (1, 1, 1)}
        elif self.motor_type == "DRV8825":
            resolution = {'Full': (0, 0, 0),
                          'Half': (1, 0, 0),
                          '1/4': (0, 1, 0),
                          '1/8': (1, 1, 0),
                          '1/16': (0, 0, 1),
                          '1/32': (1, 0, 1)}
        else: 
            print("Error invalid motor_type: {}".format(self.motor_type))
            quit()
        
        # error check stepmode
        if steptype in resolution:
            pass
        else:
            print("Error invalid steptype: {}".format(steptype))
            quit()

        GPIO.output(self.mode_pins, resolution[steptype])

    def motor_go(self, clockwise=False, steptype="Full",
                 steps=200, stepdelay=.005, verbose=False, initdelay=.05):
        """ motor_go,  moves stepper motor based on 6 inputs
         (1) clockwise, type=bool default=False
         help="Turn stepper counterclockwise"
         (2) steptype, type=string , default=Full help= type of drive to
         step motor 5 options
            (Full, Half, 1/4, 1/8, 1/16)
         (3) steps, type=int, default=200, help=Number of steps sequence's
         to execute. Default is one revolution , 200 in Full mode.
         (4) stepdelay, type=float, default=0.05, help=Time to wait
         (in seconds) between steps.
         (5) verbose, type=bool  type=bool default=False
         help="Write pin actions",
         (6) initdelay, type=float, default=1mS, help= Intial delay after
         GPIO pins initialized but before motor is moved.
        """
        # setup GPIO
        GPIO.setup(self.direction_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.output(self.direction_pin, clockwise)
        GPIO.setup(self.mode_pins, GPIO.OUT)
        try:
            # dict resolution
            self.resolution_set(steptype)

            time.sleep(initdelay)

            for i in range(steps):
                GPIO.output(self.step_pin, True)
                time.sleep(stepdelay)
                GPIO.output(self.step_pin, False)
                time.sleep(stepdelay)
                if verbose:
                    print("Steps count {}".format(i))

        except KeyboardInterrupt:
            print("User Keyboard Interrupt : RpiMotorLib:")
        except Exception as motor_error:
            print(sys.exc_info()[0])
            print(motor_error)
            print("RpiMotorLib  : Unexpected error:")
        else:
            # print report status
            if verbose:
                print("\nRpiMotorLib, Motor Run finished, Details:.\n")
                print("Motor type = {}".format(self.motor_type))
                print("Clockwise = {}".format(clockwise))
                print("Step Type = {}".format(steptype))
                print("Number of steps = {}".format(steps))
                print("Step Delay = {}".format(stepdelay))
                print("Intial delay = {}".format(initdelay))
                print("Size of turn in degrees = {}"
                      .format(degree_calc(steps, steptype)))
        finally:
            # cleanup
            GPIO.output(self.step_pin, False)
            GPIO.output(self.direction_pin, False)
            for pin in self.mode_pins:
                GPIO.output(pin, False)



def degree_calc(steps, steptype):
    """ calculate and returns size of turn in degree
    , passed number of steps and steptype"""
    degree_value = {'Full': 1.8,
                    'Half': 0.9,
                    '1/4': .45,
                    '1/8': .225,
                    '1/16': 0.1125,
                    '1/32': 0.05625}
    degree_value = (steps*degree_value[steptype])
    return degree_value


def importtest(text):
    """ testing import """
    # print(text)
    text = " "

# ===================== MAIN ===============================


if __name__ == '__main__':
    importtest("main")
else:
    importtest("Imported {}".format(__name__))


# ===================== END ===============================
