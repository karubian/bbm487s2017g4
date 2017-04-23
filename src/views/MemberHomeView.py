from PyQt5 import QtWidgets, QtGui
from views.gen.Ui_MemberHome import Ui_memberMainWindow
from controllers.UserController import UserController
from controllers.BookController import BookController
import views.ConfirmView as confirmView
import views.ErrorView as errorView


class MemberHomeView(Ui_memberMainWindow):
    def __init__(self, user):
        self.memberHome = QtWidgets.QMainWindow()
        self.ui = Ui_memberMainWindow()
        self.ui.setupUi(self.memberHome)
        self.ui.logoutButton.clicked.connect(self.logout)
        self.confirm = confirmView.ConfirmView()
        self.error = errorView.ErrorView()
        self.userController = UserController()
        self.bookController = BookController()
        self.ui.searchButton.clicked.connect(self.search_books)
        self.ui.waitingListButton.clicked.connect(self.add_to_waiting_list)
        self.ui.checkoutButton.clicked.connect(self.checkout_book)
        self.ui.cancelSelected.clicked.connect(self.cancel_waiting)
        self.currentUser = user
        self.customize_scene();
        self.current_book_queries = ["", "", ""]
        self.list_books()
        self.list_user_waiting_list()

    def customize_scene(self):
        self.ui.greetingLabel.setText("Hi, " + str(self.currentUser.name) + " " + str(self.currentUser.surname))
        self.ui.searchBookWidget.setColumnCount(3)
        self.ui.viewBookWidget.setColumnCount(3)
        self.ui.waitingListWidget.setColumnCount(3)
        self.ui.searchBookWidget.setHorizontalHeaderLabels(["Title", "Author", "Published Year"])
        self.ui.viewBookWidget.setHorizontalHeaderLabels(["Title", "Author", "Published Year"])
        self.ui.waitingListWidget.setHorizontalHeaderLabels(["Title", "Author", "Published Year"])

    def logout(self):
        import views.LoginView as LoginView
        self.memberHome.hide()
        self.ui = LoginView.LoginView()
        self.ui.show()

    def show(self):
        self.memberHome.show()

    def reset_book_filters(self):
        self.current_book_queries = ["", "", ""]
        self.list_books()

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
            if record["isAvailable"] is False:
                self.ui.searchBookWidget.item(i, 0).setBackground(QtGui.QColor(100, 50, 200))
                self.ui.searchBookWidget.item(i, 1).setBackground(QtGui.QColor(100, 50, 200))
                self.ui.searchBookWidget.item(i, 2).setBackground(QtGui.QColor(100, 50, 200))
            i = i + 1
        self.show()

    def search_books(self):
        search_title = self.ui.titleLineEdit.text()
        search_author = self.ui.authorLineEdit.text()
        search_year = self.ui.yearLineEdit.text()
        self.current_book_queries = [search_title, search_author, search_year]
        self.list_books()

    def checkout_book(self):
        selected_row = self.ui.searchBookWidget.currentRow()
        selected_book_title = self.ui.searchBookWidget.item(selected_row, 0).text()
        selected_book = self.bookController.get_book_by_title(selected_book_title)
        if selected_book.isAvailable is False:
            self.error.set_error_text("You can't checkout an unavailable book.")
            self.error.errorScreen.exec_()

    def add_to_waiting_list(self):
        selected_row = self.ui.searchBookWidget.currentRow()
        selected_book_title = self.ui.searchBookWidget.item(selected_row, 0).text()
        selected_book = self.bookController.get_book_by_title(selected_book_title)

        if selected_book.isAvailable is True:
            self.error.set_error_text("You can't add an available book to your waiting list.")
            self.error.errorScreen.exec_()
        elif selected_book.isAvailable is False:
            if selected_book.id not in self.currentUser.waitingBooks:
                self.currentUser.waitingBooks.append(selected_book.id)
            if self.currentUser.id not in selected_book.waitingList:
                selected_book.waitingList.append(self.currentUser.id)
            self.userController.update_member_attributes(self.currentUser)
            self.bookController.update_book_attributes(selected_book)
            self.list_user_waiting_list()

    def list_user_waiting_list(self):
        i = 0
        current_row_count = len(self.currentUser.waitingBooks)
        self.ui.waitingListWidget.setRowCount(current_row_count)

        for record in self.currentUser.waitingBooks:
            waited_book = self.bookController.get_book_by_id(record)
            self.ui.waitingListWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(waited_book.title))
            self.ui.waitingListWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(waited_book.author))
            self.ui.waitingListWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(waited_book.publishedYear))
            i = i+1
        self.show()

    def cancel_waiting(self):
        selected_row = self.ui.waitingListWidget.currentRow()
        selected_book_title = self.ui.waitingListWidget.item(selected_row, 0).text()
        selected_book = self.bookController.get_book_by_title(selected_book_title)
        self.confirm.confirm_flag = 0
        self.confirm.set_confirm_text("Are you sure you want to cancel waiting for this book?")
        self.confirm.confirmScreen.exec_()
        if self.confirm.confirm_flag is 2:
            self.currentUser.waitingBooks.remove(selected_book.id)
            selected_book.waitingList.remove(self.currentUser.id)
            self.userController.update_member_attributes(self.currentUser)
            self.bookController.update_book_attributes(selected_book)
        self.list_user_waiting_list()