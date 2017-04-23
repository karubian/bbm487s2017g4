from .User import User


class Librarian(User):
    def __init__(self, username, password, name, surname, email):
        super().__init__(username, password, name, surname, email)
        self.type = "librarian"

