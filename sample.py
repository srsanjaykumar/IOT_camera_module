import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

RED = 12
BLUE = 13
GREEN = 19

for channel in [RED , BLUE , GREEN]:
    GPIO.setup(channel, GPIO.OUT)


red = GPIO.PWM(RED, 1000)
blue = GPIO.PWM(BLUE, 1000)
green = GPIO.PWM(GREEN, 1000)

red.start(1)
blue.start(1)
green.start(1)

try:
    while True : 
        # for num in range(8):
            for i in range(101):
                sleep(0.1)
                red.ChangeDutyCycle(100 -i)
            sleep(1)
            for j in range(101):
                sleep(0.1)
                green.ChangeDutyCycle(100 - j)
            sleep(1)
            
            for k in range(101):
                sleep(0.1)
                blue.ChangeDutyCycle(100 -k)
            sleep(1)
    

except KeyboardInterrupt as e :
    red.stop()
    blue.stop()
    green.stop()
    GPIO.cleanup()
    