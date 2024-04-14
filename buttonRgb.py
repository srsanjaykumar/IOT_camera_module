import RPi.GPIO as GPIO
from time import sleep
from colour import Color
import time 
from threading import Thread

GPIO.setmode(GPIO.BCM)
button = 4
GPIO.setup(button, GPIO.IN)
speed = 0.1 


class RGBA():
    def __init__(self, r, g, b):
        GPIO.setmode(GPIO.BCM)
        channel = [r, g, b]
        for ch in channel:
            GPIO.setup(ch, GPIO.OUT)
        self.r = GPIO.PWM(r, 60)
        self.g = GPIO.PWM(g, 60)
        self.b = GPIO.PWM(b, 60)
        self.r.start(0)
        self.g.start(0)
        self.b.start(0)

    def setColor(self, r, g, b):
        print("Setting Color ...")
        print("r =", (r/255)*100)
        print("g =", (g/255)*100)
        print("b =", (b/255)*100)
        r = 100 - (r/255)*100
        g = 100 - (g/255)*100
        b = 100 - (b/255)*100
        print("r = = ", r)
        print("g = = ", g)
        print("b = = ", b)
        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))

    # 0 -100 for colors module
    def setRGBColor(self, rgb):
        # print(rgb)
        r = abs(rgb[0]*100 - 100)
        g = abs(rgb[1]*100 - 100)
        b = abs(rgb[2]*100 - 100)
        # print(r, g, b)
        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))


def rgb_transition_thread():
    light = RGBA(12, 13, 19)
    while True:
        rtb = Color("red").range_to(Color("blue"), 100)
        gtr = Color("blue").range_to(Color("red"), 100)
        for i in rtb:
            light.setRGBColor(i.rgb)
            sleep(speed)
  
        for j in gtr:
            light.setRGBColor(j.rgb)
            sleep(speed)


t = Thread(target=rgb_transition_thread)
t.start()
stime=None
try:
    while True:
        if (GPIO.input(button) == GPIO.HIGH):
            # print( "Button  Pressed ...\n")
            sleep(0.1)
            if stime == None:
                stime = time.time()
            else:
                speed =   time.time() - stime
                print("Speed => ", speed)
                stime = None 
            
except KeyboardInterrupt as e:
    print("Clicking -> ctrl + C ")
    
    GPIO.cleanup()

finally:
    GPIO.cleanup()
