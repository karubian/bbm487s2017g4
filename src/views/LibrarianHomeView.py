from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_LibrarianHome import Ui_libraryMainWindow
from controllers.UserController import UserController
from controllers.BookController import BookController
import views.ConfirmView as confirmView
import views.ErrorView as errorView
import views.UserRegisterFormView as userRegisterFormView
import views.BookRegisterFormView as bookRegisterFormView
import datetime


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
        self.error = errorView.ErrorView()
        self.userController = UserController()
        self.bookController = BookController()
        self.customize_scene()
        self.current_user_queries = ["", "", ""]
        self.current_book_queries = ["", "", ""]
        self.set_button_effects()
        self.book_ids = []
        self.user_ids = []

        self.list_users()
        self.list_books()

    def customize_scene(self):
        self.ui.greetingLabel.setText("Hi, " + str(self.currentUser.name) + " " + str(self.currentUser.surname))
        self.ui.dateLabel.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
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
        if selected_row > -1:
            #selected_user = self.ui.userTableWidget.item(selected_row, 2).text()
            selected_user_id = self.user_ids[selected_row]
            self.confirm.confirm_flag = 0
            self.confirm.confirmScreen.exec_()
            if self.confirm.confirm_flag is 1:
                self.userController.delete_one_user(selected_user_id)
            self.list_users()

    def delete_selected_book(self):
        selected_row = self.ui.bookTableWidget.currentRow()
        if selected_row > -1:
            #selected_book = self.ui.bookTableWidget.item(selected_row, 0).text()
            selected_book_id = self.book_ids[selected_row]
            self.confirm.confirm_flag = 0
            self.confirm.confirmScreen.exec_()
            if self.confirm.confirm_flag is 1:
                if self.bookController.get_book_by_id(selected_book_id).isAvailable:
                    self.bookController.delete_one_book_by_id(selected_book_id)
                    self.userController.delete_from_all_owned_books(selected_book_id)
            self.list_books()

    def list_users(self):
        self.user_ids = []
        query_result = self.userController.search_users(self.current_user_queries[0], self.current_user_queries[1],
                                                        self.current_user_queries[2])
        i = 0
        current_row_count = query_result.count()
        self.ui.userTableWidget.setRowCount(current_row_count)
        for record in query_result:
            self.user_ids.insert(i,record["_id"])
            self.ui.userTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(record["name"]))
            self.ui.userTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(record["surname"]))
            self.ui.userTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(record["username"]))
            i = i + 1
        self.show()

    def list_books(self):
        self.book_ids = []
        query_result = self.bookController.search_books(self.current_book_queries[0], self.current_book_queries[1],
                                                        self.current_book_queries[2])
        i = 0
        current_row_count = query_result.count()
        self.ui.bookTableWidget.setRowCount(current_row_count)
        for record in query_result:
            self.book_ids.insert(i,record["_id"])
            self.ui.bookTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(record["title"]))
            self.ui.bookTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(record["author"]))
            self.ui.bookTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(record["year"]))
            if record["isAvailable"] is False:
                self.ui.bookTableWidget.item(i, 0).setBackground(QtGui.QColor(255, 68, 68))
                self.ui.bookTableWidget.item(i, 1).setBackground(QtGui.QColor(255, 68, 68))
                self.ui.bookTableWidget.item(i, 2).setBackground(QtGui.QColor(255, 68, 68))
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
        if selected_row > -1:
            #selected_user = self.ui.userTableWidget.item(selected_row, 2).text()
            selected_user_id = self.user_ids[selected_row]
            self.userRegisterScreen.type = 1
            self.userRegisterScreen.currentUser = self.userController.get_user_by_id(selected_user_id)
            self.userRegisterScreen.prepare_update(self.userRegisterScreen.currentUser)
            self.userRegisterScreen.userRegisterFormScreen.exec_()
            self.list_users()

    def update_book_form(self):
        selected_row = self.ui.bookTableWidget.currentRow()
        if selected_row > -1:
            #selected_book = self.ui.bookTableWidget.item(selected_row, 0).text()
            selected_book_id = self.book_ids[selected_row]
            self.bookRegisterScreen.type = 1
            self.bookRegisterScreen.currentBook = self.bookController.get_book_by_id(selected_book_id)
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

    def released_color_change(self):
        self.librarianHome.sender().setStyleSheet("QPushButton {\n"
                                                  "color: white;\n"
                                                  "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                                  "font-size: 30px;\n"
                                                  "}")

    def pressed_color_change(self):
        self.librarianHome.sender().setStyleSheet("QPushButton {\n"
                                                  "color: white;\n"
                                                  "background-color: red;\n"
                                                  "font-size: 30px;\n"
                                                  "}")

    def set_button_effects(self):
        self.ui.logoutButton.released.connect(self.released_color_change)
        self.ui.logoutButton.pressed.connect(self.pressed_color_change)
        self.ui.userSearchButton.released.connect(self.released_color_change)
        self.ui.userSearchButton.pressed.connect(self.pressed_color_change)
        self.ui.userCreateButton.released.connect(self.released_color_change)
        self.ui.userCreateButton.pressed.connect(self.pressed_color_change)
        self.ui.userDeleteButton.released.connect(self.released_color_change)
        self.ui.userDeleteButton.pressed.connect(self.pressed_color_change)
        self.ui.userUpdateButton.released.connect(self.released_color_change)
        self.ui.userUpdateButton.pressed.connect(self.pressed_color_change)
        self.ui.bookSearchButton.released.connect(self.released_color_change)
        self.ui.bookSearchButton.pressed.connect(self.pressed_color_change)
        self.ui.bookDeleteButton.released.connect(self.released_color_change)
        self.ui.bookDeleteButton.pressed.connect(self.pressed_color_change)
        self.ui.bookCreateButton.released.connect(self.released_color_change)
        self.ui.bookCreateButton.pressed.connect(self.pressed_color_change)
        self.ui.bookResetButton.released.connect(self.released_color_change)
        self.ui.bookResetButton.pressed.connect(self.pressed_color_change)
        self.ui.bookUpdateButton.released.connect(self.released_color_change)
        self.ui.bookUpdateButton.pressed.connect(self.pressed_color_change)
        self.ui.userResetButton.released.connect(self.released_color_change)
        self.ui.userResetButton.pressed.connect(self.pressed_color_change)

    # def delete_user_operation(self):
    #     items = self.ui.userListView.selectedIndexes()
    #     aa = self.ui.userListView.model().itemData(self.ui.userListView.selectedIndexes()[0])
    #     print(aa[0])
    #     for data in items:
    #         print(data.row())
    #     self.confirm = confirmView.ConfirmView()
    #     self.confirm.show()
