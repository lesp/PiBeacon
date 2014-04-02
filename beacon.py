#We import four modules, to control time, enable us to use the GPIO, setup PiFm to broadcast the signal and finally enable us to access files on the operating system.
from time import *
import RPi.GPIO as GPIO
import PiFm
import os

#These two variables control the pins used for our input, which is a button and for our output which is an LED.
button_pin = 8
led_pin = 12
buzzer = 26
#We setup the GPIO pins to use a logical numbering sequence, with the left column being odd numbers, and the right column being the even numbers.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button_pin , GPIO.IN)
GPIO.setup(led_pin , GPIO.OUT)
GPIO.setup(buzzer , GPIO.OUT)
#Import the PiGlow module
from piglow import PiGlow

piglow = PiGlow()

while True:
    if GPIO.input(button_pin)==1:
	print("BUTTON PRESSED")
        #GPIO.output(led_pin, True)
        #sleep(2)
        #GPIO.output(led_pin, False)
        #sleep(2)
        #os.system('sudo python /home/pi/piflash.py &')
        PiFm.play_sound("/home/pi/sound.wav")
        for i in range(0,3):
            GPIO.output(buzzer, True)
            piglow.all(128)
            sleep(0.5)
            GPIO.output(buzzer, False)
            piglow.all(0)
            sleep(0.5)
            GPIO.output(buzzer, True)
            piglow.all(128)
            sleep(0.5)
            GPIO.output(buzzer, False)
            piglow.all(0)
            sleep(0.5)
            GPIO.output(buzzer, True)
            piglow.all(128)
            sleep(0.5)
            GPIO.output(buzzer, False)
            piglow.all(0)
            sleep(1)
            GPIO.output(buzzer, True)
            piglow.all(128)
            sleep(1)
            GPIO.output(buzzer, False)
            piglow.all(0)
            sleep(1)
            GPIO.output(buzzer, True)
            piglow.all(128)
            sleep(1)
            GPIO.output(buzzer, False)
            piglow.all(0)
            sleep(1)
            GPIO.output(buzzer, True)
            piglow.all(128)
            sleep(1)
            GPIO.output(buzzer, False)
            piglow.all(0)
            sleep(1)
    else:
        print ("Waiting for input")
        piglow.all(0)
