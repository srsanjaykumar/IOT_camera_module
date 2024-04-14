import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setmode(GPIO.BCM)
channel = 4
GPIO.setup(channel, GPIO.IN)

while True:
    if (GPIO.input(channel) == GPIO.LOW):
        print( "Button  UN  Pressed ...\n", str(
            time.time()), GPIO.input(channel))
        sleep(0.1)
     
    # else:
    #     print("BUtton Pressed",GPIO.input(channel))
