#!/usr/bin/env python

# SnoothDogg - 2019
# Tested and working on RPi Zero W (13/11/19)

import glob
import time

while True:
   # change the device ID to whatever yours is. 
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

   time.sleep(3.0)
