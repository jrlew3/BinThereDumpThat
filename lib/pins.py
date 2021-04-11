import Jetson.GPIO as GPIO 
from RpiMotorLib import RpiMotorLib

# Sensor Pin Definitions
plastic_low_pin = 5 
plastic_high_pin = 6 
glass_low_pin = 13
glass_high_pin = 19 
metal_pin = 26 

 
# Motor Pin Definitions pins
GPIO_pins = (16, 20, 21)    # Microstep Resolution MS1-MS3 -> GPIO Pin
direction = 17              # Direction -> GPIO Pin
step = 27                   # Step -> GPIO Pin
switch_pin = 22 

def setup():  
    # Setup pins    
    GPIO.setmode(GPIO.BCM)  
    channels = [switch_pin, metal_pin, plastic_low_pin, plastic_high_pin, glass_low_pin, glass_high_pin]
    GPIO.setup(channels, GPIO.IN)

    # Initialize motor 
    stepper = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988") # DRV8825 or A4988
    return stepper 
