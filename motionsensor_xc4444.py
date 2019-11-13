## Credit - https://www.rototron.info

## Snoothdogg 
# Built and tested on RPi Zero W and XC4444

from Adafruit_CharLCD import Adafruit_CharLCD

lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=11, cols=16, lines=2)
lcd.clear()

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering

# Set up input pin
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set up LED output
GPIO.setup(20, GPIO.OUT)

# Callback function to run when motion detected
def motionSensor(channel):
    GPIO.output(20, GPIO.LOW)
    if GPIO.input(21):     # True = Rising
        global counter
        counter += 1
        GPIO.output(20, GPIO.HIGH)
        print "Motion Detected"
        print "Dection count: " + str(counter) + "\n"

# add event listener on pin 21
GPIO.add_event_detect(21, GPIO.BOTH, callback=motionSensor, bouncetime=1)
counter = 0

try:
    while True:
        sleep(1)         # wait 1 second

finally:                   # run on exit
    GPIO.cleanup()         # clean up
    print "All cleaned up."
