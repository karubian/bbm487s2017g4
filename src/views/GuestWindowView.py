from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_guestWindow import Ui_guestWindow
from controllers.BookController import BookController


class GuestWindowView(Ui_guestWindow):
    def __init__(self):
        self.guestSearchScreen = QtWidgets.QMainWindow()
        self.ui = Ui_guestWindow()
        self.bookController = BookController()
        self.ui.searchButton.clicked.connect(self.terminate)
        self.ui.setupUi(self.guestSearchScreen)

    def show(self):
        self.guestSearchScreen.show()

    def terminate(self):
        pass
