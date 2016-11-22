#coding: UTF-8

import RPi.GPIO as GPIO
import time
import os
import binascii

def get_sleep_time():
    min = 0.2
    max = 0.3
    num = 0.0
    while (num < min or max < num) :
        str = os.urandom(2)
        i = int(binascii.hexlify(str), 16)
        num = i / 65535.0
    return num

print "Hello RPi.GPIO"

t = get_sleep_time()
print("%f" % t)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 14
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0)

print "ready?"
raw_input()

while True:
    print "touchesBegan"
    GPIO.output(led, 1)
    time.sleep(get_sleep_time())
    print "touchesEnded"
    GPIO.output(led, 0)
    time.sleep(get_sleep_time())

GPIO.cleanup()
