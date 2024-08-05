from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from User import User, Base
from Game import Game,Base
from UserManager import UserManager
from GameManager import GameManager

# Create a connection to the database
engine = create_engine('sqlite:///game.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



user_manager = UserManager(session)
game_manager = GameManager(session)

while True:
    print(" =========================== \n"
          "Menu \n \n"
          "1. Create new user \n"
          "2. Start new match \n"
          "3. Get users list\n"
          "4. Get games list\n"
          "5. Exit\n\n"
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