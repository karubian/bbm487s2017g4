from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_confirmDialog import Ui_confirmDialog


class ConfirmView(Ui_confirmDialog):
    def __init__(self):
        self.confirmScreen = QtWidgets.QDialog()
        self.ui = Ui_confirmDialog()
        self.ui.setupUi(self.confirmScreen)
        self.confirm_flag = None
        self.ui.noButton.clicked.connect(self.do_nothing)
        self.ui.yesButton.clicked.connect(self.confirm_operation)

    def show(self):
        self.confirmScreen.show()

    def set_confirm_text(self, message):
        self.ui.confirmMessage.setText(message)

    def do_nothing(self):
        self.confirm_flag = 0
        self.confirmScreen.hide()

    def confirm_operation(self):
        self.confirm_flag = 1
        self.confirmScreen.hide()

