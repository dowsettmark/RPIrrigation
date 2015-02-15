# Notes
#work out how to use screen
#run as a cron job
#test run the hydro setup
#check GPIO-Python-code-2.py - compare to what i have below

#!/usr/bin/env python
#import the GPIO library
import RPi.GPIO as GPIO
#select the board mode pin numbering
GPIO.setmode(GPIO.BOARD)
#set the needed GPIO pins as output
GPIO.setup(11, GPIO.OUT) #relay 1
GPIO.setup(12, GPIO.OUT) #relay 2
GPIO.setup(13, GPIO.OUT) #relay 3
GPIO.setup(15, GPIO.OUT) #relay 4
#toggle the relays
GPIO.output(13,True) #Enable relay 3 
GPIO.output(11,False) #Disable relay 1

#########################################

import RPi.GPIO as GPIO
from time import sleep

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# Set relay pins as output
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

while (True):
    
    # Turn all relays ON
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)
    # Sleep for 5 seconds
    sleep(5) 
    # Turn all relays OFF
    GPIO.output(18, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)   
    # Sleep for 5 seconds
    sleep(5)
    
########################################



#Import the necessary libraries
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

#Setup pin 18 as an output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

#This function turns the valve on and off in 30 sec. intervals. 
def valve_OnOff(Pin):
    while True:
        GPIO.output(18,True) #may need to change to GPIO.OUT?
        print("Pump should be on") 
        time.sleep(30) #waiting time in seconds
        GPIO.output(18,False)
        print("Pump should be OFF")
        time.sleep(30)

valve_OnOff(18)

GPIO.cleanup()
