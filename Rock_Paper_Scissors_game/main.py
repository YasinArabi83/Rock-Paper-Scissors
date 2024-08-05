from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from UserManager import UserManager
from GameManager import GameManager
from base import Base

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
        user_manager.CreateUser(UserName)
    elif choice == '2':
        users = user_manager.GetUsers()
        if len(users) < 2:
            print("\nThere are not enough users to play the game. Create a new user.\n")
        else:
           player1= user_manager.PlayerSelector(users)
           while True:
              try:
                   player2= user_manager.PlayerSelector(users)
                   assert player1 != player2, 'similar player are not allowed!'
                   break
              except AssertionError as err:
                   print(err)
           game_manager.PlayGame(player1, player2)
    elif choice == '3':
        users = user_manager.GetUsers()
        for user in users:
            print(f"ID: {user.id}, Name: {user.name},  Wins: {user.wins}, Games Played: {user.games_played}")
    elif choice == '4':
        games = game_manager.get_games()
        for game in games:
            print(f"Game ID: {game['game_id']}, Player 1: {game['player1_name']}, Player 2: {game['player2_name']}, Winner: {game['winner_name']}")
    elif choice == '5':
        break
    else:
        print("Invalid selection. Please select again.\n")