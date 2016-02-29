#!/usr/bin/python

# Import required Python libraries
import RPi.GPIO as GPIO
import time
import random

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [15, 16, 21, 26]
random.shuffle(pinList)

SleepTimeL = 2
SleepTimeD = 3
SleepTimeE = 5

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setwarnings(False)
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.LOW)

def trigger() :
        for i in pinList:
          GPIO.output(i, GPIO.HIGH)
	  print "%d ...nyala" % i
	  time.sleep(SleepTimeL);
	  GPIO.output(i, GPIO.LOW)
	  print "%d ...mati" % i
	  time.sleep(SleepTimeD);
	  GPIO.output(i, GPIO.HIGH)
	  print "%d ...nyala" % i
	  time.sleep(SleepTimeL);
	  GPIO.output(i, GPIO.LOW)
	  print "%d ...mati" % i
	  time.sleep(SleepTimeD);
          #GPIO.cleanup()
          #break
     

try: 
    for z in range(0, 15):
	trigger()
    
    print "   Selesai"
    GPIO.cleanup()     
      
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
