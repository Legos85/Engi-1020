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

sumSamples = 0

# TODO 2.2 - Implement definite loop to calculate sumSamples
#why do we have to use a loop for this :(
for data in dataList1:
    sumdata = dataList1[0] + dataList1[1] + dataList1[2] + dataList1[3] + dataList1[4] + dataList1[5] + dataList1[6] + dataList1[7] + dataList1[8] + dataList1[9]

# TODO 2.2 - Calculate average of samples

average_sample = sumdata / sampleCount1

# Procedure 2.3

for element in dataList1:
    print("Compare and manipulate!")
    # TODO 2.3 - Manipulate output based on comparison!!