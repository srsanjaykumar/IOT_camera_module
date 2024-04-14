import RPi.GPIO as GPIO
from time import sleep
from colour import Color


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


try:
    light = RGBA(12, 13, 19)
    while True:
        try:
            # light.setColor(0,255,0)
            # light.setRGBColor(Color(input("Enter any color :")).rgb)
            # light.setRGBColor((100 , 0, 100))
            # light.setRGBColor((100, 100, 0))
            # light.setRGBColor((0,100,100))
            # c = Color("red").range_to(Color("blue"),100)
            # print(c)
            # for i in c :
            #     print(i)
            #     light.setRGBColor(i.rgb)
            #     sleep(0.1)
            
            while True:
                rtb = Color("red").range_to(Color("blue"), 100)
                gtr = Color("green").range_to(Color("cyan"), 100)
                for i in rtb:
                    light.setRGBColor(i.rgb)
                    sleep(0.1)
                print("Done 1")
                for j in gtr:
                    light.setRGBColor(j.rgb)
                    sleep(0.1)
                print("Done 2")
        except Exception as e:
            print("Colour not found ....")
            continue


except KeyboardInterrupt as e:
    print("Clicking -> ctrl + C ")

finally:
    GPIO.cleanup()
