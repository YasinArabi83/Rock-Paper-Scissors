from getpass import getpass
from User import User

class ManagerGame:
    
    @staticmethod
    def GetPlayerChoice(PlayerName:str):
        PlayerChoice = getpass(f"{PlayerName}'s choice (Rock , Paper , Scissors) : ").lower()
       
        while PlayerChoice not in ["rock", "paper", "scissors"]:
            PlayerChoice = getpass(f"Invalid selection. Please select again (Rock , Paper , Scissors)").lower()
        
        return PlayerChoice
  
    @staticmethod
    def AddScore(player1:User,player2:User ,wins01:int,wins02:int):
       
        if wins01>wins02:
            player1.score+=1
            return ( "\n****************** "
                     + f"{player1.name} wins this match!"
                     +" ******************\n")
        else:
            player2.score+=1
            return ( "\n******************"
                     + f"{player2.name} wins this match!"
                     +"******************\n")
    
    @staticmethod
    def PlayGame(UsersList:list[User]):
        
        User.PrintUserList(UsersList)
        Player1 = User.SelectUser(UsersList)
        Player2 = User.SelectUser(UsersList)
        
        while Player1 == Player2:
            print("Players must be different. Select second player again.")
            Player2 = User.SelectUser(UsersList)
    
        wins01 = int(0)
        wins02=int(0)
    
        while abs(wins01-wins02)!=3:
        

                choice1 = ManagerGame.GetPlayerChoice(Player1.name)
                choice2 = ManagerGame.GetPlayerChoice(Player2.name)
                print(f"\n{Player1.name} : {choice1}"
                      + f"\n{Player2.name} : {choice2}\n")       
                if choice1 == choice2:
                     print( "draw!")
                elif (choice1 == "rock" and choice2 == "scissors") or \
                    (choice1 == "paper" and choice2 == "rock") or \
                    (choice1 == "scissors" and choice2 == "paper"):
        
                        wins01+=1
                        print( f"\n{Player1.name} wins this game!\n")
                else:
                    wins02+=1
                    print(f"\n{Player2.name} wins this game!\n")

            
        print(ManagerGame.AddScore(Player1,Player2,wins01,wins02))