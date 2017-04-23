from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_errorDialog import Ui_errorDialog


class ErrorView(Ui_errorDialog):
    def __init__(self):
        self.errorScreen = QtWidgets.QDialog()
        self.ui = Ui_errorDialog()
        self.ui.setupUi(self.errorScreen)
        self.ui.okButton.clicked.connect(self.terminate)

    def show(self):
        self.errorScreen.show()

    def set_error_text(self, message):
        self.ui.errorMessage.setText(message)

    def terminate(self):
        self.errorScreen.hide()
