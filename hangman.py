# this belongs to Rishit Agrawal 

car_parking = [
    ["[ ]","[ ]","[ ]","[ ]","[ ]"], # floor 0
    ["[ ]","[ ]","[ ]","[ ]","[ ]"], # floor 1 
    ["[ ]","[ ]","[ ]","[ ]","[ ]"]  # floor 2
]
car_details = {
    "KA01CA1100": [0,2,"vip"],
    "KA01CA1101": [0,3,"standard"]
}
def display():
    car_parking.reverse()
    for i in range(len(car_parking)):
        print(f"floor {2-i}",end= " : ")
        for j in car_parking[i]:
            print(j , end = " ")
        print()
    car_parking.reverse()
def user_choice():
    display()
    print()
    user_number_plate = input("enter your vehichle number plate number: ")
    if user_number_plate  not in car_details:
        print("the VIP is for ₹50")
        user_type = input("enter the status you want: ").lower()
        try:
            floor_index = int( input("enter the floor you want to park your car onto: "))
            if floor_index == 2:
                if user_type == "vip":
                    try:
                        row_index = int(input("enter the row on which you want to park your car (0,1,2,3,4)"))
                        if car_parking[floor_index][row_index] == "[ ]":
                            print(f"your car has been pakred on \nfloor = {floor_index}\nrow = {row_index}")
                            car_parking[floor_index][row_index] = "[X]"
                            temp_list = [floor_index,row_index,user_type]
                            car_details[user_number_plate] = temp_list
                        else:
                            print("this spot is already taken.... ")
                            print("try selecting another spot")
                    except (ValueError,IndexError):
                        print("ERROR: enter a valid input")
                        return
                    
                else:
                    print("you are not a vip member")        
            else:
                try:
                    row_index = int(input("enter the row on which you want to park your car (0,1,2,3,4)"))
                    if car_parking[floor_index][row_index] == "[ ]":
                        print(f"your car has been pakred on \nfloor = {floor_index}\nrow = {row_index}")
                        car_parking[floor_index][row_index] = "[X]"
                        temp_list = [floor_index,row_index,user_type]
                        car_details[user_number_plate] = temp_list
                    else:
                        print("this spot is already taken.... ")
                        print("try selecting another spot")
                except (ValueError,IndexError):
                    print("ERROR: enter a valid input choice")
                    return
        except ValueError:
            print("ERROR: enter a valid floor number")
            return
    else:
        print("your car is already parked in the building ....")
def find_car():
    user_number_plate = input("enter your number plate: ")
    if user_number_plate in car_details:
        print(f"your car is parked on ")
        print(f"floor = {car_details[user_number_plate][0]}")
        print(f" row = {car_details[user_number_plate][1]}")
    else:
        print("your car is not in the building ...") 
def bill():
    user_bill = 0
    user_number_plate = input("enter your number plate: ")
    if user_number_plate in car_details:
        try:
            time = int(input("enter the time you have pakred the car for (in hrs): "))
            if car_details[user_number_plate][-1] == "vip":
                user_bill = (time*100) + 50
                print("*" * 20)
                print("vip                  =   ₹50") 
                print(f"time ({time} * 100) =   ₹{time*100}")
                print(f"total               =   ₹{user_bill}")
                print("*" * 20)
            else:
                user_bill = time * 100
                print("*" * 20)
                print(f"time {time} * 100 = ₹{time*100}")
                print(f"total = ₹{user_bill}")
                print("*" * 20)
            floor_index = car_details[user_number_plate][0]
            row_index= car_details[user_number_plate][1]
            car_parking[floor_index][row_index] = "[ ]"
            del car_details[user_number_plate]
        except ValueError:
            print("ERROR: enter a valid number for time")
            return
    else:
        print("*" * 20)
        print("total = ₹0.00")
        print("*" * 20)
while True:
    print("press \n 1. to park car \n 2. find my car \n 3. checkout \n 4. exit")
    try:
        user_input = int(input("enter your choice: "))
    except ValueError:
        print("ERROR: enter a valid number between 1 to 4")
        continue
    if user_input == 1:
        user_choice()
    elif user_input == 2:
        find_car()
    elif user_input == 3:
        bill()
        print("thank you for choosing us")
    elif user_input == 4:
        print("thank you for choosing us")
        break
    else:
        print("enter a valid choice the menue ...")
