#!/usr/bin/python
# Samsul Ma'arif <info@samsul.web.id>
#
# PTK Mahnetik, 28 Februar 2016 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# buat daftar nomr pin

daftarPin = [27, 17]

# loop (perulangan) untuk pin

for i in daftarPin:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)

# waktu antara operasi perulangan

WaktuTidurL = 2
WaktuTidurS = 0.5

# perulangan utama

try:
  while True:

    for z in daftarPin:
	GPIO.output(z, GPIO.LOW)
	print z
  	print "...mati"
  	time.sleep(WaktuTidurS);
  	GPIO.output(z, GPIO.HIGH)
  	print "...nyala"
  	time.sleep(WaktuTidurL);
  	#GPIO.cleanup()
  	#print "Dadah........!"

# Akhiri program dengan papan ketik
except KeyboardInterrupt:
  print "  Program ditutup"

  # Reset GPIO
  GPIO.cleanup()

