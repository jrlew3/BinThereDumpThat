import RPi.GPIO as GPIO
import time

# Pin Definitions
metal_pin = 27  
plastic_low_pin = 29 
plastic_high_pin = 31 
switch_pin = 33 

GPIO.setmode(GPIO.BOARD)  
channels = [metal_pin, plastic_low_pin, plastic_high_pin, switch_pin]
GPIO.setup(channels, GPIO.IN)

def predict():
    print("Waiting for switch\n")
    GPIO.wait_for_edge(switch_pin, GPIO.RISING)
    print("Switch detected!\n")

    time.sleep(0.5)
    print("Collecting sensor data\n")
    metal_value = GPIO.input(metal_pin)
    plastic_low_value = GPIO.input(plastic_low_pin)
    plastic_high_value = GPIO.input(plastic_high_pin)
    
    isMetal = metal_value == GPIO.LOW: 
    isPlastic = plastic_low_value == GPIO.LOW and plastic_high_value == GPIO.HIGH: 
    GPIO.cleanup()

    prediction = Prediction(isMetal, isPlastic)
    print("Prediction': ", prediction)
    return prediction

if __name__ == '__main__':
    predict()