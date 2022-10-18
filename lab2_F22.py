# ENGI1020 Fall 2022
# Starting Script of Lab 2

from engi1020.arduino.api import *

#Menu system to choose which design you wish to test
print("Welcome to Lab 2 Script!")
choice = input("Enter 1 to test Design 1 or 2 to test Design 2: ")

#Implemented decision-making based on choice!
if choice == "1":
  print("You've decided to test Design 1")
  
  #STUDENT TODO 2.2 - Implement read of button, storing value to variable
  print("Variable value?")
  dig_val = digital_read(6)
  print(dig_val)

  #STUDENT TODO - Implement Design 1 here!
  if dig_val == True:
   digital_write(4, True)
  else: digital_write(4,False)

  
  
elif choice == "2":
  print("You've decided to test Design 2")

  #STUDENT TODO 2.2 - Implement read of analog sensor, storing value to variable
  print("Variable value?")
  ana_val = analog_read(6)
  print(ana_val)
  
  #STUDENT TODO - Implement Design 2 here!
  if ana_val >= 511:
    oled_print("HIGH")
  else: oled_print("LOW")

  
else:
  print("Invalid choice, please rerun script and try again!")
  
