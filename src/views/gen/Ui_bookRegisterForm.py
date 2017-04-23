# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerBook.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bookRegisterForm(object):
    def setupUi(self, bookRegisterForm):
        bookRegisterForm.setObjectName("bookRegisterForm")
        bookRegisterForm.resize(744, 463)
        self.frame = QtWidgets.QFrame(bookRegisterForm)
        self.frame.setGeometry(QtCore.QRect(0, 0, 741, 461))
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
        self.titleLineEdit = QtWidgets.QLineEdit(self.frame)
        self.titleLineEdit.setGeometry(QtCore.QRect(290, 110, 401, 51))
        self.titleLineEdit.setStyleSheet("QLineEdit {\n"
                                         "padding: 1px;\n"
                                         "border-style: solid;\n"
                                         "border: 2px solid gray;\n"
                                         "border-radius: 8px;\n"
                                         "font-size:30px;\n"
                                         "}\n"
                                         "")
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.authorLineEdit = QtWidgets.QLineEdit(self.frame)
        self.authorLineEdit.setGeometry(QtCore.QRect(290, 170, 401, 51))
        self.authorLineEdit.setStyleSheet("QLineEdit {\n"
                                          "padding: 1px;\n"
                                          "border-style: solid;\n"
                                          "border: 2px solid gray;\n"
                                          "border-radius: 8px;\n"
                                          "font-size:30px;\n"
                                          "}\n"
                                          "")
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.yearLineEdit = QtWidgets.QLineEdit(self.frame)
        self.yearLineEdit.setGeometry(QtCore.QRect(290, 230, 401, 51))
        self.yearLineEdit.setStyleSheet("QLineEdit {\n"
                                        "padding: 1px;\n"
                                        "border-style: solid;\n"
                                        "border: 2px solid gray;\n"
                                        "border-radius: 8px;\n"
                                        "font-size:30px;\n"
                                        "}\n"
                                        "")
        self.yearLineEdit.setObjectName("yearLineEdit")
        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(180, 110, 101, 51))
        self.titleLabel.setStyleSheet("QLabel {\n"
                                      "border: 3px solid rgb(255, 255, 222);\n"
                                      "font-size:30px;\n"
                                      "}")
        self.titleLabel.setObjectName("titleLabel")
        self.authorLabel = QtWidgets.QLabel(self.frame)
        self.authorLabel.setGeometry(QtCore.QRect(150, 170, 131, 41))
        self.authorLabel.setStyleSheet("QLabel {\n"
                                       "border: 3px solid rgb(255, 255, 222);\n"
                                       "font-size:30px;\n"
                                       "}")
        self.authorLabel.setObjectName("authorLabel")
        self.yearLabel = QtWidgets.QLabel(self.frame)
        self.yearLabel.setGeometry(QtCore.QRect(40, 230, 241, 51))
        self.yearLabel.setStyleSheet("QLabel {\n"
                                     "border: 3px solid rgb(255, 255, 222);\n"
                                     "font-size:30px;\n"
                                     "}")
        self.yearLabel.setObjectName("yearLabel")
        self.registerButton = QtWidgets.QPushButton(self.frame)
        self.registerButton.setGeometry(QtCore.QRect(80, 330, 271, 81))
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
        self.cancelButton.setGeometry(QtCore.QRect(420, 330, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("QPushButton {\n"
                                        "color: white;\n"
                                        "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                        "font-size: 30px;\n"
                                        "}")
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(bookRegisterForm)
        QtCore.QMetaObject.connectSlotsByName(bookRegisterForm)

    def retranslateUi(self, bookRegisterForm):
        _translate = QtCore.QCoreApplication.translate
        bookRegisterForm.setWindowTitle(_translate("bookRegisterForm", "Form"))
        self.headerLabel.setText(_translate("bookRegisterForm", "Register Book"))
        self.titleLabel.setText(_translate("bookRegisterForm", "Title :"))
        self.authorLabel.setText(_translate("bookRegisterForm", "Author :"))
        self.yearLabel.setText(_translate("bookRegisterForm", "Published Year :"))
        self.registerButton.setText(_translate("bookRegisterForm", "Register"))
        self.cancelButton.setText(_translate("bookRegisterForm", "Cancel"))
