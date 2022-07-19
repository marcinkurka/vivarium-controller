#!/usr/bin/env python3

#Script for serial communication with arduino-based board.
#Sends a string based on an input prompt

import serial
import time

if __name__ == '__main__':
 ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) #TODO: Fix hardcode
 while True:
  ser.flush()
  pinToToggle = input("Please insert number of the pin to toggle: ")
  ser.write(bytes(pinToToggle,'utf-8'))
