# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(522, 378)
        Login.setStyleSheet("QDialog {\n"
                            "background: gray;\n"
                            "}\n"
                            "\n"
                            "QFrame {\n"
                            "border: 3px solid gray;\n"
                            "border-radius: 40px;\n"
                            "background: rgb(255, 255, 222);\n"
                            "}")
        self.loginFrame = QtWidgets.QFrame(Login)
        self.loginFrame.setGeometry(QtCore.QRect(0, 0, 521, 381))
        self.loginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginFrame.setObjectName("loginFrame")
        self.loginButton = QtWidgets.QPushButton(self.loginFrame)
        self.loginButton.setGeometry(QtCore.QRect(350, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton {\n"
                                       "color: white;\n"
                                       "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                       "font-size: 15px;\n"
                                       "}")
        self.loginButton.setObjectName("loginButton")
        self.registerButton = QtWidgets.QPushButton(self.loginFrame)
        self.registerButton.setGeometry(QtCore.QRect(120, 240, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("QPushButton {\n"
                                          "color: white;\n"
                                          "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                          "font-size: 15px;\n"
                                          "}")
        self.registerButton.setObjectName("registerButton")
        self.searchButton = QtWidgets.QPushButton(self.loginFrame)
        self.searchButton.setGeometry(QtCore.QRect(120, 190, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("QPushButton {\n"
                                        "color: white;\n"
                                        "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                        "font-size: 15px;\n"
                                        "}")
        self.searchButton.setObjectName("searchButton")
        self.titleLabel = QtWidgets.QLabel(self.loginFrame)
        self.titleLabel.setGeometry(QtCore.QRect(20, 10, 491, 101))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("QLabel {\n"
                                      "color:gray;\n"
                                      "border: 3px solid rgb(255, 255, 222);\n"
                                      "border-radius: 40px;\n"
                                      "background:rgb(255, 255, 222);\n"
                                      "}")
        self.titleLabel.setTextFormat(QtCore.Qt.AutoText)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.usernameText = QtWidgets.QLineEdit(self.loginFrame)
        self.usernameText.setGeometry(QtCore.QRect(120, 110, 221, 31))
        self.usernameText.setStyleSheet("QLineEdit {\n"
                                        "padding: 1px;\n"
                                        "border-style: solid;\n"
                                        "border: 2px solid gray;\n"
                                        "border-radius: 8px;\n"
                                        "}\n"
                                        "")
        self.usernameText.setObjectName("usernameText")
        self.passText = QtWidgets.QLineEdit(self.loginFrame)
        self.passText.setGeometry(QtCore.QRect(120, 150, 221, 31))
        self.passText.setStyleSheet("QLineEdit {\n"
                                    "padding: 1px;\n"
                                    "border-style: solid;\n"
                                    "border: 2px solid gray;\n"
                                    "border-radius: 8px;\n"
                                    "}\n"
                                    "")
        self.passText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passText.setObjectName("passText")
        self.userTypeRadio = QtWidgets.QRadioButton(self.loginFrame)
        self.userTypeRadio.setGeometry(QtCore.QRect(120, 300, 251, 31))
        self.userTypeRadio.setObjectName("userTypeRadio")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.loginButton.setText(_translate("Login", "Login"))
        self.registerButton.setText(_translate("Login", "Register"))
        self.searchButton.setText(_translate("Login", "Search For Books (Guest) "))
        self.titleLabel.setText(_translate("Login", "Library Book Loan System"))
        self.usernameText.setPlaceholderText(_translate("Login", "Username"))
        self.passText.setPlaceholderText(_translate("Login", "Password"))
        self.userTypeRadio.setText(_translate("Login", "I am a librarian"))
