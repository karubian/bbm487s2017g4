from PyQt5 import QtWidgets

from views.gen.Ui_MemberHome import Ui_MemberHome


class MemberHomeView(Ui_MemberHome):
    def __init__(self):
        self.memberHome = QtWidgets.QMainWindow()
        self.ui = Ui_MemberHome()
        self.ui.setupUi(self.memberHome)
        self.ui.LogoutButton.clicked.connect(self.logout)
        self.currentUser = None

    def customize_scene(self):
        self.ui.GreetingLabel.setText("Hi, " + str(self.currentUser.name) + " " + str(self.currentUser.surname))

    def logout(self):
        import views.LoginView as LoginController
        self.memberHome.hide()
        self.ui = LoginController.LoginController()
        self.ui.show()

    def show(self):
        self.memberHome.show()

