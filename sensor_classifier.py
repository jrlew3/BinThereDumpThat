import RPi.GPIO as GPIO
import time
from lib import pins
from lib import prediction
import time


def predict():
    print("Collecting sensor data")
    metalDone = False
    plasticDone = False
    glassDone = False
    for i in range(5):
        metal_value1 = GPIO.input(pins.metal_pin)
        metal_value2 = GPIO.input(pins.metal_pin2)
        plastic_low_value = GPIO.input(pins.plastic_low_pin)
        plastic_high_value = GPIO.input(pins.plastic_high_pin)
        glass_low_value = GPIO.input(pins.glass_low_pin)
        glass_high_value = GPIO.input(pins.glass_high_pin)
    
        isMetal = (metal_value1 == GPIO.HIGH and metal_value2 == GPIO.LOW) or (metal_value1 == GPIO.LOW and metal_value2 == GPIO.HIGH)
        if (isMetal): metalDone = True
        isPlastic = plastic_low_value == GPIO.LOW and plastic_high_value == GPIO.HIGH
        if (isPlastic): plasticDone = True
        isGlass = glass_low_value == GPIO.LOW and glass_high_value == GPIO.HIGH 
        if (isGlass): glassDone = True
    pred = prediction.SensorPrediction(metalDone, plasticDone, glassDone)
    # print("metal 1: ", metal_value1)
    # print("metal 2: ", metal_value2)
    # print("plasticLow: ", plastic_low_value)
    # print("plasticHigh: ", plastic_high_value)
    # print("glassLow: ", glass_low_value)
    # print("glassHigh: ", glass_high_value)
    # print("Sensor Prediction: ", pred)
    return pred

if __name__ == '__main__':
    pins.setup()
    while True:
        predict()
        time.sleep(0.5)

    GPIO.cleanup()
