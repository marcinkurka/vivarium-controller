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
  pin1 = 9
  pwm1 = 0
  pin2 = 3
  pwm2 = 0
  if currentTime > onTime or currentTime < offTime: #TODO: this looks unelegant
   pwm1 = 255
   pwm2 = 255
  msgDict = {
   "Light1": [pin1, pwm1],
   "Light2": [pin2, pwm2],
  }
  msgToSend = json.dumps(msgDict)
  ser.write(msgToSend.encode('ascii'))
  sleep(0.1)
  incoming = ser.readline().decode("utf-8")
  #print (incoming)
  sleep(0.05)
  #ser.write(bytes(currentTime.strftime("%H:%M:%S"), 'utf-8'))
  #ser.write(bytes("\n", 'utf-8')) #TODO: This is not elegant
