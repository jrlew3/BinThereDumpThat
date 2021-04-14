import Jetson.GPIO as GPIO 
from RpiMotorLib import RpiMotorLib

delay = 0.0008 
initDelay = 0.05 
length1 = 600 
length2 = 610

def move(stepper, isRecyclable): 
    # turn cw?, step type, # steps, delay, verbose, initDelay 
    if isRecyclable: 
        stepper.motor_go(False, "Full" , length1, delay, False, initDelay)
        stepper.motor_go(True, "Full" , length2, delay, False, initDelay)
    else:
        stepper.motor_go(True, "Full" , length1, delay, False, initDelay)
        stepper.motor_go(False, "Full" , length2, delay, False, initDelay)

if __name__ == '__main__':
    stepper = pins.setup()
    move(stepper, true)
