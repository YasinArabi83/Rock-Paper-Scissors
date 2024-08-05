from User import User

class UserManager:

    def __init__(self , session):
        self.session=session

    def CreateUser(self, username):
        new_user = User(name=username)
        self.session.add(new_user)
        self.session.commit()
        print(f"User created: {username}")

    
    def PlayerSelector(self,users: list):
        while True:
            print("Select Player :")
            for i, user in enumerate(users,1):
                print(f"{i }. {user.name}")
             
            user_input = input("Enter the number of Player 1: ")
            user_index=int(user_input) if user_input.isdecimal() else -1
            if len(users) >=user_index>=0:
                return users[user_index-1]
            else:
                print(f"Invalid Input , Please enter a number between 1 and  + {len(users)}")

    @staticmethod
    def PrintUserList(UserList: list):
        for user in UserList:
            print(user)