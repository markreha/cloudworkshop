import RPi.GPIO as GPIO
import dht11_lib
import time
import datetime
import json
import requests

# Application constants
sampleTime = 1
debug = True
webApiUrl = "https://api.github.com/users/markreha/repos"

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Read data from sensor on GPIO pin 4
instance = dht11_lib.DHT11(pin=4)

# Sit in a loop reading the sensor every sampleTime, convert result to JSON, and POST to our Web API
data = {}
while True:
    # Read the sensor
    result = instance.read()
    if result.is_valid():
        # Get results
        now = str(datetime.datetime.now())
        tempC = result.temperature
        tempF = (result.temperature * 9/5 + 32)
        humidity = result.humidity
        
        # Print results to the console
        print("Last valid input: " + now)
        print("Temperature: %d C" % tempC)
        print("Temperature: %d F" % tempF)
        print("Humidity: %d %%" % humidity)

        # Save results to a data object
        data["timestamp"] = now
        data["tempC"] = tempC
        data["tempF"] = tempF
        data["humidity"] = humidity

        # Convert data object to JSON and print the console
        strj = json.dumps(data, ensure_ascii=False)
        print("JSON data is %s" % strj)

        # POST the JSON results to the RESTful Web API
        #  TODO: change this to a POST and use our API
        #  TODO: add security
        response = requests.get(webApiUrl)
        assert response.status_code == 200
        for repo in response.json():
            print('[{}] {}'.format(repo['language'], repo['name']))

    # Sleep until we need to read the sensor again
    time.sleep(sampleTime)
