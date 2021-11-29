import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
b = [26]
y = [20]
g = [19]
r = [21]
GPIO.setup(b, GPIO.OUT)
GPIO.setup(y, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(r, GPIO.OUT)
while True:
	GPIO.output(b, 1)
	GPIO.output(y, 0)
	GPIO.output(g, 0)
	GPIO.output(r, 0)
	time.sleep(0.08)
	GPIO.output(b, 0)
	GPIO.output(y, 1)
	GPIO.output(g, 0)
	GPIO.output(r, 0)
	time.sleep(0.08)
	GPIO.output(b, 0)
	GPIO.output(y, 0)
	GPIO.output(g, 0)
	GPIO.output(r, 1)
	time.sleep(0.08)
	GPIO.output(b, 0)
	GPIO.output(y, 0)
	GPIO.output(g, 1)
	GPIO.output(r, 0)
	time.sleep(0.08)
