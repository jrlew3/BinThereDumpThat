
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time
import image_classifier 
import sensor_classifier 
from lib import pins
import motor 
from signal import signal, SIGINT
from sys import exit
import jetson.inference
import jetson.utils
import argparse
import sys

# Clean up GPIO pins after exiting program 
def handler(signal, frame):
    GPIO.cleanup()
    exit(0)

# Run main classifier with motor control
def main(): 
    signal(SIGINT, handler)
    stepper = pins.setup()

    while true: 
        input() 

        # Wait for box to close 
        GPIO.wait_for_edge(switch_pin, GPIO.RISING)
        
        # Get sensor and image classifier predictions 
        sensor_prediction = sensor_classifier.predict()
        
        img = jetson.utils.input.Capture()
        image_prediction = image_classifier.predict(net, img)  
         

        # Combine classifications 
        isRecyclable = image_prediction.metal or image_prediction.glass or image_prediction.plastic

        print("Recyclable: %s" % (isRecyclable))

        # Move motor 
        motor.move(stepper, isRecyclable)
    
    GPIO.cleanup()
    

if __name__ == '__main__':
    main()
