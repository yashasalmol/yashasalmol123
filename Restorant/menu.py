from tabulate import tabulate
from order import Order

class RestaurantMenu:
    def __init__(self):
        self.menu = "Menu"


    def addFood(self):
        f_id = int(input("Enter food id: "))
        f_name = input("Enter Food name: ")
        f_price = int(input("Enter food Price: "))
        O = Order(f_id, f_name, f_price)
        
        with open("Menu.txt", "a") as f1:
            f1.write(str(O) + "\n")
        print("Food added successfully!")


    def displayFood(self):
        with open("Menu.txt", "r") as f1:
            for s in f1:
                if s.strip():
                    f_id, f_name, f_price = s.split(",")
                    print(f"ID: {f_id} | Name: {f_name} | Price: ₹{f_price}") 
 
    # def displayFood(self):
    #     with open("Menu.txt", "r") as f1:
    #         menu_items = [
    #             line.split(",") 
    #             for line in f1
    #         ]

    #     if menu_items:
    #         print("\n===== Restaurant Menu =====")
    #         print(tabulate(menu_items, headers=["ID", "Food Name", "Price (₹)"], tablefmt="grid"))
    #     else:
    #         print("Menu is empty!")

    def deleteFood(self):
        container= []
        found = False
        f_id = int(input("Enter Food ID: "))
        with open("Menu.txt","r") as f1:
            for e in f1:
                list1 = e.split(",")
                if(list1[0]!=str(f_id)):
                    container.append(e)
                else:
                    f_id, f_name, f_price = e.split(",")
                    print(f"Food ID: {f_id}\nName: {f_name}\nPrice: {f_price}")
                    print("Food has been deleted")
                    found = True
        if(found==False):
            print("Record Not Found")
        else:
            with open("Menu.txt","w") as f1:
                for c in container:
                    f1.write(c)


    def updateFoodPrice(self):
        container = []
        found = False
        f_id = int(input("Enter f_ID to update: "))
        with open("Menu.txt","r") as f1:
            for o in f1:
                list1 = o.split(",")
                if(list1[0]==str(f_id)):
                    found = True
                    print("1. Food Name")
                    print("2. Food Price")
                    print("3. Both Name and Price")
                    ch = int(input("Enter Option to update: "))
                    if(ch==1):
                        f_name = input("Enter new name: ")
                        list1[1] = f_name
                    elif(ch==2):
                        f_price = int(input("Enter new price: "))
                        list1[2] = str(f_price)
                    else:
                        f_name = input("Enter new name: ")
                        list1[1] = f_name
                        f_price = int(input("Enter new price: "))
                        list1[2] = str(f_price)
                        
                    o = ','.join(list1)+"\n"
                container.append(o)

        if(found==False):
            print("Not Present in menu")
        else:
            with open("Menu.txt","w") as f1:
                for c in container:
                    f1.write(c)


    def totalBill(self):
        self.viewOrder()
        total = 0
        # Step 1: Read Orders.txt
        with open("Orders.txt", "r") as f1, open("Revenue.txt", "a") as f2:
            for e in f1:
                list1 = e.split(",")
                total += int(list1[2])
                # Save the same order to Revenue.txt
                f2.write(e)
        # Step 2: Display bill to the user
        if total == 0:
            print("No orders placed in this session.")
        else:
            print(f"Your Total Bill: ₹{total}")
        # Step 3: Clear current session orders
        open("Orders.txt", "w").close()


    def viewOrder(self):
        with open("Orders.txt", "r") as f1:
            for s in f1:
                if s:
                    f_id, f_name, f_price = s.split(",")
                    print(f"ID: {f_id} | Name: {f_name} | Price: ₹{f_price}")
        

    def placeorder(self):
        while True:
            self.displayFood()
            f_id = int(input("\nEnter Food ID to place order (0 to stop): "))

            if f_id == 0:
                break

            found = False
            with open("Menu.txt", "r") as f1:
                for o in f1:
                    list1 = o.split(",")
                    if list1[0] == str(f_id):
                        found = True

                        # Save current session order
                        with open("Orders.txt", "a") as f2:
                            f2.write(o)

                        # Save permanent order for admin revenue
                        with open("Revenue.txt", "a") as f3:
                            f3.write(o)

                        print(f"Order placed successfully for {list1[1]}!")
                        break

            if not found:
                print("Food ID not found!")



    def Revenue(self):
        total = 0
        with open("Revenue.txt", "r") as f1:
            for e in f1:
                list1 = e.split(",")
                total += int(list1[2])
        print(f"\nTotal Revenue : ₹{total}")