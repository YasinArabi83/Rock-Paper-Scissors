class User:
    def __init__(self, Id: int, name: str, score=0):
        self.Id = Id
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.Id} - {self.name} : {self.score}"

    def __eq__(self, __value: object) -> bool:
       if self.Id == __value.Id:
           return True
       else:
           return False

    @staticmethod
    def createUser(UserList: list, name: str):
        Id = len(UserList)
        newUser = User(Id, name)
        UserList.append(newUser)

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