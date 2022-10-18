# Lab 3 Starting Script
# ENGI1020 - Fall 2022

from engi1020.arduino.api import *
from time import sleep

threshold = 400 # Variable to hold threshold value



while True: # TODO Procedure 2.2 - Convert to infinite loop
    
    
    # TODO Procedure 2.1 - Replace with required code to read sensor, print, wait
    light_sensor = analog_read(6)
    print(f"the light sensore is reading {light_sensor} what ever units this thing records it in")
    sleep(1)


    # Procedure Step 2.3 - Include threshold conditional check


    if light_sensor <= threshold: digital_write(4, True)
    elif digital_read(6) == True:
        digital_write(4, False)



    # Procedure Step 2.4 - Within threshold conditional, include button-dependant alarm loop
     
