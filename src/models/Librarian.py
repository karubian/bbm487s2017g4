from .User import User


class Librarian(User):
    def __init__(self,username,password):
        super().__init__(username,password)
        self.type = "librarian"
