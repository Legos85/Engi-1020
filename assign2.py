#had to check to see if a car will hit an object or not

#asks if there is an obstical ahead
print("is there a obstical ahead?")
#their input
choice = input("Y/N: ")

if choice == "Y":
    #checking the speed of the car and how far away it is from the object
    v = float(input("What is the speed of the car in km/h?: "))
    object_distance = float(input("How far away is the object in m?: "))
    
    #making sure that they give a possible response
    if v  <= 0 or object_distance <= 0: 
        print("Invalid response")
    else:  
        #changing from km/h to m/s
        v_ms = v/3.6
        #pluging that into a kniematics equation to get distance need to stop
        d = (-(v_ms**2) / (2 * (-4.5)))
        #checking to see if they can stop before hitting the object
        if d < object_distance:
            print("Brake!!!")
        else: print("Brace for impact!!!")

elif choice == "N":
    print("Drive ahead")

else: print("Invalid response")
