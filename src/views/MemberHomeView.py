from PyQt5 import QtWidgets, QtGui
from views.gen.Ui_MemberHome import Ui_memberMainWindow
from controllers.UserController import UserController
from controllers.BookController import BookController
from controllers.LoanController import LoanController
import views.BookInfoView as bookInfoView
import views.ConfirmView as confirmView
import views.ErrorView as errorView
import views.PaymentView as paymentView
import views.NotificationView as notificationView
import datetime


class MemberHomeView(Ui_memberMainWindow):
    def __init__(self, user):
        self.memberHome = QtWidgets.QMainWindow()
        self.ui = Ui_memberMainWindow()
        self.ui.setupUi(self.memberHome)
        self.ui.logoutButton.clicked.connect(self.logout)
        self.confirm = confirmView.ConfirmView()
        self.error = errorView.ErrorView()
        self.notification = notificationView.NotificationView()
        self.userController = UserController()
        self.bookController = BookController()
        self.loanController = LoanController()
        self.ui.searchButton.clicked.connect(self.search_books)
        self.ui.waitingListButton.clicked.connect(self.add_to_waiting_list)
        self.ui.checkoutButton.clicked.connect(self.checkout_book)
        self.ui.cancelSelected.clicked.connect(self.cancel_waiting)
        self.ui.returnBookButton.clicked.connect(self.return_operation)
        self.ui.payFineButton.clicked.connect(self.payment_operation)
        self.ui.resetButton.clicked.connect(self.reset_book_filters)
        self.ui.waitingListWidget.cellDoubleClicked.connect(self.show_book_info_waiting)
        self.ui.viewBookWidget.cellDoubleClicked.connect(self.show_book_info_view)
        self.ui.searchBookWidget.cellDoubleClicked.connect(self.show_book_info_search)
        self.currentUser = user
        self.payment = paymentView.PaymentView(0)
        self.prepare_scene()
        self.current_book_queries = ["", "", ""]
        self.update_lists()
        self.update_scene()
        self.set_button_effects()
        self.book_info = None
        self.check_notifications()

    def prepare_scene(self):
        self.ui.greetingLabel.setText("Hi, " + str(self.currentUser.name) + " " + str(self.currentUser.surname))
        self.ui.dateLabel.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.ui.searchBookWidget.setColumnCount(4)
        self.ui.viewBookWidget.setColumnCount(4)
        self.ui.waitingListWidget.setColumnCount(4)
        self.ui.searchBookWidget.setHorizontalHeaderLabels(["Title", "Author", "Year","User ID"])
        self.ui.viewBookWidget.setHorizontalHeaderLabels(["Title", "Author", "Published Year","User ID"])
        self.ui.waitingListWidget.setHorizontalHeaderLabels(["Title", "Author", "Published Year","User ID"])

    def update_scene(self):
        self.currentUser = self.userController.get_user_by_id(self.currentUser.id)
        self.ui.lastBookLabel.setText("Last Loaned Book : " + self.currentUser.lastLoanedBook)
        self.ui.fineLabel.setText("Current Fine Amount : $" + str(self.currentUser.currentFine))
        self.ui.totalBooksLabel.setText("Total Loaned Books : " + str(self.currentUser.totalLoanedBooks))

    def logout(self):
        import views.LoginView as LoginView
        self.memberHome.hide()
        self.ui = LoginView.LoginView()
        self.ui.show()

    def show(self):
        self.memberHome.show()

    def reset_book_filters(self):
        self.current_book_queries = ["", "", ""]
        self.update_lists()

    def payment_operation(self):
        self.payment = paymentView.PaymentView(self.currentUser.formerFine)
        self.payment.paymentPrompt.exec_()
        if self.payment.paymentFlag:
            self.loanController.reset_user_loans(self.currentUser.id)
            self.currentUser.currentFine = 0
            self.currentUser.formerFine = 0
            self.userController.update_member_attributes(self.currentUser)
            self.loanController.update_fines()
        self.update_scene()

    def show_book_info_view(self):
        selected_row = self.ui.viewBookWidget.currentRow()
        if selected_row > -1:
            selected_book_id = self.ui.viewBookWidget.item(selected_row, 3).text()
            selected_book = self.bookController.get_book_by_id(str(selected_book_id))
            self.book_info = bookInfoView.BookInfoView(selected_book)
            self.book_info.update_scene()
            self.book_info.show()

    def show_book_info_search(self):
        selected_row = self.ui.searchBookWidget.currentRow()
        if selected_row > -1:
            selected_book_id = self.ui.searchBookWidget.item(selected_row, 3).text()
            selected_book = self.bookController.get_book_by_id(selected_book_id)
            self.book_info = bookInfoView.BookInfoView(selected_book)
            self.book_info.update_scene()
            self.book_info.show()

    def show_book_info_waiting(self):
        selected_row = self.ui.waitingListWidget.currentRow()
        if selected_row > -1:
            selected_book_id = self.ui.waitingListWidget.item(selected_row, 3).text()
            selected_book = self.bookController.get_book_by_title(str(selected_book_id))
            self.book_info = bookInfoView.BookInfoView(selected_book)
            self.book_info.update_scene()
            self.book_info.show()


    def list_books(self):
        query_result = self.bookController.search_books(self.current_book_queries[0], self.current_book_queries[1],
                                                        self.current_book_queries[2])
        i = 0
        current_row_count = query_result.count()
        self.ui.searchBookWidget.setRowCount(current_row_count)

        for record in query_result:
            self.ui.searchBookWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(record["title"]))
            self.ui.searchBookWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(record["author"]))
            self.ui.searchBookWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(record["year"]))
            self.ui.searchBookWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(record["_id"])))
            if record["isAvailable"] is False:
                self.ui.searchBookWidget.item(i, 0).setBackground(QtGui.QColor(255, 68, 68))
                self.ui.searchBookWidget.item(i, 1).setBackground(QtGui.QColor(255, 68, 68))
                self.ui.searchBookWidget.item(i, 2).setBackground(QtGui.QColor(255, 68, 68))
            i = i + 1
        self.show()

    def search_books(self):
        search_title = self.ui.titleLineEdit.text()
        search_author = self.ui.authorLineEdit.text()
        search_year = self.ui.yearLineEdit.text()
        self.current_book_queries = [search_title, search_author, search_year]
        self.update_lists()

    def checkout_book(self):
        selected_row = self.ui.searchBookWidget.currentRow()
        if selected_row > -1:
            selected_book_id = self.ui.searchBookWidget.item(selected_row, 3).text()
            selected_book = self.bookController.get_book_by_id(str(selected_book_id))
            if selected_book.isAvailable is False:
                self.error.set_error_text("You can't checkout an unavailable book.")
                self.error.errorScreen.exec_()
            else:
                self.loanController.checkout_book(self.currentUser, selected_book)
                self.update_lists()
                self.update_scene()

    def add_to_waiting_list(self):
        selected_row = self.ui.searchBookWidget.currentRow()
        if selected_row > -1:
            selected_book_id = self.ui.searchBookWidget.item(selected_row, 3).text()
            selected_book = self.bookController.get_book_by_id(str(selected_book_id))

            if selected_book.isAvailable is True:
                self.error.set_error_text("You can't add an available book to your waiting list.")
                self.error.errorScreen.exec_()
            elif selected_book.id in self.currentUser.loanedBooks:
                self.error.set_error_text("You already loaned this book.")
                self.error.errorScreen.exec_()
            elif selected_book.isAvailable is False:
                if str(selected_book.id) not in self.currentUser.waitingBooks:
                    self.currentUser.waitingBooks.append(str(selected_book.id))
                if str(self.currentUser.id) not in selected_book.waitingList:
                    selected_book.waitingList.append(str(self.currentUser.id))
                self.userController.update_member_attributes(self.currentUser)
                self.bookController.update_book_attributes(selected_book)
                self.update_lists()

    def update_lists(self):
        self.list_user_waiting_list()
        self.list_books()
        self.list_loaned_books()

    def check_notifications(self):
        for book in self.currentUser.waitingBooks:
            if self.bookController.get_book_by_id(book).isAvailable:
                self.notification.set_notif_text("\"" + self.bookController.get_book_by_id(book).title + "\"" +
                                                 " is available to rent.")
                self.notification.show()

    def list_user_waiting_list(self):
        i = 0
        current_row_count = len(self.currentUser.waitingBooks)
        self.ui.waitingListWidget.setRowCount(current_row_count)

        for record in self.currentUser.waitingBooks:
            waited_book = self.bookController.get_book_by_id(record)
            self.ui.waitingListWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(waited_book.title))
            self.ui.waitingListWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(waited_book.author))
            self.ui.waitingListWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(waited_book.publishedYear))
            self.ui.waitingListWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(waited_book.id)))
            if waited_book.isAvailable is False:
                self.ui.waitingListWidget.item(i, 0).setBackground(QtGui.QColor(255, 68, 68))
                self.ui.waitingListWidget.item(i, 1).setBackground(QtGui.QColor(255, 68, 68))
                self.ui.waitingListWidget.item(i, 2).setBackground(QtGui.QColor(255, 68, 68))
            i = i + 1
        self.show()

    def list_loaned_books(self):
        i = 0
        current_row_count = len(self.currentUser.loanedBooks)
        self.ui.viewBookWidget.setRowCount(current_row_count)

        for record in self.currentUser.loanedBooks:
            loaned_book = self.bookController.get_book_by_id(record)
            self.ui.viewBookWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(loaned_book.title))
            self.ui.viewBookWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(loaned_book.author))
            self.ui.viewBookWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(loaned_book.publishedYear))
            self.ui.viewBookWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(loaned_book.id)))
            i = i + 1
        self.show()

    def cancel_waiting(self):
        selected_row = self.ui.waitingListWidget.currentRow()
        if selected_row > -1:
            selected_book_id = self.ui.waitingListWidget.item(selected_row, 3).text()
            selected_book = self.bookController.get_book_by_id(str(selected_book_id))
            self.confirm.confirm_flag = 0
            self.confirm.set_confirm_text("Are you sure you want to cancel waiting for this book?")
            self.confirm.confirmScreen.exec_()
            if self.confirm.confirm_flag is 1:
                self.currentUser.waitingBooks.remove(str(selected_book.id))
                selected_book.waitingList.remove(str(self.currentUser.id))
                self.userController.update_member_attributes(self.currentUser)
                self.bookController.update_book_attributes(selected_book)
        self.update_lists()

    def return_operation(self):
        selected_row = self.ui.viewBookWidget.currentRow()
        if selected_row > -1:
            selected_book_id = self.ui.viewBookWidget.item(selected_row, 3).text()
            selected_book = self.bookController.get_book_by_id(str(selected_book_id))
            self.confirm.confirm_flag = 0
            self.confirm.set_confirm_text("Are you sure you want to return this book?")
            self.confirm.confirmScreen.exec_()
            if self.confirm.confirm_flag is 1:
                self.loanController.return_book(self.currentUser, selected_book)
                self.update_lists()
                self.update_scene()

    def set_button_effects(self):
        self.ui.returnBookButton.released.connect(self.released_color_change)
        self.ui.returnBookButton.pressed.connect(self.pressed_color_change)
        self.ui.searchButton.released.connect(self.released_color_change)
        self.ui.searchButton.pressed.connect(self.pressed_color_change)
        self.ui.cancelSelected.released.connect(self.released_color_change)
        self.ui.cancelSelected.pressed.connect(self.pressed_color_change)
        self.ui.checkoutButton.released.connect(self.released_color_change)
        self.ui.checkoutButton.pressed.connect(self.pressed_color_change)
        self.ui.logoutButton.released.connect(self.released_color_change)
        self.ui.logoutButton.pressed.connect(self.pressed_color_change)
        self.ui.waitingListButton.released.connect(self.released_color_change)
        self.ui.waitingListButton.pressed.connect(self.pressed_color_change)
        self.ui.payFineButton.released.connect(self.released_color_change)
        self.ui.payFineButton.pressed.connect(self.pressed_color_change)

    def released_color_change(self):
        if self.memberHome.sender().text() == 'Add To Waiting List':
            self.memberHome.sender().setStyleSheet("QPushButton {\n"
                                                   "color: white;\n"
                                                   "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                                   "font-size: 20px;\n"
                                                   "}")
        else:
            self.memberHome.sender().setStyleSheet("QPushButton {\n"
                                                   "color: white;\n"
                                                   "background-color:  QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                                   "font-size: 30px;\n"
                                                   "}")

    def pressed_color_change(self):
        if self.memberHome.sender().text() == 'Add To Waiting List':
            self.memberHome.sender().setStyleSheet("QPushButton {\n"
                                                   "color: white;\n"
                                                   "background-color: red;\n"
                                                   "font-size: 20px;\n"
                                                   "}")
        else:
            self.memberHome.sender().setStyleSheet("QPushButton {\n"
                                                   "color: white;\n"
                                                   "background-color:red;\n"
                                                   "font-size: 30px;\n"
                                                   "}")
