#coding: UTF-8

import RPi.GPIO as GPIO
import time

print "Hello RPi.GPIO"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 14
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0)

print "ready?"
raw_input()

i = 0
while i<10000:
    print "touchesBegan"
    GPIO.output(led, 1)
    time.sleep(0.3)
    print "touchesEnded"
    GPIO.output(led, 0)
    time.sleep(0.3)
    i += 1

GPIO.cleanup()
