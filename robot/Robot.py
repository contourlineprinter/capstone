#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafru$
import RPi.GPIO as GPIO
import time
import atexit
import threading

STEPS_PER_ROTATION = 828

class Robot(object):

    def __init__(self, speed=30, stepstyle='double', stop_at_exit=True, n$
        self.marker = Marker(15,7,11,13)
        self.marker.standby()
        time.sleep(naptime)
        self.mh = Adafruit_MotorHAT()
        self.mleft = self.mh.getStepper(513, 1)
        self.mright = self.mh.getStepper(513, 2)
        self.speed = speed
        self.mleft.setSpeed(self.speed)
        self.mright.setSpeed(self.speed)
        self.naptime = naptime

        # create empty threads (these will hold the stepper 1 and 2 threa$
        self.st1 = threading.Thread()
        self.st2 = threading.Thread()

        # Other option could be  Adafruit_MotorHAT.INTERLEAVE, Adafruit_M$
        # but for our application single and double are only appropriate
        if stepstyle.lower() == 'single':
            self.stepstyle = Adafruit_MotorHAT.SINGLE
        else:
            self.stepstyle = Adafruit_MotorHAT.DOUBLE


        # Start with motors turned off.
        #self.mleft.run(Adafruit_MotorHAT.RELEASE)
        #self.mright.run(Adafruit_MotorHAT.RELEASE)
        # Configure all motors to stop at program exit if desired.
        #if stop_at_exit:
        #   atexit.register(self.stop)

    def stepper_worker(self, stepper, numsteps, direction, style):
        stepper.step(numsteps, direction, style)

    # recommended for auto-disabling motors on shutdown!
    def turnOffMotors(self):
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
        #atexit.register(turnOffMotors)

    def forward(self, steps):
        print('forward start')
        self.marker.down()
        if not self.st1.isAlive():
            self.st1 = threading.Thread(target=self.stepper_worker, args=$

        if not self.st2.isAlive():
            self.st2 = threading.Thread(target=self.stepper_worker, args=$
        time.sleep(0.2)
        self.st2.start()
        self.st1.start()

        self.st1.join()
        self.st2.join()
        time.sleep(self.naptime)
        print('forward end')

    def move(self, steps):
        print('move start')
        self.marker.up()
        if not self.st1.isAlive():
            self.st1 = threading.Thread(target=self.stepper_worker, args=$

        if not self.st2.isAlive():
            self.st2 = threading.Thread(target=self.stepper_worker, args=$
        time.sleep(0.2)
        self.st2.start()
        self.st1.start()

        self.st1.join()
        self.st2.join()
        self.marker.down()
        time.sleep(self.naptime)
        print('move end')

    def right(self, steps):
        print('right start')
        self.marker.up()
        if not self.st1.isAlive():
            self.st1 = threading.Thread(target=self.stepper_worker, args=$

        if not self.st2.isAlive():
            self.st2 = threading.Thread(target=self.stepper_worker, args=$
        time.sleep(0.2)
        self.st2.start()
        self.st1.start()
        #time.sleep(0.1)
        self.st1.join()
        self.st2.join()
        self.marker.down()
        time.sleep(self.naptime)
        print('right end')


    def left(self, steps):
        print('left start')
        self.marker.up()
        if not self.st1.isAlive():
            self.st1 = threading.Thread(target=self.stepper_worker, args=$

        if not self.st2.isAlive():
            self.st2 = threading.Thread(target=self.stepper_worker, args=$
        time.sleep(0.2)
        self.st2.start()
        self.st1.start()
        # time.sleep(0.1)
        self.st1.join()
        self.st2.join()
        self.marker.down()
        time.sleep(self.naptime)
        print('left end')


    def rotate(self, theta):
        #make theta make sense

        while theta >= 360:
            theta = theta - 360

        if theta > 180:
            theta = -1 * (360-theta)
        elif theta < -180:
            theta = 360+theta

        steps = int((theta * STEPS_PER_ROTATION) / 360)

        print('theta =', theta, 'steps =',steps)
        if steps > 0:
            self.right(steps)
        else:
            self.left(abs(steps))


    def cleanup(self):
        GPIO.cleanup()
        self.turnOffMotors()


class Led:

    def __init__(self, pin_num):
        GPIO.setmode(GPIO.BOARD)
        self.pin = pin_num
        self.status = 'off'
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        self.status = 'on'
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        self.status = 'off'
        GPIO.output(self.pin, GPIO.LOW)



class Marker:

    def __init__(self, pin_num, pred, pgreen, pblue):
        GPIO.setmode(GPIO.BOARD)
        self.pin = pin_num
        self.status = 'down'
        GPIO.setup(self.pin, GPIO.OUT)
        self.red = Led(pred)
        self.green = Led(pgreen)
        self.blue = Led(pblue)

    def standby(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.red.off()
        self.green.off()
        self.blue.on()

    def down(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.status = 'down'
        self.red.off()
        self.blue.off()
        self.green.on()

    def up(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.status = 'up'
        self.blue.off()
        self.green.off()
        self.red.on()
