#!/usr/bin/env python3

#Script for serial communication with arduino-based board.
#Sends a json

import time
import json
import serial
from pprint import pprint
import random

if __name__ == '__main__':
 ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) #TODO: Fix hardcode
 while True:
  ser.flush()
  pin1 = input("Please insert pin 1: ")
  pwm1 = input("Please insert pwm 1: ")
  pin2 = input("Please insert pin 2: ")
  pwm2 = input("Please insert pwm 2: ")
  #ser.write(bytes(pinToToggle,'utf-8'))
  msgDict = {
   "Light1": [pin1,pwm1],
   "Light2": [pin2,pwm2],
  }
  msgToSend = json.dumps(msgDict)
  print(msgToSend)
  ser.write(msgToSend.encode('ascii'))
  time.sleep(0.1)
  incoming = ser.readline().decode("utf-8")
  print (incoming)
  time.sleep(0.5)
