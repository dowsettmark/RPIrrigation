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


########################################

# Notes
#use the definition above in the code below
#work out how to use screen
#run as a cron job
#test run the hydro setup


#Import the necessary libraries
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#Setup pin 18 as an output
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

#This function turns the valve on and off in 10 sec. intervals. 
def valve_OnOff(Pin):
    while True:
        GPIO.output(18, GPIO.HIGH)
        print("GPIO HIGH (on), valve should be off") 
        time.sleep(10) #waiting time in seconds
        GPIO.output(18, GPIO.LOW)
        print("GPIO LOW (off), valve should be on")
        time.sleep(10)

valve_OnOff(18)

GPIO.cleanup()
