import RPi.GPIO as GPIO
channel = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, 1000 ) # 1000 hz to avoid Camera Flickering 
p.start(100)
i = None

try:
    while i != 'q':
        try:
            d = input("Set duty Cycle = ") # Brigntness
            f = input("Set Frequency  = ") # Pulses 

            if (d == 'q' or f == 'q'):
                break
            p.ChangeDutyCycle(int(d))
            p.ChangeFrequency(int(f))
        except ValueError as e:
            pass
except KeyboardInterrupt as e:
    print("pressing  Ctrl + C  -> Qutting ...")
    pass

p.stop()
GPIO.cleanup()


# Pins Usings   
 
# Ground  
# GPIO pwm Pin  =>   channel number 
