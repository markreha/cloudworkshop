import RPi.GPIO as GPIO
import dht11_lib
import time
import datetime

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Read data using pin 4
instance = dht11_lib.DHT11(pin=4)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Temperature: %d F" % (result.temperature * 9/5 + 32))
        print("Humidity: %d %%" % result.humidity)
    time.sleep(1)
