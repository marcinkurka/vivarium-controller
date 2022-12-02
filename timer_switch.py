#!/usr/bin/env python3

#Script for serial communication with arduino-based board.
#Sends an ON/OFF on a preset time, sets an output state on a preset pin.

import serial
from datetime import datetime, date, time
from time import sleep
import json
import pandas as pd

if __name__ == '__main__':
 ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) #TODO: Fix hardcode
 lightSchedule1 = pd.read_csv("/home/pi/vivarium-controller-production/vivarium-controller/LightSchedule1.dat", sep = "\t", names = ("Hour", "Intensity"))
 lightSchedule2 = pd.read_csv("/home/pi/vivarium-controller-production/vivarium-controller/LightSchedule2.dat", sep = "\t", names = ("Hour", "Intensity"))
 pin1 = 9
 pwm1 = 0
 pin2 = 3
 pwm2 = 0
 while True:
  currentTime = datetime.now().time()
  ser.flush()
  currentParams1 = lightSchedule1[lightSchedule1["Hour"] == datetime.now().strftime("%H:%M:%S")]
  currentParams2 = lightSchedule2[lightSchedule2["Hour"] == datetime.now().strftime("%H:%M:%S")]
  pwm1 = int(currentParams1["Intensity"].iloc[0])
  pwm2 = int(currentParams2["Intensity"].iloc[0])
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
