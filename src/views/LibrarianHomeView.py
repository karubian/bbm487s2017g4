from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_LibrarianHome import Ui_libraryMainWindow
from controllers.UserController import UserController


class LibrarianHomeView(Ui_libraryMainWindow):
    def __init__(self):
        self.librarianHome = QtWidgets.QMainWindow()
        self.ui = Ui_libraryMainWindow()
        self.ui.setupUi(self.librarianHome)
        self.ui.logoutButton.clicked.connect(self.logout)
        self.currentUser = None
        self.userController = UserController()
        self.update_scroll_bar()

    def customize_scene(self):
        self.ui.greetingLabel.setText("Hi, " + str(self.currentUser.name) + " " + str(self.currentUser.surname))

    def update_scroll_bar(self):
        model = QtCore.QStringListModel()
        lisst = self.userController.get_all_users()
        model.setStringList(lisst)
        self.ui.userListView.setModel(model)
        # print(self.ui.userListView.selectedIndexes()

    def logout(self):
        # print(self.ui.userListView.selectedIndexes())
        import views.LoginView as LoginView
        self.librarianHome.hide()
        self.ui = LoginView.LoginView()
        self.ui.show()

    def show(self):
        self.librarianHome.show()
