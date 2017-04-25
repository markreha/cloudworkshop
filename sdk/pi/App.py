import TemperatureSensor
import LED
import datetime
import json
import requests
import time

# Application constants
sampleTime = 20
debug = True
deviceID = 0
#webApiUrl = "http://marks-macbookair.local:8080/workshop/rest/dht11/save"
webApiUrl = "http://node5.codenvy.io:37551/cloudservices/rest/dht11/save"
#webApiUrl = "http://cloud-services-playlaravel.44fs.preview.openshiftapps.com/cloadservices/rest/dht11/save"
webApiUsername = "CloudWorkshop"
webApiPassword = "dGVzdHRlc3Q="

# Create an indicator LED on GPIO pin 17
led = LED(17)

# Create the Temperature Sensor on GPIO pin 4
temperatureSensor = TemperatureSensor(4)

# Dictionary to hold Temperature Sensor data
temperatureData = {}

# Sit in a loop reading the sensors every sampleTime, convert result to JSON, and POST to the Web API
while True:
	# Turn LED ON
	led.on()
	
    # Read the Temperature Sensor
	temperatureSensor.read()
	if temperatureSensor.valid:
		# Save the Temperature Sensor results in a Temperature Data Object
		temperatureData["deviceID"] = deviceID
		temperatureData["temperature"] = temperatureSensor.temperatureF
		temperatureData["humidity"] = temperatureSensor.humidity
        
		# Print results to the console if in debug mode
		if debug:
			print("Sampled at %s  Temperature: %.2f F Humidity: %.2f" % (str(datetime.datetime.now()), temperatureData["temperature"], temperatureData["humidity"]))

		# Convert the Temperature Data Object to JSON string
		strj = json.dumps(temperatureData, ensure_ascii=False)

		# POST the JSON results to the RESTful Web API using HTTP Basic Authentication
		response = requests.post(webApiUrl, strj, headers={'Content-Type':'application/json'}, auth=(webApiUsername, webApiPassword))
		if response.status_code == 200:
			strj = response.json()
			print("Response status is %s with message of %s" % (strj["status"], strj["message"]))
		else:
			print("Response Error: %d" % response.status_code)
	else:
		print("Temperature Sensor Error")

	# Turn LED OFF
	led.off()
	
	# Sleep until we need to read the sensors again
	time.sleep(sampleTime)