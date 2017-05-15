from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_notifDialog import Ui_notifDialog


class NotificationView(Ui_notifDialog):
    def __init__(self):
        self.notificationScreen = QtWidgets.QDialog()
        self.ui = Ui_notifDialog()
        self.ui.setupUi(self.notificationScreen)
        self.ui.okButton.clicked.connect(self.terminate)
        self.set_button_effects()

    def show(self):
        self.notificationScreen.show()

    def set_notif_text(self, message):
        self.ui.notifMessage.setText(message)

    def terminate(self):
        self.notificationScreen.hide()

    def set_button_effects(self):
        self.ui.okButton.released.connect(self.released_color_change)
        self.ui.okButton.pressed.connect(self.pressed_color_change)



    def released_color_change(self):
        self.notificationScreen.sender().setStyleSheet("QPushButton {\n"
                                                  "color: white;\n"
                                                  "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                                  "font-size: 30px;\n"
                                                  "border-radius:10px;\n"
                                                  "}")

    def pressed_color_change(self):
        self.notificationScreen.sender().setStyleSheet("QPushButton {\n"
                                                  "color: white;\n"
                                                  "background-color: red;\n"
                                                  "font-size: 30px;\n"
                                                  "border-radius:10px;\n"
                                                  "}")