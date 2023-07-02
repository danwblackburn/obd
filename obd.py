import RPi.GPIO as GPIO

channel = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)

while True:
	print(GPIO.input(channel))
