from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_notifDialog import Ui_notifDialog


class NotificationView(Ui_notifDialog):
    def __init__(self):
        self.notificationScreen = QtWidgets.QDialog()
        self.ui = Ui_notifDialog()
        self.ui.setupUi(self.notificationScreen)
        self.ui.okButton.clicked.connect(self.terminate)

    def show(self):
        self.notificationScreen.show()

    def set_notif_text(self, message):
        self.ui.notifMessage.setText(message)

    def terminate(self):
        self.notificationScreen.hide()
