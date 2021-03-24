import Rpi.GPIO as GPIO 
from RpiMotorLib import RpiMotorLib 
    
#define GPIO pins
GPIO_pins = (14, 15, 18)    # Microstep Resolution MS1-MS3 -> GPIO Pin
direction = 20              # Direction -> GPIO Pin
step = 21                   # Step -> GPIO Pin

# Declare a instance of class pass GPIO pins numbers and the motor type
stepper = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "DRV8825") # or a4988

# turn cw?, step type, # steps, delay, verbose, initDelay    
stepper.motor_go(False, "Full" , 100, .01, False, .05)
stepper.motor_go(True, "Full" , 100, .01, False, .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
    