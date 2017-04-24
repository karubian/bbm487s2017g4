from PyQt5 import QtWidgets
from controllers.UserController import UserController
import views.MemberHomeView as memberHomeView
import views.LibrarianHomeView as librarianHomeView
from views.gen.Ui_Login import Ui_Login
import views.ErrorView as errorView


class LoginView(Ui_Login):
    def __init__(self):
        self.login = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.login)
        self.ui.loginButton.clicked.connect(self.user_login)
        self.userController = UserController()
        self.error = errorView.ErrorView()

    def show(self):
        self.login.show()

    def clear_login_forms(self):
        self.ui.usernameText.setText("")
        self.ui.passText.setText("")

    def get_login_info(self):
        return self.ui.usernameText.text(), self.ui.passText.text()

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
