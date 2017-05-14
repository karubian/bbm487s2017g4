from utils.DbClient import DbClient
from utils.MailClient import MailClient
from models.Loan import Loan
from controllers.UserController import UserController
from controllers.BookController import BookController
import _thread


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
        user.loanedBooks.remove(book.id)
        book.isAvailable = True
        self.client.delete_loan_record(book.id)
        self.bookController.update_book_attributes(book)
        self.userController.update_member_attributes(user)
        self.available_notification(book)

    def available_notification(self, returned_book):
        mail_client = MailClient()
        for waiting_user_id in returned_book.waitingList:
            waiting_user = self.userController.get_user_by_id(waiting_user_id)
            _thread.start_new_thread(mail_client.send_email, (waiting_user.username, waiting_user.email_address,
                                                              returned_book.title))
            # mail_client.send_email(waiting_user.username,waiting_user.email_address,returned_book.title)

    def get_loan_record(self, book_id):
        return self.client.find_loan_record(book_id)

    def instantiate_loan(self, loan_info):
        existing_loan = Loan(loan_info["user_id"], loan_info["book_id"])
        existing_loan.startDate = loan_info["startDate"]
        existing_loan.returnDate = loan_info["returnDate"]
        return existing_loan

    def update_fines(self):
        self.reset_fines()
        loans = self.client.db.loans.find({})
        for loan in loans:
            existing_loan = self.instantiate_loan(loan)
            existing_loan.check_status()
            existing_user = self.userController.get_user_by_id(existing_loan.user_id)
            existing_user.fineAmount = existing_user.fineAmount + existing_loan.currentFine
            self.userController.update_member_attributes(existing_user)

    def reset_fines(self):
        current_users = self.client.search_user_db("", "", "")
        for person in current_users:
            user_op = self.userController.get_user_by_id(person["_id"])
            user_op.fineAmount = 0
            self.userController.update_member_attributes(user_op)


