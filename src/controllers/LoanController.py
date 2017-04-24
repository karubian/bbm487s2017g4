from utils.DbClient import DbClient
from models.Loan import Loan
from controllers.UserController import UserController
from controllers.BookController import BookController


class LoanController:
    def __init__(self):
        self.client = DbClient.Instance()
        self.userController = UserController()
        self.bookController = BookController()

    def checkout_book(self, user, book):
        if user.fineAmount is 0 and len(user.loanedBooks) < 4:
            user.loanedBooks.append(book.id)
            if book.id in user.waitingBooks:
                user.waitingBooks.remove(book.id)
            book.isAvailable = False
            user.totalLoanedBooks = user.totalLoanedBooks + 1
            user.lastLoanedBook = book.title
            self.userController.update_member_attributes(user)
            self.bookController.update_book_attributes(book)
            new_loan = Loan(user.id, book.id)
            self.client.add_loan_record(new_loan)

    def return_book(self, user, book):
        loan_info = self.get_loan_record(book.id)
        existing_loan = Loan(loan_info["user_id"], loan_info["book_id"])
        existing_loan.startDate = loan_info["startDate"]
        existing_loan.returnDate = loan_info["returnDate"]
        existing_loan.check_status()
        user.fineAmount = user.fineAmount + existing_loan.currentFine
        user.loanedBooks.remove(book.id)
        book.isAvailable = True
        self.client.delete_loan_record(book.id)
        self.bookController.update_book_attributes(book)
        self.userController.update_member_attributes(user)

    def get_loan_record(self, book_id):
        return self.client.find_loan_record(book_id)
