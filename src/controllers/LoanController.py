from utils.DbClient import DbClient
from utils.MailClient import MailClient
from models.Loan import Loan
from controllers.UserController import UserController
from controllers.BookController import BookController
import _thread
import datetime


class LoanController:
    def __init__(self):
        self.client = DbClient.Instance()
        self.userController = UserController()
        self.bookController = BookController()

    def checkout_book(self, user, book):
        if user.currentFine is not 0:
            return 0
        elif len(user.loanedBooks) >= 4:
            return 1
        else:
            user.loanedBooks.append(book.id)
            if book.id in user.waitingBooks:
                user.waitingBooks.remove(str(book.id))
            book.isAvailable = False
            user.totalLoanedBooks = user.totalLoanedBooks + 1
            user.lastLoanedBook = book.title
            self.userController.update_member_attributes(user)
            self.bookController.update_book_attributes(book)
            new_loan = Loan(str(user.id), str(book.id))
            self.client.add_loan_record(new_loan)
            return 2

    def return_book(self, user, book):
        loan_info = self.get_loan_record(str(book.id))
        existing_loan = Loan(str(loan_info["user_id"]), str(loan_info["book_id"]))
        existing_loan.startDate = loan_info["startDate"]
        existing_loan.returnDate = loan_info["returnDate"]
        existing_loan.check_status()
        self.update_loan_attributes(existing_loan)
        user.loanedBooks.remove(str(book.id))
        book.isAvailable = True
        user.formerFine = user.formerFine + existing_loan.currentFine
        self.client.delete_loan_record(str(book.id))
        self.bookController.update_book_attributes(book)
        self.userController.update_member_attributes(user)
        self.update_fines()
        self.available_notification(book)

    def available_notification(self, returned_book):
        mail_client = MailClient()
        for waiting_user_id in returned_book.waitingList:
            waiting_user = self.userController.get_user_by_id(str(waiting_user_id))
            _thread.start_new_thread(mail_client.send_email, (waiting_user.username, waiting_user.email_address,
                                                              returned_book.title))
            # mail_client.send_email(waiting_user.username,waiting_user.email_address,returned_book.title)

    def get_loan_record(self, book_id):
        return self.client.find_loan_record(str(book_id))

    def instantiate_loan(self, loan_info):
        existing_loan = Loan(str(loan_info["user_id"]), str(loan_info["book_id"]))
        existing_loan.startDate = loan_info["startDate"]
        existing_loan.returnDate = loan_info["returnDate"]
        return existing_loan

    def update_fines(self):
        self.reset_fines()
        loans = self.client.db.loans.find({})
        for loan in loans:
            existing_loan = self.instantiate_loan(loan)
            existing_loan.check_status()
            self.update_loan_attributes(existing_loan)
            existing_user = self.userController.get_user_by_id(str(existing_loan.user_id))
            existing_user.currentFine = existing_user.currentFine + existing_loan.currentFine
            self.userController.update_member_attributes(existing_user)

    def reset_fines(self):
        current_users = self.client.search_user_db("", "", "")
        for person in current_users:
            user_op = self.userController.get_user_by_id(str(person["_id"]))
            user_op.currentFine = user_op.formerFine
            self.userController.update_member_attributes(user_op)

    def delete_user_from_loans(self, user_id):
        loans = self.client.db.loans.find({})
        for loan in loans:
            if loan["user_id"] == user_id:
                op_book = self.bookController.get_book_by_id(str(loan["book_id"]))
                op_book.isAvailable = True
                self.bookController.update_book_attributes(op_book)
                self.client.delete_loan_record(str(loan["book_id"]))

    def delete_book_from_loans(self, book_id):
        loans = self.client.db.loans.find({})
        for loan in loans:
            if loan["book_id"] == book_id:
                self.client.delete_loan_record(str(loan["book_id"]))

    def update_loan_attributes(self, loan):
        self.client.update_loan_attributes_db(loan)

    def reset_user_loans(self, user_id):
        loans = self.client.db.loans.find({})
        for loan_info in loans:
            if loan_info["user_id"] == user_id and loan_info["status"] == 1:
                updated_loan = self.instantiate_loan(loan_info)
                updated_loan.startDate = datetime.datetime.now() - datetime.timedelta(days=40)
                updated_loan.check_status()
                self.update_loan_attributes(updated_loan)
