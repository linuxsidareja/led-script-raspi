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

SleepTimeL = 0.7
SleepTimeD = 1
SleepTimeE = 0.3

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setwarnings(False)
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.LOW)

def nyala() :
        for i in pinList:
          GPIO.output(i, GPIO.HIGH)
	  print "%d ...nyala" % i
	  time.sleep(SleepTimeL);

def mati() :
	for i in pinList:	  
	  GPIO.output(i, GPIO.LOW)
	  print "%d ...mati" % i
	  time.sleep(SleepTimeD);

def nyate() :
	for i in pinList:
	  GPIO.output(i, GPIO.HIGH)
	  print "%d ...nyala" % i
	  time.sleep(SleepTimeE);
	  GPIO.output(i, GPIO.LOW)
	  print "%d ...mati" % i
	  time.sleep(SleepTimeE);
          #GPIO.cleanup()
          #break
     

try: 
    for z in range(0, 15):
	print "%d ....nyala semua" % z
	nyala()
	print "%d ...mati semua" % z
	mati()
	print "%d ..nyala mati" %z
	nyate()
    
    print "   Selesai"
    GPIO.cleanup()     
      
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
