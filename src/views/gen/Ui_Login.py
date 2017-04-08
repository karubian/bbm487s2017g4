# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
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
                            "background: rgb(240, 240, 240);\n"
                            "}")
        self.LoginFrame = QtWidgets.QFrame(Login)
        self.LoginFrame.setGeometry(QtCore.QRect(0, 0, 521, 381))
        self.LoginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginFrame.setObjectName("LoginFrame")
        self.LoginButton = QtWidgets.QPushButton(self.LoginFrame)
        self.LoginButton.setGeometry(QtCore.QRect(350, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("QPushButton {\n"
                                       "color: white;\n"
                                       "background-color: rgb(255, 170, 0);\n"
                                       "font-size: 15px;\n"
                                       "}")
        self.LoginButton.setObjectName("LoginButton")
        self.registerButton = QtWidgets.QPushButton(self.LoginFrame)
        self.registerButton.setGeometry(QtCore.QRect(120, 240, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("QPushButton {\n"
                                          "color: white;\n"
                                          "background-color: rgb(255, 170, 0);\n"
                                          "font-size: 15px;\n"
                                          "}")
        self.registerButton.setObjectName("registerButton")
        self.searchButton = QtWidgets.QPushButton(self.LoginFrame)
        self.searchButton.setGeometry(QtCore.QRect(120, 190, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("QPushButton {\n"
                                        "color: white;\n"
                                        "background-color: rgb(255, 170, 0);\n"
                                        "font-size: 15px;\n"
                                        "}")
        self.searchButton.setObjectName("searchButton")
        self.titleLabel = QtWidgets.QLabel(self.LoginFrame)
        self.titleLabel.setGeometry(QtCore.QRect(20, 10, 491, 101))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("QLabel {\n"
                                      "color:rgb(0, 0, 220);\n"
                                      "border: 3px solid rgb(240, 240, 240);\n"
                                      "border-radius: 40px;\n"
                                      "background:rgb(240, 240, 240);\n"
                                      "}")
        self.titleLabel.setTextFormat(QtCore.Qt.AutoText)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.usernameText = QtWidgets.QLineEdit(self.LoginFrame)
        self.usernameText.setGeometry(QtCore.QRect(120, 110, 221, 31))
        self.usernameText.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.usernameText.setObjectName("usernameText")
        self.passText = QtWidgets.QLineEdit(self.LoginFrame)
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


        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.LoginButton.setText(_translate("Login", "Login"))
        self.registerButton.setText(_translate("Login", "Register"))
        self.searchButton.setText(_translate("Login", "Search For Books (Guest) "))
        self.titleLabel.setText(_translate("Login", "Library Book Loan System"))
        self.usernameText.setPlaceholderText(_translate("Login", "Username"))
        self.passText.setPlaceholderText(_translate("Login", "Password"))


