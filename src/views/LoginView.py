from PyQt5 import QtWidgets
from controllers.UserController import UserController
from controllers.LoanController import LoanController
import views.MemberHomeView as memberHomeView
import views.LibrarianHomeView as librarianHomeView
from views.gen.Ui_Login import Ui_Login
import views.ErrorView as errorView
import views.GuestWindowView as guestWindowView


class LoginView(Ui_Login):
    def __init__(self):
        self.login = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.login)
        self.ui.loginButton.clicked.connect(self.user_login)
        self.ui.searchButton.clicked.connect(self.guest_search)
        self.userController = UserController()
        self.error = errorView.ErrorView()
        self.ui.loginButton.released.connect(self.released_color_change)
        self.ui.loginButton.pressed.connect(self.pressed_color_change)
        self.ui.searchButton.released.connect(self.released_color_change)
        self.ui.searchButton.pressed.connect(self.pressed_color_change)

    def show(self):
        loan_controller = LoanController()
        loan_controller.update_fines()
        self.login.show()

    def clear_login_forms(self):
        self.ui.usernameText.setText("")
        self.ui.passText.setText("")

    def get_login_info(self):
        return self.ui.usernameText.text(), self.ui.passText.text()

    def guest_search(self):
        self.login.hide()
        self.ui = guestWindowView.GuestWindowView()
        self.ui.show()

    def user_login(self):
        user, password = self.get_login_info()
        if self.userController.authorization(user, password):
            current_user = self.userController.get_user_by_username(user)
            if current_user.type is "member":
                self.login.hide()
                self.ui = memberHomeView.MemberHomeView(current_user)
            elif current_user.type is "librarian":
                self.login.hide()
                self.ui = librarianHomeView.LibrarianHomeView(current_user)
            self.ui.show()
        else:
            self.error.set_error_text("Wrong username or password")
            self.error.show()
            self.clear_login_forms()


    def released_color_change(self):
        self.login.sender().setStyleSheet("QPushButton {\n"
                                                  "color: white;\n"
                                                  "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                                  "font-size: 30px;\n"
                                                  "border-radius:10px;\n"
                                                  "}")

    def pressed_color_change(self):
        self.login.sender().setStyleSheet("QPushButton {\n"
                                                  "color: white;\n"
                                                  "background-color: red;\n"
                                                  "font-size: 30px;\n"
                                                  "border-radius:10px;\n"
                                                  "}")