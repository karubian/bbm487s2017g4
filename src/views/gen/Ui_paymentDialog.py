# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payment.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_paymentDialog(object):
    def setupUi(self, paymentDialog):
        paymentDialog.setObjectName("paymentDialog")
        paymentDialog.resize(662, 351)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(paymentDialog.sizePolicy().hasHeightForWidth())
        paymentDialog.setSizePolicy(sizePolicy)
        paymentDialog.setMinimumSize(QtCore.QSize(662, 351))
        paymentDialog.setMaximumSize(QtCore.QSize(662, 351))
        paymentDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.paymentFrame = QtWidgets.QFrame(paymentDialog)
        self.paymentFrame.setGeometry(QtCore.QRect(0, 0, 661, 351))
        self.paymentFrame.setStyleSheet("QFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: rgb(255, 255, 222);\n"
"}")
        self.paymentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.paymentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.paymentFrame.setObjectName("paymentFrame")
        self.paymentLabel = QtWidgets.QLabel(self.paymentFrame)
        self.paymentLabel.setGeometry(QtCore.QRect(150, 30, 221, 51))
        self.paymentLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 255, 222);\n"
"font-size:30px;\n"
"}")
        self.paymentLabel.setObjectName("paymentLabel")
        self.priceLabel = QtWidgets.QLabel(self.paymentFrame)
        self.priceLabel.setGeometry(QtCore.QRect(380, 30, 231, 51))
        self.priceLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 255, 222);\n"
"font-size:30px;\n"
"}")
        self.priceLabel.setObjectName("priceLabel")
        self.cardNumberLabel = QtWidgets.QLabel(self.paymentFrame)
        self.cardNumberLabel.setGeometry(QtCore.QRect(20, 130, 211, 51))
        self.cardNumberLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 255, 222);\n"
"font-size:30px;\n"
"}")
        self.cardNumberLabel.setObjectName("cardNumberLabel")
        self.paymentLineEdit = QtWidgets.QLineEdit(self.paymentFrame)
        self.paymentLineEdit.setGeometry(QtCore.QRect(240, 140, 401, 41))
        self.paymentLineEdit.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"font-size:30px;\n"
"}\n"
"")
        self.paymentLineEdit.setObjectName("paymentLineEdit")
        self.proceedButton = QtWidgets.QPushButton(self.paymentFrame)
        self.proceedButton.setGeometry(QtCore.QRect(80, 240, 221, 71))
        self.proceedButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"border-radius:10px;\n"
"}")
        self.proceedButton.setObjectName("proceedButton")
        self.proceedButton_2 = QtWidgets.QPushButton(self.paymentFrame)
        self.proceedButton_2.setGeometry(QtCore.QRect(360, 240, 221, 71))
        self.proceedButton_2.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"border-radius:10px;\n"
"}")
        self.proceedButton_2.setObjectName("proceedButton_2")

        self.retranslateUi(paymentDialog)
        QtCore.QMetaObject.connectSlotsByName(paymentDialog)

    def retranslateUi(self, paymentDialog):
        _translate = QtCore.QCoreApplication.translate
        paymentDialog.setWindowTitle(_translate("paymentDialog", "Dialog"))
        self.paymentLabel.setText(_translate("paymentDialog", "Total Payment :"))
        self.priceLabel.setText(_translate("paymentDialog", "20 TRY"))
        self.cardNumberLabel.setText(_translate("paymentDialog", "Card Number :"))
        self.proceedButton.setText(_translate("paymentDialog", "Proceed"))
        self.proceedButton_2.setText(_translate("paymentDialog", "Cancel"))

