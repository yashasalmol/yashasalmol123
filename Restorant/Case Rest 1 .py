from menu import RestaurantMenu
from admin import admincode
from user import User

while True:
   print("1. Admin")
   print("2. User")
   print("3. Exit")
   opt = int(input("Enter option: "))
   if(opt == 1):
      admincode()
   elif(opt == 2):
      User()
   elif(opt == 3):
      print("Thank you come again!")
      break
   else:
      print("invalid input! try again")