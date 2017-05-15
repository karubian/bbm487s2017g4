from .User import User


class Member(User):
    def __init__(self, username, password, name, surname, email):
        super().__init__(username, password, name, surname, email)
        self.type = "member"
        self.currentFine = 0
        self.formerFine = 0
        self.waitingBooks = []
        self.loanedBooks = []
        self.totalLoanedBooks = 0
        self.lastLoanedBook = "No books loaned"
