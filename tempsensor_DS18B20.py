#!/usr/bin/env python

# SnoothDogg - 2019
# Built, Tested and working on RPi Zero W (13/11/19)

import glob
import time

while True:
   # change the device ID to whatever yours is. 
   # for 1-wire deployments, make sure you have at least a 4k7 ohm resistor from 3.3v to signal cable, otherwise you wont see therm in devices.
   # therm device will always start with 28*
   for sensor in glob.glob("/sys/bus/w1/devices/28-01145428d9aa/w1_slave"):
      id = sensor.split("/")[5]

      try:
         f = open(sensor, "r")
         data = f.read()
         f.close()
         if "YES" in data:
            (discard, sep, reading) = data.partition(' t=')
            t = float(reading) / 1000.0
            print("{} {:.1f}".format(id, t))
         else:
            print("999.9")

      except:
         pass
   
   # Will poll every 3 secs - increase or decrease as intended. 
   time.sleep(3.0)
