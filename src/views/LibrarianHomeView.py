from PyQt5 import QtWidgets
from views.gen.Ui_LibrarianHome import Ui_libraryMainWindow


class LibrarianHomeView(Ui_libraryMainWindow):
    def __init__(self):
        self.librarianHome = QtWidgets.QMainWindow()
        self.ui = Ui_libraryMainWindow()
        self.ui.setupUi(self.librarianHome)
        self.ui.logoutButton.clicked.connect(self.logout)
        self.currentUser = None

    def customize_scene(self):
        self.ui.greetingLabel.setText("Hi, " + str(self.currentUser.name) + " " + str(self.currentUser.surname))

    def logout(self):
        import views.LoginView as LoginView
        self.librarianHome.hide()
        self.ui = LoginView.LoginView()
        self.ui.show()

    def show(self):
        self.librarianHome.show()
