from PyQt5 import QtWidgets

import utils.DbClient as DbClient
import views.MemberHomeView as HomeController
from views.gen.Ui_Login import Ui_Login


class LoginView(Ui_Login):
    def __init__(self):
        self.login = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.login)
        self.ui.LoginButton.clicked.connect(self.button_click)
        self.ui.LoginButton.clicked.connect(self.logmein)
        self.dbClient = DbClient.DbClient()

    def show(self):
        self.login.show()

    def button_click(self):
        pass

    def logmein(self):
        user = str(self.ui.usernameText.text())
        password = str(self.ui.passText.text())
        if self.dbClient.authorization(user, password):
            self.login.hide()
            self.ui = HomeController.HomeController()
            self.ui.currentUser = self.dbClient.init_user(user, password)
            self.ui.customize_scene()
            self.ui.show()
        else:
            self.ui.usernameText.setText("")
            self.ui.passText.setText("")
            self.ui.usernameText.setPlaceholderText("Wrong Credentials!")
            self.ui.passText.setPlaceholderText("Wrong Credentials!")
