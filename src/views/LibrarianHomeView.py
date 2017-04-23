from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_LibrarianHome import Ui_libraryMainWindow
from controllers.UserController import UserController
from controllers.BookController import BookController
import views.ConfirmView as confirmView
import views.UserRegisterFormView as userRegisterFormView
import views.BookRegisterFormView as bookRegisterFormView


class LibrarianHomeView(Ui_libraryMainWindow):
    def __init__(self, user):
        self.userRegisterScreen = userRegisterFormView.UserRegisterFormView()
        self.bookRegisterScreen = bookRegisterFormView.BookRegisterFormView()
        self.librarianHome = QtWidgets.QMainWindow()
        self.ui = Ui_libraryMainWindow()
        self.ui.setupUi(self.librarianHome)
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.userResetButton.clicked.connect(self.reset_user_filters)
        self.ui.bookResetButton.clicked.connect(self.reset_book_filters)
        self.ui.userDeleteButton.clicked.connect(self.delete_selected_user)
        self.ui.userCreateButton.clicked.connect(self.register_user_form)
        self.ui.userUpdateButton.clicked.connect(self.update_user_form)
        self.ui.userSearchButton.clicked.connect(self.search_users)
        self.ui.bookSearchButton.clicked.connect(self.search_books)
        self.ui.bookDeleteButton.clicked.connect(self.delete_selected_book)
        self.ui.bookCreateButton.clicked.connect(self.register_book_form)
        self.ui.bookUpdateButton.clicked.connect(self.update_book_form)
        self.ui.userTableWidget.cellDoubleClicked.connect(self.update_user_form)
        self.ui.bookTableWidget.cellDoubleClicked.connect(self.update_book_form)
        self.currentUser = user
        self.confirm = confirmView.ConfirmView()
        self.error = None
        self.userController = UserController()
        self.bookController = BookController()
        self.customize_scene()
        self.current_user_queries = ["", "", ""]
        self.current_book_queries = ["", "", ""]

        self.list_users()
        self.list_books()

    def customize_scene(self):
        self.ui.greetingLabel.setText("Hi, " + str(self.currentUser.name) + " " + str(self.currentUser.surname))
        self.ui.userTableWidget.setColumnCount(3)
        self.ui.bookTableWidget.setColumnCount(3)
        self.ui.userTableWidget.setHorizontalHeaderLabels(["Name", "Surname", "Username"])
        self.ui.bookTableWidget.setHorizontalHeaderLabels(["Title", "Author", "Published Year"])

    def reset_user_filters(self):
        self.current_user_queries = ["", "", ""]
        self.list_users()

    def reset_book_filters(self):
        self.current_book_queries = ["", "", ""]
        self.list_books()

    def delete_selected_user(self):
        selected_row = self.ui.userTableWidget.currentRow()
        selected_user = self.ui.userTableWidget.item(selected_row, 2).text()
        self.confirm.confirm_flag = 0
        self.confirm.confirmScreen.exec_()
        if self.confirm.confirm_flag is 2:
            self.userController.delete_one_user(selected_user)
        self.list_users()

    def delete_selected_book(self):
        selected_row = self.ui.bookTableWidget.currentRow()
        selected_book = self.ui.bookTableWidget.item(selected_row, 0).text()
        self.confirm.confirm_flag = 0
        self.confirm.confirmScreen.exec_()
        if self.confirm.confirm_flag is 2:
            self.bookController.delete_one_book(selected_book)
        self.list_books()

    def list_users(self):
        query_result = self.userController.search_users(self.current_user_queries[0], self.current_user_queries[1],
                                                        self.current_user_queries[2])
        i = 0
        current_row_count = query_result.count()
        self.ui.userTableWidget.setRowCount(current_row_count)

        for record in query_result:
            self.ui.userTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(record["name"]))
            self.ui.userTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(record["surname"]))
            self.ui.userTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(record["username"]))
            i = i + 1
        self.show()

    def list_books(self):
        query_result = self.bookController.search_books(self.current_book_queries[0], self.current_book_queries[1],
                                                        self.current_book_queries[2])
        i = 0
        current_row_count = query_result.count()
        self.ui.bookTableWidget.setRowCount(current_row_count)

        for record in query_result:
            self.ui.bookTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(record["title"]))
            self.ui.bookTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(record["author"]))
            self.ui.bookTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(record["year"]))
            i = i + 1
        self.show()

    def logout(self):
        import views.LoginView as LoginView
        self.librarianHome.hide()
        self.ui = LoginView.LoginView()
        self.ui.show()

    def show(self):
        self.librarianHome.show()

    def update_user_form(self):
        selected_row = self.ui.userTableWidget.currentRow()
        selected_user = self.ui.userTableWidget.item(selected_row, 2).text()
        self.userRegisterScreen.type = 1
        self.userRegisterScreen.currentUser = self.userController.get_user_by_username(selected_user)
        self.userRegisterScreen.prepare_update(self.userRegisterScreen.currentUser)
        self.userRegisterScreen.userRegisterFormScreen.exec_()
        self.list_users()

    def update_book_form(self):
        selected_row = self.ui.bookTableWidget.currentRow()
        selected_book = self.ui.bookTableWidget.item(selected_row, 0).text()
        self.bookRegisterScreen.type = 1
        self.bookRegisterScreen.currentBook = self.bookController.get_book_by_title(selected_book)
        self.bookRegisterScreen.prepare_update(self.bookRegisterScreen.currentBook)
        self.bookRegisterScreen.bookRegisterFormScreen.exec_()
        self.list_books()

    def register_user_form(self):
        self.userRegisterScreen.type = 0
        self.userRegisterScreen.clear_forms()
        self.userRegisterScreen.userRegisterFormScreen.exec_()
        self.list_users()

    def register_book_form(self):
        self.bookRegisterScreen.type = 0
        self.bookRegisterScreen.clear_forms()
        self.bookRegisterScreen.bookRegisterFormScreen.exec_()
        self.list_books()

    def search_users(self):
        search_username = self.ui.usernameLineEdit.text()
        search_name = self.ui.nameLineEdit.text()
        search_surname = self.ui.surnameLineEdit.text()
        self.current_user_queries = [search_username, search_name, search_surname]
        self.list_users()

    def search_books(self):
        search_title = self.ui.titleLineEdit.text()
        search_author = self.ui.authorLineEdit.text()
        search_year = self.ui.yearLineEdit.text()
        self.current_book_queries = [search_title, search_author, search_year]
        self.list_books()




        # def delete_user_operation(self):
        #     items = self.ui.userListView.selectedIndexes()
        #     aa = self.ui.userListView.model().itemData(self.ui.userListView.selectedIndexes()[0])
        #     print(aa[0])
        #     for data in items:
        #         print(data.row())
        #     self.confirm = confirmView.ConfirmView()
        #     self.confirm.show()
