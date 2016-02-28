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

# perulangan utama

try:
  GPIO.output(27, GPIO.LOW)
  print "SATU"
  time.sleep(WaktuTidurL);
  GPIO.output(27, GPIO.HIGH)
  print "Satu nyala"
  time.sleep(WaktuTidurL);
  GPIO.output(17, GPIO.LOW)
  print "DUA"
  time.sleep(WaktuTidurL);
  GPIO.cleanup()
  print "Dadah........!"

# Akhiri program dengan papan ketik
except KeyboardInterrupt:
  print "  Program ditutup"

  # Reset GPIO
  GPIO.cleanup()

