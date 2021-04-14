import RPi.GPIO as GPIO
import time
from lib import pins
from lib import prediction
import time


def predict():
    print("Collecting sensor data")
    metal_value1 = GPIO.input(pins.metal_pin)
    metal_value2 = GPIO.input(pins.metal_pin2)
    plastic_low_value = GPIO.input(pins.plastic_low_pin)
    plastic_high_value = GPIO.input(pins.plastic_high_pin)
    glass_low_value = GPIO.input(pins.glass_low_pin)
    glass_high_value = GPIO.input(pins.glass_high_pin)
    
    isMetal = metal_value1 == GPIO.LOW or metal_value2 == GPIO.LOW
    isPlastic = plastic_low_value == GPIO.LOW and plastic_high_value == GPIO.HIGH
    isGlass = glass_low_value == GPIO.LOW and glass_high_value == GPIO.HIGH 

    pred = prediction.SensorPrediction(isMetal, isPlastic, isGlass)
    print("metal 1: ", metal_value1)
    print("metal 2: ", metal_value2)
    print("Sensor Prediction: ", pred)
    return pred

if __name__ == '__main__':
    pins.setup()
    while True:
        predict()
        time.sleep(0.5)

    GPIO.cleanup()
