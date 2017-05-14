# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notification.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_notifDialog(object):
    def setupUi(self, notifDialog):
        notifDialog.setObjectName("notifDialog")
        notifDialog.resize(662, 429)
        notifDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.okButton = QtWidgets.QPushButton(notifDialog)
        self.okButton.setGeometry(QtCore.QRect(240, 310, 221, 71))
        self.okButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.okButton.setObjectName("okButton")
        self.norifFrame = QtWidgets.QFrame(notifDialog)
        self.norifFrame.setGeometry(QtCore.QRect(0, 0, 661, 431))
        self.norifFrame.setStyleSheet("QFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: rgb(255, 255, 222);\n"
"}")
        self.norifFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.norifFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.norifFrame.setObjectName("norifFrame")
        self.label = QtWidgets.QLabel(self.norifFrame)
        self.label.setGeometry(QtCore.QRect(10, 40, 201, 221))
        self.label.setStyleSheet("QLabel {\n"
"border:0px\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../project/resources/notification.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.notifMessage = QtWidgets.QLabel(self.norifFrame)
        self.notifMessage.setGeometry(QtCore.QRect(230, 40, 411, 221))
        self.notifMessage.setStyleSheet("QLabel {\n"
"    font-size:30px;\n"
"    border:0px;\n"
"}")
        self.notifMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.notifMessage.setWordWrap(True)
        self.notifMessage.setObjectName("notifMessage")
        self.norifFrame.raise_()
        self.okButton.raise_()

        self.retranslateUi(notifDialog)
        QtCore.QMetaObject.connectSlotsByName(notifDialog)

    def retranslateUi(self, notifDialog):
        _translate = QtCore.QCoreApplication.translate
        notifDialog.setWindowTitle(_translate("notifDialog", "Dialog"))
        self.okButton.setText(_translate("notifDialog", "OK"))
        self.notifMessage.setText(_translate("notifDialog", "Ahmet is available now to rent nkjnk"))

