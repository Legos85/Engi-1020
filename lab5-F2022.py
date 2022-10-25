# ENGI 1020
# Starting script file for Lab 5
# References to Lab 5 Preparation and Procedure below

from engi1020.arduino.api import *
from time import sleep

# "Stub" or placeholder function for 3.1 Implementation
# TODO 3.1 - Use answers from Preparation to determine what parameters this function needs
def lab5_dataCollect(pin,sample_count,time):
    """
    Reads sampleCount samples from analogPin at waitTime seconds interval
    Returns collected data in a list

    pin(int): pin it uses
    sample_count(int): amount of iterations it does
    time(float): time it waits in seconds
    """
    datalist = []
    for data in range(int(sample_count)):
        data = analog_read((pin))
        sleep(time)

        datalist.append(data)
    return(datalist)

    #TODO 3.1 - Replace with implementation of algorithm
    
#TODO 3.2 - call your defined function here
# so that the list will contain 25 samples from the analog rotary dial, separated by 0.25 seconds

test = lab5_dataCollect(6,100,0.1)



# Replace the 0 with the average calculation 
rotaryAverage = int((sum(test)/len(test)))

print(f"Here is my rotary data: {test} ") #Print your list here
print("Here is the average:", rotaryAverage)

#TODO 3.3 - Implement code to manipulate your output device



for element in test:
    
    if element > rotaryAverage:
        rgb_lcd_colour(255,0,0)
        sleep(1)
    if element < rotaryAverage:
        rgb_lcd_colour(0,0,255)
        sleep(1)
    if element == rotaryAverage:
        rgb_lcd_colour(0,255,0)
        sleep(1)
    else:
        pass

rgb_lcd_clear()