# Starting script file for Lab 4
from engi1020.arduino.api import *
from time import sleep

# List you can use in your implementation
dataList1 = []

# Procedure 2.1, implement sample collection loop
# TODO 2.1 - Implement definite loop
# Think about how many iterations, and what needs to happen each time?

for data in range(10):
    data = analog_read(0)
    sleep(1)

    dataList1.append(data)

sampleCount1 = len(dataList1)

# Procedure 2.2, implement statistics

sumdata = 0

# TODO 2.2 - Implement definite loop to calculate sumSamples

for data in dataList1:
    sumdata += data

# TODO 2.2 - Calculate average of samples

average_sample = sumdata / sampleCount1

# Procedure 2.3
print(average_sample)
print(dataList1)

x = 0
for element in dataList1:
    
    if element > average_sample:
        digital_write(4,True)
        x += 1
        sleep(1)
        digital_write(4,False)
        sleep(1)
    else:
        sleep(1)
oled_print(x)
sleep(5)
oled_clear
    # TODO 2.3 - Manipulate output based on comparison!!
