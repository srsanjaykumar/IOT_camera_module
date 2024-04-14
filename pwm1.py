import RPi.GPIO as GPIO
from time import sleep

channel = 12
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, 1000)
print("Pwm Starting ...")
p.start(0)

try:
    while 1 :
        print("High")
        for dc in range(0,100,1):
            p.ChangeDutyCycle(dc)
            sleep(0.01)
        sleep(1)
        print("Low")
        for dc in range(100,0,-1):
            p.ChangeDutyCycle(dc)
            sleep(0.01)        
        sleep(1)
except KeyboardInterrupt as e :
    print("Problem Occur ")
    p.stop() 
    GPIO.cleanup()
p.stop()    
GPIO.cleanup()