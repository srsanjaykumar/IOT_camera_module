
import RPi.GPIO as GPIO
from time import sleep

channel = [12, 13, 19]

# set the mode  for BCM   that means it can connect from GPIO pins
GPIO.setmode(GPIO.BCM)

# target channels are used to get input and output
for c in channel:
    GPIO.setup(c, GPIO.OUT)

# GPIO.output(17,GPIO.HIGH)
# GPIO.output(27,GPIO.LOW)

try:
    while True:
        try:
            for j in range(1,8):
                rgb = format(j, '03b')
                print('rgb =:>', rgb)
                for i, c in enumerate(channel):
                    print(i, c, rgb[i], int(rgb[i]))
                    GPIO.output(c, not bool(int(rgb[i])))
                sleep(0.4)
        except ValueError as e:
            print("Error Occurs ,  Try Again...")

except KeyboardInterrupt as e:
    GPIO.cleanup(channel)
    print("Quitting using ctrl + C  ....")