# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_errorDialog(object):
    def setupUi(self, errorDialog):
        errorDialog.setObjectName("errorDialog")
        errorDialog.resize(661, 431)
        errorDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.okButton = QtWidgets.QPushButton(errorDialog)
        self.okButton.setGeometry(QtCore.QRect(240, 310, 221, 71))
        self.okButton.setStyleSheet("QPushButton {\n"
"    font-size:20px;\n"
"}")
        self.okButton.setObjectName("okButton")
        self.errorX = QtWidgets.QLabel(errorDialog)
        self.errorX.setGeometry(QtCore.QRect(10, 40, 251, 261))
        self.errorX.setText("")
        self.errorX.setPixmap(QtGui.QPixmap("resources/error.png"))
        self.errorX.setObjectName("errorX")
        self.errorMessage = QtWidgets.QLabel(errorDialog)
        self.errorMessage.setGeometry(QtCore.QRect(320, 30, 231, 221))
        self.errorMessage.setStyleSheet("QLabel {\n"
"    font-size:30px;\n"
"}")
        self.errorMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.errorMessage.setWordWrap(True)
        self.errorMessage.setObjectName("errorMessage")
        self.errorFrame = QtWidgets.QFrame(errorDialog)
        self.errorFrame.setGeometry(QtCore.QRect(0, 0, 661, 431))
        self.errorFrame.setStyleSheet("QFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: rgb(255, 255, 222);\n"
"}")
        self.errorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.errorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.errorFrame.setObjectName("errorFrame")
        self.errorFrame.raise_()
        self.errorX.raise_()
        self.errorMessage.raise_()
        self.okButton.raise_()

        self.retranslateUi(errorDialog)
        QtCore.QMetaObject.connectSlotsByName(errorDialog)

    def retranslateUi(self, errorDialog):
        _translate = QtCore.QCoreApplication.translate
        errorDialog.setWindowTitle(_translate("errorDialog", "Dialog"))
        self.okButton.setText(_translate("errorDialog", "OK"))
        self.errorMessage.setText(_translate("errorDialog", "Wrong password or username"))

