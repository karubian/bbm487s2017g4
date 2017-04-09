from .User import User


class Member(User):
    def __init__(self,username,password):
        super().__init__(username,password)
        self.type = "member"
