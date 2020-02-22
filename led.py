import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
for i in range(5):
    GPIO.output(40, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(40, GPIO.LOW)
    time.sleep(0.5)
