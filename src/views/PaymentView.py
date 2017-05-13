from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_paymentDialog import Ui_paymentDialog
import views.ConfirmView as confirmView

class PaymentView(Ui_paymentDialog):
    def __init__(self,fineAmount):
        self.paymentPrompt = QtWidgets.QDialog()
        self.ui = Ui_paymentDialog()
        self.ui.setupUi(self.paymentPrompt)
        self.confirm = confirmView.ConfirmView()
        self.fineAmount = fineAmount
        self.paymentFlag = 0
        self.ui.proceedButton.clicked.connect(self.transaction)

    def show(self):
        self.paymentPrompt.show()

    def transaction(self):
        self.confirm.set_confirm_text("Are you sure you want to pay " + str(self.fineAmount) + " TRY as fine ? ")
        self.confirm.confirmScreen.exec_()
        if self.confirm.confirm_flag:
            self.paymentFlag = 1
            self.paymentPrompt.hide()


