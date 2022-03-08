import RPi.GPIO as GPIO
from pynput.keyboard import Key, Controller

keyboard = Controller()

# 1, 7, 8, 25

GPIO.setmode(GPIO.BCM)

GPIO.setup(1, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(1, GPIO.HIGH)
GPIO.output(25, GPIO.HIGH)

def callback(channel):
    print(channel)
    keyboard.press('a')

GPIO.add_event_detect(7, GPIO.RISING, callback=callback, bouncetime=100)
GPIO.add_event_detect(8, GPIO.RISING, callback=callback, bouncetime=100)

while True:
    pass