import RPi.GPIO as GPIO
from time import sleep
# import uinput
from pynput.keyboard import Key, Controller

keyboard = Controller()

# 1, 7, 8, 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.OUT)
GPIO.output(1, GPIO.HIGH)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.HIGH)

while True:
    sleep(1/30)
# with uinput.Device([uinput.KEY_A, uinput.KEY_B]) as device:
    if GPIO.input(7) == 1: 
        print("Button7 is pressed")
        # device.emit_click(uinput.KEY_A)
        keyboard.press('a')
    if GPIO.input(8) == 1: 
        print("Button8 is pressed")
        # device.emit_click(uinput.KEY_B)
        keyboard.press('b')
    sleep(1/30)

