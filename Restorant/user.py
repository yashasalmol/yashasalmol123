from menu import RestaurantMenu

def User():
    menu = RestaurantMenu()
    ch = 0
    while True:
        print("\n--- User Menu ---")
        print("1. Display Food")
        print("2. Place Order")
        print("3. View Order")
        print("4. Total Bill")
        print("5. Exit")
        ch = int(input("Enter Choice: "))
        if(ch==1):
            menu.displayFood()
        elif(ch==2):
            menu.placeorder()
        elif(ch==3):
            menu.viewOrder()
        elif(ch==4):
            menu.totalBill()
        elif(ch==5):
            print("Exiting User Menu...")
            break
        else:
            print("Invalid choice! Please try again.")