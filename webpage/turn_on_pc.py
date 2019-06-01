import RPi.GPIO as GPIO
import time
channel = 21
# GPIO setup
GPIO.setmode(GPIO.BCM)#use bcm mode.
GPIO.setup(channel, GPIO.OUT) ) # initialize GPIO.
# the relay must connect to 3.3V. if you connect the relay to 5V, it will not work correctly(use register.)


GPIO.output(channel, GPIO.LOW) # first of all, switch off
time.sleep(0.5)
GPIO.output(channel, GPIO.HIGH) # switch on
time.sleep(0.5)
GPIO.output(channel, GPIO.LOW) # switch off
time.sleep(0.5)
GPIO.cleanup() # very important commend for end GPIO. Do not skip this commend.
