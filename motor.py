import Jetson.GPIO as GPIO 
import stepper as RpiMotorLib 

#define GPIO pins
GPIO_pins = (13, 19, 26)    # Microstep Resolution MS1-MS3 -> GPIO Pin
direction = 20              # Direction -> GPIO Pin
step = 21                   # Step -> GPIO Pin

# Declare a instance of class pass GPIO pins numbers and the motor type
stepper = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988") # DRV8825 or A4988

def move(isRecyclable): 
    # turn cw?, step type, # steps, delay, verbose, initDelay    
    if isRecyclable: 
        stepper.motor_go(False, "Full" , 100, .01, False, .05)
        stepper.motor_go(True, "Full" , 100, .01, False, .05)
    else
        stepper.motor_go(False, "Full" , 100, .01, False, .05)
        stepper.motor_go(True, "Full" , 100, .01, False, .05)

    # good practise to cleanup GPIO at some point before exit
    GPIO.cleanup()

if __name__ == '__main__':
    move()
