# Notes
#work out how to use screen
#run as a cron job
#test run the hydro setup


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
