print("is there a obstical ahead?")
choice = input("Y/N: ")

if choice == "Y":
    v = float(input("What is the speed of the car in km/h?: "))
    object_distance = float(input("How far away is the object in m?: "))
    
    if v  <= 0 or object_distance <= 0: 
        print("Invalid response")
    else:  
        
        v_ms = v/3.6
        d = (-(v_ms**2) / (2 * (-4.5)))
    
        if d < object_distance:
            print("Brake!!!")
        else: print("Brace for impact!!!")

elif choice == "N":
    print("Drive ahead")

else: print("Invalid response")
