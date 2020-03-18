import RPi.GPIO as GPIO
import time
# Function to control the base motor
def basemotor(degree):
    GPIO.setup(7,GPIO.OUT)
    p = GPIO.PWM(7,50)
    # p.start(degree)
    p.ChangeDutyCycle(degree)
    print("Base motor should move "+str(degree)+" degree")

def abovebasemotor(degree):
    GPIO.setup(8,GPIO.OUT)
    p = GPIO.PWM(8,50)
    # p.start(degree)
    p.ChangeDutyCycle(degree)
    print("Motor above base should move "+str(degree)+" degree")


def midmotor(degree):
    GPIO.setup(10,GPIO.OUT)
    p = GPIO.PWM(10,50)
    # p.start(degree)
    p.ChangeDutyCycle(degree)
    print("Mid motor should move "+str(degree)+" degree")

def clawrotatemotor(degree):
    GPIO.setup(11,GPIO.OUT)
    p = GPIO.PWM(11,50)
    # p.start(degree)
    p.ChangeDutyCycle(degree)
    print("Claw rotate motor should move "+str(degree)+" degree")

def clawmotor(degree):
    GPIO.setup(12,GPIO.OUT)
    p = GPIO.PWM(12,50)
    # p.start(degree)
    p.ChangeDutyCycle(degree)
    print("Claw motor above base should move "+str(degree)+" degree")

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    while True:
        x = input("Enter 1 for base, 2 for above base, 3 for mid motor, 4 for claw rotate motor and 5 for claw motor:")
        v = input("Value:")
        if x == 1:
            basemotor(v)
        elif x == 2:
            abovebasemotor(v)
        elif x == 3:
            midmotor(v)
        elif x == 4:
            clawrotatemotor(v)
        elif x == 5:
            clawmotor(v)