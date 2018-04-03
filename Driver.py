import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.out)
class driver:
    def __init__(self,ping):
        self.ping = ping
        time.sleep(1)
        GPIO.output(7,False)
        time.sleep(1)
