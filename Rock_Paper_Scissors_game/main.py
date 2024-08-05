import getpass
from Rock_Paper_Scissors_game.ManagerGame import ManagerGame
from User import User

Users: list[User] = []

while True:
    print(" =========================== \n"
          "Menu \n \n"
          "1. Create new user \n"
          "2. Start new match \n"
          "3. Get users list\n"
          "4. Exit\n\n"
          "===========================")
    choice = input("What`s your choice: ")
    
    if choice == '1':
        UserName = input("Enter a Username: ")
        User.createUser(Users, UserName)
    elif choice == '2':
        if len(Users) < 2:
            print("\nThere are not enough users to play the game. Create a new user.\n")
        else:
            ManagerGame.PlayGame(Users)
    elif choice == '3':
        User.PrintUserList(Users)
    elif choice == '4':
        break
    else:
        print("Invalid selection. Please select again.\n")