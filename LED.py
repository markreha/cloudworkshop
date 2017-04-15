import RPi.GPIO as GPIO
import time

print("Starting LED and GPIO test...........")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,GPIO.HIGH)
print("LED on")
time.sleep(5)
GPIO.output(3,GPIO.LOW)
print("LED off")
time.sleep(5)
GPIO.output(3,GPIO.HIGH)
print("LED on")
print("Completed LED and GPIO test")



