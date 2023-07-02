import RPi.GPIO as GPIO

import time
import csv
from datetime import datetime, timezone

recording_data = False

start_time = time.time()

channel = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if recording_data:
	filename = "logs/{now}.csv".format(now = datetime.now(timezone.utc).strftime('%y%m%d %H:%M:%S'))
	logger = csv.writer(open(filename, 'w'))
	logger.writerow(['time', 'reading'])

while True:
	reading = GPIO.input(channel)
	if recording_data:
		logger.writerow([time.time(), reading])
	time.sleep(.001)
	
