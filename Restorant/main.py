from menu import RestaurantMenu
print("----Restaurant Management System----")
print("1. Admin")
print("2. User")
choice = int(input("Enter choice: "))
if(choice == 1):
    menu = RestaurantMenu()
    uid = input("Enter user ID: ")
    pass1 = input("Enter password: ")
    if(uid == "yash" and pass1 =="1234"):
        order = OrderSystem()
        ch = 0
        while(ch!=7):
            print("1. Add food")
            print("2. Display Food")
            print("3. Delete Food ")
            print("4. Update Food Price")
            print("5. Total Bill")
            print("6. View order")
            print("7. Exit")
            ch = int(input("Enter Choice: "))
            if(ch==1):
                menu.addFood()
            elif(ch==2):
                menu.displayFood()
            elif(ch==3):
                menu.deleteFood()
            elif(ch==4):
                menu.updateFoodPrice()
            elif(ch==5):
                menu.totalBill()
            elif ch == 6:
                menu.viewOrder()
            elif ch == 7:
                print("Exiting Admin Menu...")
                break