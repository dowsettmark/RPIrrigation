# Notes
#work out how to use screen
#run as a cron job
#test run the hydro setup
#check GPIO-Python-code-2.py - compare to what i have below
#continue running jobs after the server connection breaks

#water discharge baffle required to prevent splash 

#Integrate water level - and link in pump cut out
#Itegrate moisture Measurement
#integrate temp and humidity
#Integrate light sensor
#reporting and web interface through plotty or control mypi

#import RPi.GPIO as gpio
#import time

#gpio.setmode(gpio.BCM)
#gpio.setup(18, gpio.OUT)
#while True:
 # time.sleep(2)
 # gpio.output(18, True)
 # print "True"
 #time.sleep(2)
 # gpio.output(18, False)
 # print "False"


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

#might need to get rid of this line
valve_OnOff(18)

GPIO.cleanup()
