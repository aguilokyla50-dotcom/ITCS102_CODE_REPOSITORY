route = ["TERMINAL","PEREZ PARK", "PACIFIC MALL"]
passenger =[]
SEATS = 6 
FARE = 13
total = 0

while True:
    print("sakay: ", passenger)
    print(len(passenger), " of ",SEATS , "seats")
    print("1 sakay 2 priority 3 para po!")
    print("4 baba sa pinto 5 baba sa harap")
    print("6 Seat check 8 Balikan 9 Exit")
    choice = input("CHOICE : ")

    if choice == "1":
        if len (passenger) == SEATS:
            print(" PNO NA! ")
        else:
            name = input("name: ")
            passenger.append (name)
            total = total + FARE
            print(name, " boarded at the back ")

    elif choice == "2":
        if len(passenger)== SEATS:
            print(" PUNO NA! ")
        else:
            name = input ("NAME: ")
            passenger.insert(0, name )
            total = total + FARE
            print( name, "TOOK THE PRIORITY SEAT")

    elif choice  == "3":
        name = input(" WHO IS GETTING OFF?")
        if name in passenger:
            passenger.remove(name)
            print(name, "GOT OFF. INGAT!")
        else:
            print(name ,"is not on this jeep")

    elif choice == "4":
        if len(passenger)== 0:
                print(" THE JEEP IS EMPTY ")
        else:                
            front = passenger.pop()
            print( front, "GOT OFF THE DOOR ")
    
    elif choice == "5":
        if len(passenger)== 0:
            print(" THE JEEP IS EMPTY ")
        else:                
            front = passenger.pop(0)
            print( front, "GOT OFF THE FRONT ")

    elif choice == "6":
        for i in range(len(passenger)):
            print("SEAT",i +1, passenger[i])

    elif choice == "7":
        route.reverse()
        print("ROUTE: ", route)

    elif choice == "8":
        print("TOTAL FARE TODAY: ",total)
        break

    else: 
        print(" INVALID!!!")