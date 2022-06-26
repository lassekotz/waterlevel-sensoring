import RPi.GPIO as GPIO
from time import sleep

pins = [24, 23, 25]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins[0], GPIO.OUT)
    GPIO.setup(pins[1], GPIO.OUT)
    GPIO.setup(pins[2], GPIO.OUT)


def loop():
    # Going forwards
    GPIO.output(pins[0], GPIO.HIGH)
    GPIO.output(pins[1], GPIO.LOW)
    GPIO.output(pins[2], GPIO.HIGH)

    sleep(5)
    # Going backwards
    GPIO.output(pins[0], GPIO.LOW)
    GPIO.output(pins[1], GPIO.HIGH)
    GPIO.output(pins[2], GPIO.HIGH)

    sleep(5)
    # Stop
    GPIO.output(pins[2], GPIO.LOW)


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()