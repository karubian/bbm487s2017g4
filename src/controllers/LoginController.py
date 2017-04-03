from PyQt5 import QtCore, QtGui, QtWidgets
from views.Ui_Login import Ui_Login
import controllers.HomeController as HomeController
import utils.DbClient as DbClient


class LoginController(Ui_Login):
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
        user = self.ui.usernameText.text()
        password = self.ui.passText.text()

    def logmein(self):
        user = str(self.ui.usernameText.text())
        password = str(self.ui.passText.text())
        if self.dbClient.authorization(user, password):
            self.login.hide()
            self.ui = HomeController.HomeController()
            self.ui.currentUser = self.dbClient.init_user(user,password)
            self.ui.customize_scene()
            self.ui.show()
        else:
            self.ui.usernameText.setText("")
            self.ui.passText.setText("")
            self.ui.usernameText.setPlaceholderText("Wrong Credentials!")
            self.ui.passText.setPlaceholderText("Wrong Credentials!")
