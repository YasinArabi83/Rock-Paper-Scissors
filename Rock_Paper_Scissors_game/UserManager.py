from User import User

class UserManager:

    def __init__(self , session):
        self.session=session

    def CreateUser(self, username):
        new_user = User(name=username)
        self.session.add(new_user)
        self.session.commit()
        print(f"User created: {username}")
        
    @staticmethod
    def SelectUser(UserList: list):
        while True:
            user_id_input = input("\nEnter user ID: ")
            Id = int(user_id_input) if user_id_input.isdecimal() else -1

            if 0 <= Id < len(UserList):
                return UserList[Id]
            else:
                print("\nInvalid selection. Please select again\n")

    @staticmethod
    def PrintUserList(UserList: list):
        for user in UserList:
            print(user)