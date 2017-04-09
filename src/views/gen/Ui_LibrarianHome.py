# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'librarian.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_libraryMainWindow(object):
    def setupUi(self, libraryMainWindow):
        libraryMainWindow.setObjectName("libraryMainWindow")
        libraryMainWindow.resize(723, 471)
        libraryMainWindow.setStyleSheet("QFrame {\n"
                                        "border: 3px solid gray;\n"
                                        "border-radius: 40px;\n"
                                        "background: white;\n"
                                        "}")
        self.centralwidget = QtWidgets.QWidget(libraryMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.librarianMainFrame = QtWidgets.QFrame(self.centralwidget)
        self.librarianMainFrame.setGeometry(QtCore.QRect(0, 0, 721, 471))
        self.librarianMainFrame.setSizeIncrement(QtCore.QSize(10, 0))
        self.librarianMainFrame.setStyleSheet("QFrame {\n"
                                              "border: 3px solid gray;\n"
                                              "border-radius: 40px;\n"
                                              "background: rgb(255, 255, 222);\n"
                                              "}")
        self.librarianMainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.librarianMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.librarianMainFrame.setObjectName("librarianMainFrame")
        self.greetingLabel = QtWidgets.QLabel(self.librarianMainFrame)
        self.greetingLabel.setGeometry(QtCore.QRect(30, 10, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.greetingLabel.setFont(font)
        self.greetingLabel.setStyleSheet("QLabel {\n"
                                         "border: 3px solid rgb(255, 255, 222);\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.greetingLabel.setWordWrap(False)
        self.greetingLabel.setObjectName("greetingLabel")
        self.dateLabel = QtWidgets.QLabel(self.librarianMainFrame)
        self.dateLabel.setGeometry(QtCore.QRect(30, 10, 81, 20))
        self.dateLabel.setStyleSheet("QLabel {\n"
                                     "border: 3px solid rgb(255, 255, 222);\n"
                                     "}")
        self.dateLabel.setObjectName("dateLabel")
        self.tabWidget = QtWidgets.QTabWidget(self.librarianMainFrame)
        self.tabWidget.setGeometry(QtCore.QRect(20, 80, 681, 361))
        self.tabWidget.setStyleSheet("QWidget {\n"
                                     "border: 2px solid gray;\n"
                                     "border-radius: 0px;\n"
                                     "background: rgb(233, 255, 254);\n"
                                     "}")
        self.tabWidget.setObjectName("tabWidget")
        self.bookTab = QtWidgets.QWidget()
        self.bookTab.setObjectName("bookTab")
        self.formLayoutWidget = QtWidgets.QWidget(self.bookTab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 20, 391, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.bookForm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.bookForm.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.bookForm.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.bookForm.setFormAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.bookForm.setContentsMargins(0, 0, 0, 0)
        self.bookForm.setObjectName("bookForm")
        self.titleLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.titleLineEdit.setStyleSheet("QLineEdit {\n"
                                         "background-color:white;\n"
                                         "}")
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.bookForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleLineEdit)
        self.iSBNLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.iSBNLabel.setStyleSheet("QLabel {\n"
                                     "background-color:white;\n"
                                     "}")
        self.iSBNLabel.setObjectName("iSBNLabel")
        self.bookForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.iSBNLabel)
        self.iSBNLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.iSBNLineEdit.setStyleSheet("QLineEdit {\n"
                                        "background-color:white;\n"
                                        "}")
        self.iSBNLineEdit.setObjectName("iSBNLineEdit")
        self.bookForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.iSBNLineEdit)
        self.authorLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.authorLabel.setStyleSheet("QLabel {\n"
                                       "background-color:white;\n"
                                       "}")
        self.authorLabel.setObjectName("authorLabel")
        self.bookForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.authorLabel)
        self.authorLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.authorLineEdit.setStyleSheet("QLineEdit {\n"
                                          "background-color:white;\n"
                                          "}")
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.bookForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.authorLineEdit)
        self.categoryLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.categoryLabel.setStyleSheet("QLabel {\n"
                                         "background-color:white;\n"
                                         "}")
        self.categoryLabel.setObjectName("categoryLabel")
        self.bookForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
        self.titleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.titleLabel.setStyleSheet("QLabel {\n"
                                      "background-color:white;\n"
                                      "}")
        self.titleLabel.setObjectName("titleLabel")
        self.bookForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.categoryLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.categoryLineEdit.setStyleSheet("QLineEdit {\n"
                                            "background-color:white;\n"
                                            "}")
        self.categoryLineEdit.setObjectName("categoryLineEdit")
        self.bookForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.categoryLineEdit)
        self.bookSearchButton = QtWidgets.QPushButton(self.bookTab)
        self.bookSearchButton.setGeometry(QtCore.QRect(470, 20, 141, 31))
        self.bookSearchButton.setStyleSheet("QPushButton {\n"
                                            "color: white;\n"
                                            "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                            "font-size: 20px;\n"
                                            "}")
        self.bookSearchButton.setObjectName("bookSearchButton")
        self.bookDeleteButton = QtWidgets.QPushButton(self.bookTab)
        self.bookDeleteButton.setGeometry(QtCore.QRect(470, 150, 141, 31))
        self.bookDeleteButton.setStyleSheet("QPushButton {\n"
                                            "color: white;\n"
                                            "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                            "font-size: 20px;\n"
                                            "}")
        self.bookDeleteButton.setObjectName("bookDeleteButton")
        self.bookUpdateButton = QtWidgets.QPushButton(self.bookTab)
        self.bookUpdateButton.setGeometry(QtCore.QRect(470, 190, 141, 31))
        self.bookUpdateButton.setStyleSheet("QPushButton {\n"
                                            "color: white;\n"
                                            "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                            "font-size: 20px;\n"
                                            "}")
        self.bookUpdateButton.setObjectName("bookUpdateButton")
        self.bookScrollArea = QtWidgets.QScrollArea(self.bookTab)
        self.bookScrollArea.setGeometry(QtCore.QRect(50, 150, 401, 131))
        self.bookScrollArea.setStyleSheet("QScrollArea {\n"
                                          "background-color: rgb(85, 255, 255);}")
        self.bookScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.bookScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bookScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.bookScrollArea.setWidgetResizable(True)
        self.bookScrollArea.setObjectName("bookScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 376, 127))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.bookScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.bookCreateButton = QtWidgets.QPushButton(self.bookTab)
        self.bookCreateButton.setGeometry(QtCore.QRect(470, 60, 141, 31))
        self.bookCreateButton.setStyleSheet("QPushButton {\n"
                                            "color: white;\n"
                                            "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                            "font-size: 20px;\n"
                                            "}")
        self.bookCreateButton.setObjectName("bookCreateButton")
        self.tabWidget.addTab(self.bookTab, "")
        self.userTab = QtWidgets.QWidget()
        self.userTab.setObjectName("userTab")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.userTab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(50, 20, 391, 53))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.userForm = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.userForm.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.userForm.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.userForm.setFormAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.userForm.setContentsMargins(0, 0, 0, 0)
        self.userForm.setObjectName("userForm")
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.usernameLabel.setStyleSheet("QLabel {\n"
                                         "background-color:white;\n"
                                         "}")
        self.usernameLabel.setObjectName("usernameLabel")
        self.userForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.usernameLineEdit.setStyleSheet("QLineEdit {\n"
                                            "background-color:white;\n"
                                            "}")
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.userForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.idLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.idLabel.setStyleSheet("QLabel {\n"
                                   "background-color:white;\n"
                                   "}")
        self.idLabel.setObjectName("idLabel")
        self.userForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.idLabel)
        self.idLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.idLineEdit.setStyleSheet("QLineEdit {\n"
                                      "background-color:white;\n"
                                      "}")
        self.idLineEdit.setObjectName("idLineEdit")
        self.userForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.idLineEdit)
        self.userScrollArea = QtWidgets.QScrollArea(self.userTab)
        self.userScrollArea.setGeometry(QtCore.QRect(50, 150, 401, 131))
        self.userScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.userScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.userScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.userScrollArea.setWidgetResizable(True)
        self.userScrollArea.setObjectName("userScrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 376, 127))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.userScrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.userSearchButton = QtWidgets.QPushButton(self.userTab)
        self.userSearchButton.setGeometry(QtCore.QRect(470, 20, 141, 31))
        self.userSearchButton.setStyleSheet("QPushButton {\n"
                                            "color: white;\n"
                                            "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                            "font-size: 20px;\n"
                                            "}")
        self.userSearchButton.setObjectName("userSearchButton")
        self.userUpdateButton = QtWidgets.QPushButton(self.userTab)
        self.userUpdateButton.setGeometry(QtCore.QRect(470, 190, 141, 31))
        self.userUpdateButton.setStyleSheet("QPushButton {\n"
                                            "color: white;\n"
                                            "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                            "font-size: 20px;\n"
                                            "}")
        self.userUpdateButton.setObjectName("userUpdateButton")
        self.userDeleteButton = QtWidgets.QPushButton(self.userTab)
        self.userDeleteButton.setGeometry(QtCore.QRect(470, 150, 141, 31))
        self.userDeleteButton.setStyleSheet("QPushButton {\n"
                                            "color: white;\n"
                                            "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                            "font-size: 20px;\n"
                                            "}")
        self.userDeleteButton.setObjectName("userDeleteButton")
        self.userCreateButton = QtWidgets.QPushButton(self.userTab)
        self.userCreateButton.setGeometry(QtCore.QRect(470, 60, 141, 31))
        self.userCreateButton.setStyleSheet("QPushButton {\n"
                                            "color: white;\n"
                                            "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                            "font-size: 20px;\n"
                                            "}")
        self.userCreateButton.setObjectName("userCreateButton")
        self.tabWidget.addTab(self.userTab, "")
        self.logoutButton = QtWidgets.QPushButton(self.librarianMainFrame)
        self.logoutButton.setGeometry(QtCore.QRect(520, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.logoutButton.setFont(font)
        self.logoutButton.setStyleSheet("QPushButton {\n"
                                        "color: white;\n"
                                        "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                        "font-size: 20px;\n"
                                        "}")
        self.logoutButton.setObjectName("logoutButton")
        libraryMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(libraryMainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(libraryMainWindow)

    def retranslateUi(self, libraryMainWindow):
        _translate = QtCore.QCoreApplication.translate
        libraryMainWindow.setWindowTitle(_translate("libraryMainWindow", "Home - Librarian"))
        self.librarianMainFrame.setWhatsThis(
            _translate("libraryMainWindow", "<html><head/><body><p>BUrak</p><p><br/></p></body></html>"))
        self.greetingLabel.setText(_translate("libraryMainWindow", "Welcome back, John Doe"))
        self.dateLabel.setText(_translate("libraryMainWindow", "10.05.2017"))
        self.iSBNLabel.setText(_translate("libraryMainWindow", "ISBN"))
        self.authorLabel.setText(_translate("libraryMainWindow", "Author"))
        self.categoryLabel.setText(_translate("libraryMainWindow", "Category"))
        self.titleLabel.setText(_translate("libraryMainWindow", "Title"))
        self.bookSearchButton.setText(_translate("libraryMainWindow", "Search"))
        self.bookDeleteButton.setText(_translate("libraryMainWindow", "Delete"))
        self.bookUpdateButton.setText(_translate("libraryMainWindow", "Update"))
        self.bookCreateButton.setText(_translate("libraryMainWindow", "Create"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bookTab),
                                  _translate("libraryMainWindow", "Manipulate Books"))
        self.usernameLabel.setText(_translate("libraryMainWindow", "Username"))
        self.idLabel.setText(_translate("libraryMainWindow", "User ID"))
        self.userSearchButton.setText(_translate("libraryMainWindow", "Search"))
        self.userUpdateButton.setText(_translate("libraryMainWindow", "Update"))
        self.userDeleteButton.setText(_translate("libraryMainWindow", "Delete"))
        self.userCreateButton.setText(_translate("libraryMainWindow", "Create"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.userTab),
                                  _translate("libraryMainWindow", "Manipulate Users"))
        self.logoutButton.setText(_translate("libraryMainWindow", "Logout"))
