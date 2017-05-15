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
        self.set_button_effects()

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

    def set_button_effects(self):
        self.ui.yesButton.released.connect(self.released_color_change)
        self.ui.yesButton.pressed.connect(self.pressed_color_change)
        self.ui.noButton.released.connect(self.released_color_change)
        self.ui.noButton.pressed.connect(self.pressed_color_change)



    def released_color_change(self):
        self.confirmScreen.sender().setStyleSheet("QPushButton {\n"
                                                  "color: white;\n"
                                                  "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                                  "font-size: 30px;\n"
                                                  "border-radius:10px;\n"
                                                  "}")

    def pressed_color_change(self):
        self.confirmScreen.sender().setStyleSheet("QPushButton {\n"
                                                  "color: white;\n"
                                                  "background-color: red;\n"
                                                  "font-size: 30px;\n"
                                                  "border-radius:10px;\n"
                                                  "}")