
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

import image_classifier 
import sensor_classifier 
from lib import pins
from lib import prediction
import motor 
from signal import signal, SIGINT
from sys import exit
import jetson.inference
import jetson.utils
import argparse
import sys

# Global variables 
confidence_threshold = 0.7 

# Clean up GPIO pins after exiting program 
def handler(signal, frame):
    print("Cleaning up!")
    GPIO.cleanup()
    exit(0)

# Run main classifier with motor control
def predict(sensor_prediction, image_prediction): 
    if sensor_prediction.metal or sensor_prediction.plastic or sensor_prediction.glass:
        return True 
    else: 
        return image_prediction.material != prediction.Material.trash and image_prediction.confidence > confidence_threshold 

def main(): 
    signal(SIGINT, handler)
    stepper = pins.setup()


    argv = ['overall_classifier.py', '--model=/home/binthere/jetson-inference/python/training/classification/models/GarbageClassification/resnet50.onnx', '--input_blob=input_0', '--output_blob=output_0', '--labels=/home/binthere/jetson-inference/python/training/classification/data/GarbageClassification/labels.txt', 'csi://0']
    is_headless = "--headless" if sys.argv[0].find('console.py') != -1 else "" 
    
    net = jetson.inference.imageNet("", argv)
    input = jetson.utils.videoSource("csi://0", argv=argv)
    output = jetson.utils.videoOutput("", argv=argv.append(is_headless))
    font = jetson.utils.cudaFont()
    
    while True: 
        # Wait for box to close 
        print("Waiting for box to close")
        GPIO.wait_for_edge(pins.switch_pin, GPIO.FALLING)
        print("Box closed")

        # Get sensor and image classifier predictions 
        time.sleep(0.2)
        img = input.Capture()
        image_prediction = image_classifier.predict(net, img, output)  
        sensor_prediction = sensor_classifier.predict()
        
        # Render image 
        font.OverlayText(img, img.width, img.height, "{:05.2f}% {:s}".format(image_prediction.confidence * 100, image_prediction.material), 5, 5, font.White, font.Gray40)
        output.Render(img)
        output.SetStatus("{:s} | Network {:.0f} FPS".format(net.GetNetworkName(), net.GetNetworkFPS()))
        net.PrintProfilerTimes()
 
        # Combine classifications 
        isRecyclable = predict(sensor_prediction, image_prediction)
        print("Recyclable: %s" % (isRecyclable))

        # Move motor 
        motor.move(stepper, isRecyclable)
        print("Done!")
        print("-----------------------------------------\n")
        time.sleep(0.5)
    
    GPIO.cleanup()
    

if __name__ == '__main__':
    main()
