#!/usr/bin/env python3

#Script for serial communication with arduino-based board.
#Sends an ON/OFF on a preset time, sets an output state on a preset pin.

import serial
from datetime import datetime, date, time
from time import sleep

if __name__ == '__main__':
 ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) #TODO: Fix hardcode
 onTime = time(9, 20, 0)
 offTime = time(21, 20, 0) #TODO: Fix hardcode
 while True:
  currentTime = datetime.now().time()
  ser.flush()
  if currentTime.hour > offTime.hour and currnetTime.minute > offTime.minute: #TODO: this looks unelegant
   ser.write(bytes("OFF\n", 'utf-8'))
  elif currentTime.hour < onTime.hour and currnetTime.minute < onTime.minute:
   ser.write(bytes("OFF\n", 'utf-8'))
  else:
   ser.write(bytes("ON\n", 'utf-8'))
  sleep(5)
  ser.write(bytes(currentTime.strftime("%H:%M:%S"), 'utf-8'))
  ser.write(bytes("\n", 'utf-8')) #TODO: This is not elegant
