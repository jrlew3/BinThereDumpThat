import RPi.GPIO as GPIO
import time
from lib import pins


def predict():
    print("Collecting sensor data\n")
    metal_value = GPIO.input(pins.metal_pin)
    plastic_low_value = GPIO.input(pins.plastic_low_pin)
    plastic_high_value = GPIO.input(pins.plastic_high_pin)
    glass_low_value = GPIO.input(pins.glass_low_pin)
    glass_high_value = GPIO.input(pins.glass_high_pin)
    
    isMetal = metal_value == GPIO.LOW
    isPlastic = plastic_low_value == GPIO.LOW and plastic_high_value == GPIO.HIGH
    isGlass = glass_low_value == GPIO.LOW and glass_high_value == GPIO.HIGH 

    prediction = Prediction(isMetal, isPlastic, isGlass)
    print("Prediction': ", prediction)
    return prediction

if __name__ == '__main__':
    predict()