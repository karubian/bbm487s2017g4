from PyQt5 import QtWidgets
from  controllers.UserController import UserController
import views.MemberHomeView as memberHomeView
import views.LibrarianHomeView as librarianHomeView
from views.gen.Ui_Login import Ui_Login


class LoginView(Ui_Login):
    def __init__(self):
        self.login = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.login)
        self.ui.loginButton.clicked.connect(self.logmein)
        self.userController = UserController()

    def show(self):
        self.login.show()

    def logmein(self):
        user = self.ui.usernameText.text()
        password = self.ui.passText.text()
        is_librarian = self.ui.userTypeRadio.isChecked()
        if self.userController.client.authorization(user, password,is_librarian):
            self.ui.currentUser = self.userController.get_user_by_username(user,is_librarian)
            if is_librarian is False:
                self.login.hide()
                self.ui = memberHomeView.MemberHomeView()
                # self.ui.customize_scene()
            else:
                self.login.hide()
                self.ui = librarianHomeView.LibrarianHomeView()
            self.ui.show()
        else:
            self.ui.usernameText.setText("")
            self.ui.passText.setText("")
            self.ui.usernameText.setPlaceholderText("Wrong Credentials!")
            self.ui.passText.setPlaceholderText("Wrong Credentials!")
