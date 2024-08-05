from getpass import getpass
from User import User
from Game import Game

class GameManager:
    
    def __init__(self, session):
        self.session = session

    
    def GetPlayerChoice(self, PlayerName:str):
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
    
    def PlayGame(self, player1, player2):

        wins01 = int(0)
        wins02=int(0)
    
        while abs(wins01-wins02)!=3:
        

            choice1 = self.GetPlayerChoice(player1.name)
            choice2 = self.GetPlayerChoice(player2.name)

            print(f"\n{player1.name} : {choice1}"
                    + f"\n{player2.name} : {choice2}\n")       
            if choice1 == choice2:
                    print( "draw!")
            elif (choice1 == "rock" and choice2 == "scissors") or \
                (choice1 == "paper" and choice2 == "rock") or \
                (choice1 == "scissors" and choice2 == "paper"):
                wins01+=1
                
            else:
                wins02+=1
                
            print( f"\n{player1.name} : {wins01}  |  {player2.name} : {wins02}\n")

        winner_id = player1.id if wins01 > wins02 else player2.id
        new_game = Game(player1_id=player1.id, player2_id=player2.id, winner_id=winner_id)
        self.session.add(new_game)
        self.session.commit()
        print(f"Game played between {player1.name} and {player2.name}. Winner: {player1.name if wins01 > wins02 else player2.name}")
         
        # Update wins and games played 
        player1.games_played += 1
        player2.games_played += 1
        if winner_id == player1.id:
            player1.wins += 1
        else:
            player2.wins += 1
        self.session.commit()
    
    def get_games(self):
        games = self.session.query(Game).all()

        game_details = []
        for game in games:
            player1 = self.session.query(User).filter_by(id=game.player1_id).first()
            player2 = self.session.query(User).filter_by(id=game.player2_id).first()
            winner = self.session.query(User).filter_by(id=game.winner_id).first()
            game_details.append({
                'game_id': game.id,
                'player1_name': player1.name if player1 else 'Unknown',
                'player2_name': player2.name if player2 else 'Unknown',
                'winner_name': winner.name 
            })
        return game_details