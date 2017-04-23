# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerUser.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_userRegisterForm(object):
    def setupUi(self, userRegisterForm):
        userRegisterForm.setObjectName("userRegisterForm")
        userRegisterForm.resize(639, 549)
        self.frame = QtWidgets.QFrame(userRegisterForm)
        self.frame.setGeometry(QtCore.QRect(0, 0, 641, 551))
        self.frame.setStyleSheet("QFrame {\n"
                                 "border: 3px solid gray;\n"
                                 "border-radius: 40px;\n"
                                 "background: rgb(255, 255, 222);\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.headerLabel = QtWidgets.QLabel(self.frame)
        self.headerLabel.setGeometry(QtCore.QRect(30, 10, 321, 71))
        self.headerLabel.setStyleSheet("QLabel {\n"
                                       "border: 3px solid rgb(255, 255, 222);\n"
                                       "font-size:40px;\n"
                                       "}")
        self.headerLabel.setObjectName("headerLabel")
        self.usernameLineEdit = QtWidgets.QLineEdit(self.frame)
        self.usernameLineEdit.setGeometry(QtCore.QRect(200, 110, 401, 51))
        self.usernameLineEdit.setStyleSheet("QLineEdit {\n"
                                            "padding: 1px;\n"
                                            "border-style: solid;\n"
                                            "border: 2px solid gray;\n"
                                            "border-radius: 8px;\n"
                                            "font-size:30px;\n"
                                            "}\n"
                                            "")
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.frame)
        self.passwordLineEdit.setGeometry(QtCore.QRect(200, 170, 401, 51))
        self.passwordLineEdit.setStyleSheet("QLineEdit {\n"
                                            "padding: 1px;\n"
                                            "border-style: solid;\n"
                                            "border: 2px solid gray;\n"
                                            "border-radius: 8px;\n"
                                            "font-size:30px;\n"
                                            "}\n"
                                            "")
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.nameLineEdit = QtWidgets.QLineEdit(self.frame)
        self.nameLineEdit.setGeometry(QtCore.QRect(200, 230, 401, 51))
        self.nameLineEdit.setStyleSheet("QLineEdit {\n"
                                        "padding: 1px;\n"
                                        "border-style: solid;\n"
                                        "border: 2px solid gray;\n"
                                        "border-radius: 8px;\n"
                                        "font-size:30px;\n"
                                        "}\n"
                                        "")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.surnameLineEdit = QtWidgets.QLineEdit(self.frame)
        self.surnameLineEdit.setGeometry(QtCore.QRect(200, 290, 401, 51))
        self.surnameLineEdit.setStyleSheet("QLineEdit {\n"
                                           "padding: 1px;\n"
                                           "border-style: solid;\n"
                                           "border: 2px solid gray;\n"
                                           "border-radius: 8px;\n"
                                           "font-size:30px;\n"
                                           "}\n"
                                           "")
        self.surnameLineEdit.setObjectName("surnameLineEdit")
        self.emailLineEdit = QtWidgets.QLineEdit(self.frame)
        self.emailLineEdit.setGeometry(QtCore.QRect(200, 350, 401, 51))
        self.emailLineEdit.setStyleSheet("QLineEdit {\n"
                                         "padding: 1px;\n"
                                         "border-style: solid;\n"
                                         "border: 2px solid gray;\n"
                                         "border-radius: 8px;\n"
                                         "font-size:30px;\n"
                                         "}\n"
                                         "")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.usernameLabel = QtWidgets.QLabel(self.frame)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 100, 171, 51))
        self.usernameLabel.setStyleSheet("QLabel {\n"
                                         "border: 3px solid rgb(255, 255, 222);\n"
                                         "font-size:30px;\n"
                                         "}")
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.frame)
        self.passwordLabel.setGeometry(QtCore.QRect(30, 160, 171, 51))
        self.passwordLabel.setStyleSheet("QLabel {\n"
                                         "border: 3px solid rgb(255, 255, 222);\n"
                                         "font-size:30px;\n"
                                         "}")
        self.passwordLabel.setObjectName("passwordLabel")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(80, 220, 111, 51))
        self.nameLabel.setStyleSheet("QLabel {\n"
                                     "border: 3px solid rgb(255, 255, 222);\n"
                                     "font-size:30px;\n"
                                     "}")
        self.nameLabel.setObjectName("nameLabel")
        self.emailLabel = QtWidgets.QLabel(self.frame)
        self.emailLabel.setGeometry(QtCore.QRect(80, 350, 111, 51))
        self.emailLabel.setStyleSheet("QLabel {\n"
                                      "border: 3px solid rgb(255, 255, 222);\n"
                                      "font-size:30px;\n"
                                      "}")
        self.emailLabel.setObjectName("emailLabel")
        self.surnameLabel = QtWidgets.QLabel(self.frame)
        self.surnameLabel.setGeometry(QtCore.QRect(40, 290, 151, 51))
        self.surnameLabel.setStyleSheet("QLabel {\n"
                                        "border: 3px solid rgb(255, 255, 222);\n"
                                        "font-size:30px;\n"
                                        "}")
        self.surnameLabel.setObjectName("surnameLabel")
        self.registerButton = QtWidgets.QPushButton(self.frame)
        self.registerButton.setGeometry(QtCore.QRect(40, 430, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("QPushButton {\n"
                                          "color: white;\n"
                                          "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                          "font-size: 30px;\n"
                                          "}")
        self.registerButton.setObjectName("registerButton")
        self.cancelButton = QtWidgets.QPushButton(self.frame)
        self.cancelButton.setGeometry(QtCore.QRect(340, 430, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("QPushButton {\n"
                                        "color: white;\n"
                                        "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                        "font-size: 30px;\n"
                                        "}")
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(userRegisterForm)
        QtCore.QMetaObject.connectSlotsByName(userRegisterForm)

    def retranslateUi(self, userRegisterForm):
        _translate = QtCore.QCoreApplication.translate
        userRegisterForm.setWindowTitle(_translate("userRegisterForm", "Form"))
        self.headerLabel.setText(_translate("userRegisterForm", "Register User"))
        self.usernameLabel.setText(_translate("userRegisterForm", "Username :"))
        self.passwordLabel.setText(_translate("userRegisterForm", "Password :"))
        self.nameLabel.setText(_translate("userRegisterForm", "Name :"))
        self.emailLabel.setText(_translate("userRegisterForm", "Email :"))
        self.surnameLabel.setText(_translate("userRegisterForm", "Surname :"))
        self.registerButton.setText(_translate("userRegisterForm", "Register"))
        self.cancelButton.setText(_translate("userRegisterForm", "Cancel"))
