from menu import RestaurantMenu

def admincode():
    menu = RestaurantMenu()
    uid = input("Enter user ID: ")
    pass1 = input("Enter password: ")

    if uid == "yash" and pass1 == "1234":
        while True:
            print("\n--- Admin Menu ---")
            print("1. Add food")
            print("2. Display Food")
            print("3. Delete Food")
            print("4. Update Food Price")
            print("5. Total Revenue")
            print("6. Exit")

            ch = int(input("Enter Choice: "))
            if ch == 1:
                menu.addFood()
            elif ch == 2:
                menu.displayFood()
            elif ch == 3:
                menu.deleteFood()
            elif ch == 4:
                menu.updateFoodPrice()
            elif ch == 5:
                menu.Revenue()
            elif ch == 6:
                print("Exiting Admin Menu...")
                break
            else:
                print("Invalid choice! Please try again.")
    else:
        print("Invalid User ID or Password!")
