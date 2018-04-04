import RPi.GPIO as GPIO
import time
import threading

class Button (threading.Thread):
    def __init__(self,semaphore):
    # setting thread
        threading.Thread.__init__(self)
        self.semaphore = semaphore
    # setting button variables.
        self.buttonPing = 12
        self.groundPing = 6
        GPIO.setmode(GPIO.BOARD)
        self.pwm = GPIO.PWM(self.buttonPing, 50)  # Initialize PWM on pwmPin 100Hz frequency
        self.dc = 95  # duty cycle (0-100) for PWM pin

    def setButtonPing(self, buttonPing):
        self.buttonPing = buttonPing

    def setGroundPing(self,groundPing):
        self.groundPing = groundPing

    def getButtonPing(self):
        return self.buttonPing

    def getGroundPing(self):
        return self.groundPing


    def run(self):
        GPIO.setup(self.buttonPing, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print("Here we go! Press CTRL+C to exit")
        self.pwm.start(self.dc)
        try:
            while 1:
                self.semaphore.acquire()
                if GPIO.input(self.buttonPing):  # button is released
                   self.pwm.ChangeDutyCycle(self.dc)
                   pass # do random graph
                else:  # button is pressed:
                    self.pwm.ChangeDutyCycle(100 - self.dc)
                    print("Down")
                    time.sleep(0.015)
                self.semaphore.release()
        except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
            self.pwm.stop()  # stop PWM
            GPIO.cleanup()  # cleanup all GPIO



