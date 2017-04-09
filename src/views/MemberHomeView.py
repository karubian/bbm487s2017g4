from PyQt5 import QtWidgets
from views.gen.Ui_MemberHome import Ui_memberMainWindow


class MemberHomeView(Ui_memberMainWindow):
    def __init__(self):
        self.memberHome = QtWidgets.QMainWindow()
        self.ui = Ui_memberMainWindow()
        self.ui.setupUi(self.memberHome)
        self.ui.logoutButton.clicked.connect(self.logout)
        self.currentUser = None

    def customize_scene(self):
        self.ui.greetingLabel.setText("Hi, " + str(self.currentUser.name) + " " + str(self.currentUser.surname))

    def logout(self):
        import views.LoginView as LoginView
        self.memberHome.hide()
        self.ui = LoginView.LoginView()
        self.ui.show()

    def show(self):
        self.memberHome.show()
