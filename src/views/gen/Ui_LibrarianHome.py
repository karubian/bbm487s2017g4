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
        libraryMainWindow.resize(1164, 836)
        libraryMainWindow.setStyleSheet("QFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(libraryMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.librarianMainFrame = QtWidgets.QFrame(self.centralwidget)
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
        self.greetingLabel.setGeometry(QtCore.QRect(30, 50, 611, 81))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.greetingLabel.setFont(font)
        self.greetingLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 255, 222);\n"
"font-size:50px;\n"
"}\n"
"\n"
"")
        self.greetingLabel.setWordWrap(False)
        self.greetingLabel.setObjectName("greetingLabel")
        self.dateLabel = QtWidgets.QLabel(self.librarianMainFrame)
        self.dateLabel.setGeometry(QtCore.QRect(30, 10, 161, 41))
        self.dateLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 255, 222);\n"
"font-size:20px;\n"
"}")
        self.dateLabel.setObjectName("dateLabel")
        self.tabWidget = QtWidgets.QTabWidget(self.librarianMainFrame)
        self.tabWidget.setGeometry(QtCore.QRect(20, 140, 1111, 641))
        self.tabWidget.setStyleSheet("QWidget {\n"
"border: 2px solid gray;\n"
"border-radius: 0px;\n"
"background: rgb(233, 255, 254);\n"
"font-size:30px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.bookTab = QtWidgets.QWidget()
        self.bookTab.setObjectName("bookTab")
        self.bookSearchButton = QtWidgets.QPushButton(self.bookTab)
        self.bookSearchButton.setGeometry(QtCore.QRect(810, 120, 241, 71))
        self.bookSearchButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.bookSearchButton.setObjectName("bookSearchButton")
        self.bookDeleteButton = QtWidgets.QPushButton(self.bookTab)
        self.bookDeleteButton.setGeometry(QtCore.QRect(810, 350, 241, 71))
        self.bookDeleteButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.bookDeleteButton.setObjectName("bookDeleteButton")
        self.bookUpdateButton = QtWidgets.QPushButton(self.bookTab)
        self.bookUpdateButton.setGeometry(QtCore.QRect(810, 440, 241, 81))
        self.bookUpdateButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.bookUpdateButton.setObjectName("bookUpdateButton")
        self.bookCreateButton = QtWidgets.QPushButton(self.bookTab)
        self.bookCreateButton.setGeometry(QtCore.QRect(810, 260, 241, 71))
        self.bookCreateButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.bookCreateButton.setObjectName("bookCreateButton")
        self.titleLabel = QtWidgets.QLabel(self.bookTab)
        self.titleLabel.setGeometry(QtCore.QRect(40, 50, 77, 42))
        self.titleLabel.setStyleSheet("QLabel {\n"
"background-color:white;\n"
"}")
        self.titleLabel.setObjectName("titleLabel")
        self.titleLineEdit = QtWidgets.QLineEdit(self.bookTab)
        self.titleLineEdit.setGeometry(QtCore.QRect(190, 50, 591, 42))
        self.titleLineEdit.setStyleSheet("QLineEdit {\n"
"background-color:white;\n"
"}")
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.authorLabel = QtWidgets.QLabel(self.bookTab)
        self.authorLabel.setGeometry(QtCore.QRect(40, 100, 108, 42))
        self.authorLabel.setStyleSheet("QLabel {\n"
"background-color:white;\n"
"}")
        self.authorLabel.setObjectName("authorLabel")
        self.authorLineEdit = QtWidgets.QLineEdit(self.bookTab)
        self.authorLineEdit.setGeometry(QtCore.QRect(190, 100, 591, 42))
        self.authorLineEdit.setStyleSheet("QLineEdit {\n"
"background-color:white;\n"
"}")
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.bookTableWidget = QtWidgets.QTableWidget(self.bookTab)
        self.bookTableWidget.setGeometry(QtCore.QRect(30, 230, 751, 291))
        self.bookTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bookTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.bookTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.bookTableWidget.setDragDropOverwriteMode(False)
        self.bookTableWidget.setAlternatingRowColors(False)
        self.bookTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.bookTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.bookTableWidget.setShowGrid(True)
        self.bookTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.bookTableWidget.setRowCount(0)
        self.bookTableWidget.setColumnCount(0)
        self.bookTableWidget.setObjectName("bookTableWidget")
        self.bookTableWidget.horizontalHeader().setVisible(True)
        self.bookTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.bookTableWidget.horizontalHeader().setDefaultSectionSize(253)
        self.bookTableWidget.horizontalHeader().setStretchLastSection(False)
        self.bookTableWidget.verticalHeader().setVisible(False)
        self.bookTableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.bookTableWidget.verticalHeader().setStretchLastSection(False)
        self.bookResetButton = QtWidgets.QPushButton(self.bookTab)
        self.bookResetButton.setGeometry(QtCore.QRect(810, 40, 241, 71))
        self.bookResetButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.bookResetButton.setObjectName("bookResetButton")
        self.yearLineEdit = QtWidgets.QLineEdit(self.bookTab)
        self.yearLineEdit.setGeometry(QtCore.QRect(190, 150, 591, 42))
        self.yearLineEdit.setStyleSheet("QLineEdit {\n"
"background-color:white;\n"
"}")
        self.yearLineEdit.setObjectName("yearLineEdit")
        self.yearLabel = QtWidgets.QLabel(self.bookTab)
        self.yearLabel.setGeometry(QtCore.QRect(40, 150, 108, 42))
        self.yearLabel.setStyleSheet("QLabel {\n"
"background-color:white;\n"
"}")
        self.yearLabel.setObjectName("yearLabel")
        self.tabWidget.addTab(self.bookTab, "")
        self.userTab = QtWidgets.QWidget()
        self.userTab.setObjectName("userTab")
        self.userSearchButton = QtWidgets.QPushButton(self.userTab)
        self.userSearchButton.setGeometry(QtCore.QRect(810, 120, 241, 71))
        self.userSearchButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.userSearchButton.setObjectName("userSearchButton")
        self.userUpdateButton = QtWidgets.QPushButton(self.userTab)
        self.userUpdateButton.setGeometry(QtCore.QRect(810, 440, 241, 81))
        self.userUpdateButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.userUpdateButton.setObjectName("userUpdateButton")
        self.userDeleteButton = QtWidgets.QPushButton(self.userTab)
        self.userDeleteButton.setGeometry(QtCore.QRect(810, 350, 241, 71))
        self.userDeleteButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.userDeleteButton.setObjectName("userDeleteButton")
        self.userCreateButton = QtWidgets.QPushButton(self.userTab)
        self.userCreateButton.setGeometry(QtCore.QRect(810, 260, 241, 71))
        self.userCreateButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.userCreateButton.setObjectName("userCreateButton")
        self.usernameLineEdit = QtWidgets.QLineEdit(self.userTab)
        self.usernameLineEdit.setGeometry(QtCore.QRect(200, 50, 581, 42))
        self.usernameLineEdit.setStyleSheet("QLineEdit {\n"
"background-color:white;\n"
"}")
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.nameLineEdit = QtWidgets.QLineEdit(self.userTab)
        self.nameLineEdit.setGeometry(QtCore.QRect(200, 100, 581, 42))
        self.nameLineEdit.setStyleSheet("QLineEdit {\n"
"background-color:white;\n"
"}")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.usernameLabel = QtWidgets.QLabel(self.userTab)
        self.usernameLabel.setGeometry(QtCore.QRect(30, 50, 153, 40))
        self.usernameLabel.setStyleSheet("QLabel {\n"
"background-color:white;\n"
"}")
        self.usernameLabel.setObjectName("usernameLabel")
        self.nameLabel = QtWidgets.QLabel(self.userTab)
        self.nameLabel.setGeometry(QtCore.QRect(30, 100, 119, 40))
        self.nameLabel.setStyleSheet("QLabel {\n"
"background-color:white;\n"
"}")
        self.nameLabel.setObjectName("nameLabel")
        self.surnameLabel = QtWidgets.QLabel(self.userTab)
        self.surnameLabel.setGeometry(QtCore.QRect(30, 150, 141, 40))
        self.surnameLabel.setStyleSheet("QLabel {\n"
"background-color:white;\n"
"}")
        self.surnameLabel.setObjectName("surnameLabel")
        self.surnameLineEdit = QtWidgets.QLineEdit(self.userTab)
        self.surnameLineEdit.setGeometry(QtCore.QRect(200, 150, 581, 42))
        self.surnameLineEdit.setStyleSheet("QLineEdit {\n"
"background-color:white;\n"
"}")
        self.surnameLineEdit.setObjectName("surnameLineEdit")
        self.userTableWidget = QtWidgets.QTableWidget(self.userTab)
        self.userTableWidget.setGeometry(QtCore.QRect(30, 230, 751, 291))
        self.userTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.userTableWidget.setAlternatingRowColors(False)
        self.userTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.userTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.userTableWidget.setShowGrid(True)
        self.userTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.userTableWidget.setRowCount(0)
        self.userTableWidget.setColumnCount(0)
        self.userTableWidget.setObjectName("userTableWidget")
        self.userTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.userTableWidget.horizontalHeader().setDefaultSectionSize(238)
        self.userTableWidget.horizontalHeader().setStretchLastSection(True)
        self.userTableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.userTableWidget.verticalHeader().setStretchLastSection(False)
        self.userResetButton = QtWidgets.QPushButton(self.userTab)
        self.userResetButton.setGeometry(QtCore.QRect(810, 40, 241, 71))
        self.userResetButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.userResetButton.setObjectName("userResetButton")
        self.tabWidget.addTab(self.userTab, "")
        self.logoutButton = QtWidgets.QPushButton(self.librarianMainFrame)
        self.logoutButton.setGeometry(QtCore.QRect(830, 40, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.logoutButton.setFont(font)
        self.logoutButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.logoutButton.setObjectName("logoutButton")
        self.label_2 = QtWidgets.QLabel(self.librarianMainFrame)
        self.label_2.setGeometry(QtCore.QRect(840, 50, 71, 61))
        self.label_2.setStyleSheet("QLabel {\n"
"border:none;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"}")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../project/resources/logout.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.librarianMainFrame, 0, 0, 1, 1)
        libraryMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(libraryMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(libraryMainWindow)

    def retranslateUi(self, libraryMainWindow):
        _translate = QtCore.QCoreApplication.translate
        libraryMainWindow.setWindowTitle(_translate("libraryMainWindow", "Home - Librarian"))
        self.librarianMainFrame.setWhatsThis(_translate("libraryMainWindow", "<html><head/><body><p>BUrak</p><p><br/></p></body></html>"))
        self.greetingLabel.setText(_translate("libraryMainWindow", "Welcome back, John Doe"))
        self.dateLabel.setText(_translate("libraryMainWindow", "10.05.2017"))
        self.bookSearchButton.setText(_translate("libraryMainWindow", "Search"))
        self.bookDeleteButton.setText(_translate("libraryMainWindow", "Delete"))
        self.bookUpdateButton.setText(_translate("libraryMainWindow", "Update"))
        self.bookCreateButton.setText(_translate("libraryMainWindow", "Create"))
        self.titleLabel.setText(_translate("libraryMainWindow", "Title"))
        self.authorLabel.setText(_translate("libraryMainWindow", "Author"))
        self.bookTableWidget.setSortingEnabled(True)
        self.bookResetButton.setText(_translate("libraryMainWindow", "Reset"))
        self.yearLabel.setText(_translate("libraryMainWindow", "Year"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bookTab), _translate("libraryMainWindow", "Manipulate Books"))
        self.userSearchButton.setText(_translate("libraryMainWindow", "Search"))
        self.userUpdateButton.setText(_translate("libraryMainWindow", "Update"))
        self.userDeleteButton.setText(_translate("libraryMainWindow", "Delete"))
        self.userCreateButton.setText(_translate("libraryMainWindow", "Create"))
        self.usernameLabel.setText(_translate("libraryMainWindow", "Username"))
        self.nameLabel.setText(_translate("libraryMainWindow", "Name"))
        self.surnameLabel.setText(_translate("libraryMainWindow", "Surname"))
        self.userTableWidget.setSortingEnabled(True)
        self.userResetButton.setText(_translate("libraryMainWindow", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.userTab), _translate("libraryMainWindow", "Manipulate Users"))
        self.logoutButton.setText(_translate("libraryMainWindow", "Logout"))

