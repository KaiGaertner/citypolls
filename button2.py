import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True: # Run forever
	if GPIO.input(10) == GPIO.LOW:
		print("Button YES was pushed!")
		time.sleep(1)
	if GPIO.input(12) == GPIO.LOW:
		print("Button NO was pushed!")
		time.sleep(1)
