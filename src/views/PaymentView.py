from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_paymentDialog import Ui_paymentDialog
import views.ConfirmView as confirmView


class PaymentView(Ui_paymentDialog):
    def __init__(self, fineAmount):
        self.paymentPrompt = QtWidgets.QDialog()
        self.ui = Ui_paymentDialog()
        self.ui.setupUi(self.paymentPrompt)
        self.confirm = confirmView.ConfirmView()
        self.fineAmount = fineAmount
        self.paymentFlag = 0
        self.ui.proceedButton.clicked.connect(self.transaction)
        self.ui.proceedButton_2.clicked.connect(self.terminate)
        self.ui.priceLabel.setText(str(self.fineAmount) + " TL")
        self.set_button_effects()
    def show(self):
        self.paymentPrompt.show()

    def terminate(self):
        self.paymentPrompt.hide()

    def transaction(self):
        self.confirm.set_confirm_text("Are you sure you want to pay " + str(self.fineAmount) + " TL as fine ? ")
        self.confirm.confirmScreen.exec_()
        if self.confirm.confirm_flag:
            self.paymentFlag = 1
            self.paymentPrompt.hide()

    def set_button_effects(self):
        self.ui.proceedButton_2.released.connect(self.released_color_change)
        self.ui.proceedButton_2.pressed.connect(self.pressed_color_change)
        self.ui.proceedButton.released.connect(self.released_color_change)
        self.ui.proceedButton.pressed.connect(self.pressed_color_change)



    def released_color_change(self):
        self.paymentPrompt.sender().setStyleSheet("QPushButton {\n"
                                                  "color: white;\n"
                                                  "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                                  "font-size: 30px;\n"
                                                  "border-radius:10px;\n"
                                                  "}")

    def pressed_color_change(self):
        self.paymentPrompt.sender().setStyleSheet("QPushButton {\n"
                                                  "color: white;\n"
                                                  "background-color: red;\n"
                                                  "font-size: 30px;\n"
                                                  "border-radius:10px;\n"
                                                  "}")