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