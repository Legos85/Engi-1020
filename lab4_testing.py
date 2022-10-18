from curses import pair_number
from engi1020.arduino.api import *
from time import sleep

datalist = []

#getting 10 samples from a dial and adding them to a list

for data in range(10):
    data = analog_read(0)
    sleep(1)

    datalist.append(data)

print(datalist)

#finding the sum of the list

sumlist1 = sum(datalist)

#for some reason they don't want us using the sum funtion just to check. this hurts me

for data in datalist:
    pima = datalist[0] + datalist[1] + datalist[2] + datalist[3] + datalist[4] + datalist[5] + datalist[6] + datalist[7] + datalist[8] + datalist[9]

print(pima)
print(sumlist1)

print(sumlist1 / len(datalist))

sumbad1 = sum(datalist[1:9])
sumgood1 = sum(datalist[0:5])


