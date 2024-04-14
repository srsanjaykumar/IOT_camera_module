
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
            i = (input("Enter the number between 0-7: "))
            if (i == 'q'):
                GPIO.cleanup(channel)
                print("You are Quitting  ....")
                break
            i = int(i)
            if (i < 0 or i >= 8):
                print("Invalid Range of Input ... Try Again ... ")
                continue

            rgb = format(i, '03b')
            print('rgb =:>', rgb)
            for i, c in enumerate(channel):
                print(i, c, rgb[i], int(rgb[i]))
                GPIO.output(c, not bool(int(rgb[i])))
        except ValueError as e:
            print("Invalid input ,  Try Again...")

except KeyboardInterrupt as e:
    GPIO.cleanup(channel)
    print("Quitting using ctrl + C  ....")


