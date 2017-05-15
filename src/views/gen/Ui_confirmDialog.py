# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_confirmDialog(object):
    def setupUi(self, confirmDialog):
        confirmDialog.setObjectName("confirmDialog")
        confirmDialog.resize(775, 370)
        confirmDialog.setMinimumSize(QtCore.QSize(775, 370))
        confirmDialog.setMaximumSize(QtCore.QSize(775, 370))
        confirmDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.confirmFrame = QtWidgets.QFrame(confirmDialog)
        self.confirmFrame.setGeometry(QtCore.QRect(0, 0, 771, 371))
        self.confirmFrame.setStyleSheet("QFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: rgb(255, 255, 222);\n"
"}")
        self.confirmFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.confirmFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.confirmFrame.setObjectName("confirmFrame")
        self.questionImg = QtWidgets.QLabel(self.confirmFrame)
        self.questionImg.setGeometry(QtCore.QRect(40, 80, 201, 181))
        self.questionImg.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 255, 222);\n"
"}")
        self.questionImg.setText("")
        self.questionImg.setPixmap(QtGui.QPixmap("../project/resources/question.png"))
        self.questionImg.setObjectName("questionImg")
        self.yesButton = QtWidgets.QPushButton(self.confirmFrame)
        self.yesButton.setGeometry(QtCore.QRect(260, 280, 221, 71))
        self.yesButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"border-radius:10px;\n"
"}")
        self.yesButton.setObjectName("yesButton")
        self.confirmMessage = QtWidgets.QLabel(self.confirmFrame)
        self.confirmMessage.setGeometry(QtCore.QRect(250, 30, 421, 221))
        self.confirmMessage.setStyleSheet("QLabel {\n"
"    font-size:30px;\n"
"border: 3px solid rgb(255, 255, 222);\n"
"\n"
"}")
        self.confirmMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.confirmMessage.setWordWrap(True)
        self.confirmMessage.setObjectName("confirmMessage")
        self.noButton = QtWidgets.QPushButton(self.confirmFrame)
        self.noButton.setGeometry(QtCore.QRect(500, 280, 221, 71))
        self.noButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"border-radius:10px;\n"
"\n"
"}")
        self.noButton.setObjectName("noButton")

        self.retranslateUi(confirmDialog)
        QtCore.QMetaObject.connectSlotsByName(confirmDialog)

    def retranslateUi(self, confirmDialog):
        _translate = QtCore.QCoreApplication.translate
        confirmDialog.setWindowTitle(_translate("confirmDialog", "Dialog"))
        self.yesButton.setText(_translate("confirmDialog", "YES"))
        self.confirmMessage.setText(_translate("confirmDialog", "Are you sure you want to delete this item ? "))
        self.noButton.setText(_translate("confirmDialog", "NO"))

