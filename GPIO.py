import RPi.GPIO as GPIO
from time import sleep

channel =[17,27]

# set the mode  for BCM   that means it can connect from GPIO pins
GPIO.setmode(GPIO.BCM)

# target channels are used to get input and output
GPIO.setup(channel,GPIO.OUT)


while True:
    # High refers to turn on light 
    GPIO.output(17,GPIO.HIGH)
    # Low refers to turn off light 
    GPIO.output(27,GPIO.LOW)
    sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.HIGH)
    sleep(0.3)
    


# finally it will clear the GPIO target channels  
GPIO.cleanup(channel)