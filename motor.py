import Jetson.GPIO as GPIO 
from RpiMotorLib import RpiMotorLib

delay = 0.00045   
initDelay = 0.03 
length = 500 

def move(stepper, isRecyclable): 
    # turn cw?, step type, # steps, delay, verbose, initDelay 
    if isRecyclable: 
        stepper.motor_go(False, "Full" , length, delay, False, initDelay)
        stepper.motor_go(True, "Full" , length, delay, False, initDelay)
    else:
        stepper.motor_go(False, "Full" , length, .01, False, initDelay)
        stepper.motor_go(True, "Full" , length, .01, False, initDelay)

if __name__ == '__main__':
    move(stepper, true)
