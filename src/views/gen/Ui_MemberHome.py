# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registered_home.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_memberMainWindow(object):
    def setupUi(self, memberMainWindow):
        memberMainWindow.setObjectName("memberMainWindow")
        memberMainWindow.setWindowModality(QtCore.Qt.NonModal)
        memberMainWindow.setEnabled(True)
        memberMainWindow.resize(1155, 839)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(memberMainWindow.sizePolicy().hasHeightForWidth())
        memberMainWindow.setSizePolicy(sizePolicy)
        memberMainWindow.setMinimumSize(QtCore.QSize(1155, 839))
        memberMainWindow.setMaximumSize(QtCore.QSize(1155, 839))
        memberMainWindow.setAutoFillBackground(False)
        memberMainWindow.setStyleSheet("QFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(memberMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.memberMainFrame = QtWidgets.QFrame(self.centralwidget)
        self.memberMainFrame.setGeometry(QtCore.QRect(0, 0, 1151, 831))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.memberMainFrame.sizePolicy().hasHeightForWidth())
        self.memberMainFrame.setSizePolicy(sizePolicy)
        self.memberMainFrame.setMaximumSize(QtCore.QSize(1151, 831))
        self.memberMainFrame.setStyleSheet("QFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: rgb(255, 255, 222);\n"
"}")
        self.memberMainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.memberMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.memberMainFrame.setObjectName("memberMainFrame")
        self.greetingLabel = QtWidgets.QLabel(self.memberMainFrame)
        self.greetingLabel.setGeometry(QtCore.QRect(30, 50, 671, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.greetingLabel.setFont(font)
        self.greetingLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 255, 222);\n"
"font-size:50px;\n"
"}\n"
"")
        self.greetingLabel.setWordWrap(False)
        self.greetingLabel.setObjectName("greetingLabel")
        self.dateLabel = QtWidgets.QLabel(self.memberMainFrame)
        self.dateLabel.setGeometry(QtCore.QRect(30, 10, 141, 41))
        self.dateLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 255, 222);\n"
"font-size:20px;\n"
"}")
        self.dateLabel.setObjectName("dateLabel")
        self.tabWidget = QtWidgets.QTabWidget(self.memberMainFrame)
        self.tabWidget.setGeometry(QtCore.QRect(10, 180, 1121, 631))
        self.tabWidget.setStyleSheet("QWidget {\n"
"border: 2px solid gray;\n"
"border-radius: 0px;\n"
"background: rgb(233, 255, 254);\n"
"font-size:30px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.homeTab = QtWidgets.QWidget()
        self.homeTab.setObjectName("homeTab")
        self.totalBooksLabel = QtWidgets.QLabel(self.homeTab)
        self.totalBooksLabel.setGeometry(QtCore.QRect(390, 460, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.totalBooksLabel.setFont(font)
        self.totalBooksLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(233, 255, 254);\n"
"}")
        self.totalBooksLabel.setObjectName("totalBooksLabel")
        self.lastBookLabel = QtWidgets.QLabel(self.homeTab)
        self.lastBookLabel.setGeometry(QtCore.QRect(390, 330, 691, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lastBookLabel.setFont(font)
        self.lastBookLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(233, 255, 254);\n"
"}")
        self.lastBookLabel.setObjectName("lastBookLabel")
        self.fineLabel = QtWidgets.QLabel(self.homeTab)
        self.fineLabel.setGeometry(QtCore.QRect(390, 390, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.fineLabel.setFont(font)
        self.fineLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(233, 255, 254);\n"
"}")
        self.fineLabel.setObjectName("fineLabel")
        self.payFineButton = QtWidgets.QPushButton(self.homeTab)
        self.payFineButton.setGeometry(QtCore.QRect(40, 450, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.payFineButton.setFont(font)
        self.payFineButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"border-radius:10px;\n"
"}")
        self.payFineButton.setObjectName("payFineButton")
        self.avatarLabel = QtWidgets.QLabel(self.homeTab)
        self.avatarLabel.setGeometry(QtCore.QRect(830, 60, 251, 251))
        self.avatarLabel.setText("")
        self.avatarLabel.setPixmap(QtGui.QPixmap("../project/resources/user.png"))
        self.avatarLabel.setScaledContents(True)
        self.avatarLabel.setObjectName("avatarLabel")
        self.waitingListWidget = QtWidgets.QTableWidget(self.homeTab)
        self.waitingListWidget.setGeometry(QtCore.QRect(40, 60, 741, 251))
        self.waitingListWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.waitingListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.waitingListWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.waitingListWidget.setAutoScroll(False)
        self.waitingListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.waitingListWidget.setAlternatingRowColors(False)
        self.waitingListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.waitingListWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.waitingListWidget.setShowGrid(True)
        self.waitingListWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.waitingListWidget.setRowCount(0)
        self.waitingListWidget.setColumnCount(0)
        self.waitingListWidget.setObjectName("waitingListWidget")
        self.waitingListWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.waitingListWidget.horizontalHeader().setDefaultSectionSize(247)
        self.waitingListWidget.horizontalHeader().setStretchLastSection(True)
        self.waitingListWidget.verticalHeader().setVisible(False)
        self.waitingListWidget.verticalHeader().setCascadingSectionResizes(True)
        self.waitingListWidget.verticalHeader().setStretchLastSection(False)
        self.waitingListLabel = QtWidgets.QLabel(self.homeTab)
        self.waitingListLabel.setGeometry(QtCore.QRect(40, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.waitingListLabel.setFont(font)
        self.waitingListLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(233, 255, 254);\n"
"}")
        self.waitingListLabel.setObjectName("waitingListLabel")
        self.cancelSelected = QtWidgets.QPushButton(self.homeTab)
        self.cancelSelected.setGeometry(QtCore.QRect(40, 330, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.cancelSelected.setFont(font)
        self.cancelSelected.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"border-radius:10px;\n"
"}")
        self.cancelSelected.setObjectName("cancelSelected")
        self.tabWidget.addTab(self.homeTab, "")
        self.searchBooksTab = QtWidgets.QWidget()
        self.searchBooksTab.setObjectName("searchBooksTab")
        self.authorLineEdit = QtWidgets.QLineEdit(self.searchBooksTab)
        self.authorLineEdit.setGeometry(QtCore.QRect(210, 160, 591, 42))
        self.authorLineEdit.setStyleSheet("QLineEdit {\n"
"background-color:white;\n"
"}")
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.authorLabel = QtWidgets.QLabel(self.searchBooksTab)
        self.authorLabel.setGeometry(QtCore.QRect(60, 160, 108, 42))
        self.authorLabel.setStyleSheet("QLabel {\n"
"background-color:white;\n"
"}")
        self.authorLabel.setObjectName("authorLabel")
        self.yearLineEdit = QtWidgets.QLineEdit(self.searchBooksTab)
        self.yearLineEdit.setGeometry(QtCore.QRect(210, 210, 591, 42))
        self.yearLineEdit.setStyleSheet("QLineEdit {\n"
"background-color:white;\n"
"}")
        self.yearLineEdit.setObjectName("yearLineEdit")
        self.yearLabel = QtWidgets.QLabel(self.searchBooksTab)
        self.yearLabel.setGeometry(QtCore.QRect(60, 210, 108, 42))
        self.yearLabel.setStyleSheet("QLabel {\n"
"background-color:white;\n"
"}")
        self.yearLabel.setObjectName("yearLabel")
        self.titleLabel = QtWidgets.QLabel(self.searchBooksTab)
        self.titleLabel.setGeometry(QtCore.QRect(60, 110, 77, 42))
        self.titleLabel.setStyleSheet("QLabel {\n"
"background-color:white;\n"
"}")
        self.titleLabel.setObjectName("titleLabel")
        self.titleLineEdit = QtWidgets.QLineEdit(self.searchBooksTab)
        self.titleLineEdit.setGeometry(QtCore.QRect(210, 110, 591, 42))
        self.titleLineEdit.setStyleSheet("QLineEdit {\n"
"background-color:white;\n"
"}")
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.searchButton = QtWidgets.QPushButton(self.searchBooksTab)
        self.searchButton.setGeometry(QtCore.QRect(580, 20, 241, 71))
        self.searchButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"border-radius:10px;\n"
"}")
        self.searchButton.setObjectName("searchButton")
        self.waitingListButton = QtWidgets.QPushButton(self.searchBooksTab)
        self.waitingListButton.setGeometry(QtCore.QRect(60, 20, 241, 71))
        self.waitingListButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 20px;\n"
"border-radius:10px;\n"
"}")
        self.waitingListButton.setObjectName("waitingListButton")
        self.checkoutButton = QtWidgets.QPushButton(self.searchBooksTab)
        self.checkoutButton.setGeometry(QtCore.QRect(320, 20, 241, 71))
        self.checkoutButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"border-radius:10px;\n"
"}")
        self.checkoutButton.setObjectName("checkoutButton")
        self.searchBookWidget = QtWidgets.QTableWidget(self.searchBooksTab)
        self.searchBookWidget.setGeometry(QtCore.QRect(60, 270, 1021, 271))
        self.searchBookWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchBookWidget.setAutoScroll(False)
        self.searchBookWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.searchBookWidget.setAlternatingRowColors(False)
        self.searchBookWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.searchBookWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.searchBookWidget.setShowGrid(True)
        self.searchBookWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.searchBookWidget.setRowCount(1)
        self.searchBookWidget.setColumnCount(6)
        self.searchBookWidget.setObjectName("searchBookWidget")
        item = QtWidgets.QTableWidgetItem()
        self.searchBookWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchBookWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.searchBookWidget.setHorizontalHeaderItem(2, item)
        self.searchBookWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.searchBookWidget.horizontalHeader().setDefaultSectionSize(385)
        self.searchBookWidget.horizontalHeader().setStretchLastSection(True)
        self.searchBookWidget.verticalHeader().setCascadingSectionResizes(True)
        self.searchBookWidget.verticalHeader().setStretchLastSection(False)
        self.resetButton = QtWidgets.QPushButton(self.searchBooksTab)
        self.resetButton.setGeometry(QtCore.QRect(840, 20, 241, 71))
        self.resetButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"border-radius:10px;\n"
"}")
        self.resetButton.setObjectName("resetButton")
        self.tabWidget.addTab(self.searchBooksTab, "")
        self.viewBooksTab = QtWidgets.QWidget()
        self.viewBooksTab.setObjectName("viewBooksTab")
        self.returnBookButton = QtWidgets.QPushButton(self.viewBooksTab)
        self.returnBookButton.setGeometry(QtCore.QRect(30, 430, 501, 111))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.returnBookButton.setFont(font)
        self.returnBookButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"border-radius:10px;\n"
"}")
        self.returnBookButton.setObjectName("returnBookButton")
        self.viewBookWidget = QtWidgets.QTableWidget(self.viewBooksTab)
        self.viewBookWidget.setGeometry(QtCore.QRect(30, 40, 991, 361))
        self.viewBookWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.viewBookWidget.setAutoScroll(False)
        self.viewBookWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.viewBookWidget.setAlternatingRowColors(False)
        self.viewBookWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.viewBookWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.viewBookWidget.setShowGrid(True)
        self.viewBookWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.viewBookWidget.setRowCount(0)
        self.viewBookWidget.setColumnCount(0)
        self.viewBookWidget.setObjectName("viewBookWidget")
        self.viewBookWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.viewBookWidget.horizontalHeader().setDefaultSectionSize(340)
        self.viewBookWidget.horizontalHeader().setStretchLastSection(True)
        self.viewBookWidget.verticalHeader().setVisible(False)
        self.viewBookWidget.verticalHeader().setCascadingSectionResizes(True)
        self.viewBookWidget.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.viewBooksTab, "")
        self.logoutButton = QtWidgets.QPushButton(self.memberMainFrame)
        self.logoutButton.setGeometry(QtCore.QRect(840, 50, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.logoutButton.setFont(font)
        self.logoutButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"border-radius:10px;\n"
"}")
        self.logoutButton.setObjectName("logoutButton")
        self.logoutPng = QtWidgets.QLabel(self.memberMainFrame)
        self.logoutPng.setGeometry(QtCore.QRect(850, 60, 81, 71))
        self.logoutPng.setStyleSheet("QLabel {\n"
"border:none;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"}")
        self.logoutPng.setText("")
        self.logoutPng.setPixmap(QtGui.QPixmap("../project/resources/logout.png"))
        self.logoutPng.setScaledContents(True)
        self.logoutPng.setObjectName("logoutPng")
        memberMainWindow.setCentralWidget(self.centralwidget)
        self.actionBurak = QtWidgets.QAction(memberMainWindow)
        self.actionBurak.setObjectName("actionBurak")

        self.retranslateUi(memberMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(memberMainWindow)

    def retranslateUi(self, memberMainWindow):
        _translate = QtCore.QCoreApplication.translate
        memberMainWindow.setWindowTitle(_translate("memberMainWindow", "Home - Member"))
        memberMainWindow.setWhatsThis(_translate("memberMainWindow", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.memberMainFrame.setWhatsThis(_translate("memberMainWindow", "<html><head/><body><p>BUrak</p><p><br/></p></body></html>"))
        self.greetingLabel.setText(_translate("memberMainWindow", "Welcome back, John Doe"))
        self.dateLabel.setText(_translate("memberMainWindow", "10.05.2017"))
        self.totalBooksLabel.setText(_translate("memberMainWindow", "Total Loaned Books : 5"))
        self.lastBookLabel.setText(_translate("memberMainWindow", "Last Loaned Book : Sapiens"))
        self.fineLabel.setText(_translate("memberMainWindow", "Current Fine Amount : $23"))
        self.payFineButton.setText(_translate("memberMainWindow", "Pay Fine"))
        self.waitingListWidget.setSortingEnabled(True)
        self.waitingListLabel.setText(_translate("memberMainWindow", "My Waiting List"))
        self.cancelSelected.setText(_translate("memberMainWindow", "Cancel Selected"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), _translate("memberMainWindow", "Home"))
        self.authorLabel.setText(_translate("memberMainWindow", "Author"))
        self.yearLabel.setText(_translate("memberMainWindow", "Year"))
        self.titleLabel.setText(_translate("memberMainWindow", "Title"))
        self.searchButton.setText(_translate("memberMainWindow", "Search"))
        self.waitingListButton.setText(_translate("memberMainWindow", "Add To Waiting List"))
        self.checkoutButton.setText(_translate("memberMainWindow", "Checkout"))
        self.searchBookWidget.setSortingEnabled(True)
        item = self.searchBookWidget.horizontalHeaderItem(0)
        item.setText(_translate("memberMainWindow", "Title"))
        item = self.searchBookWidget.horizontalHeaderItem(1)
        item.setText(_translate("memberMainWindow", "Author"))
        item = self.searchBookWidget.horizontalHeaderItem(2)
        item.setText(_translate("memberMainWindow", "Published Year"))
        self.resetButton.setText(_translate("memberMainWindow", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchBooksTab), _translate("memberMainWindow", "Search For Books"))
        self.returnBookButton.setText(_translate("memberMainWindow", "Return selected book"))
        self.viewBookWidget.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.viewBooksTab), _translate("memberMainWindow", "View My Books"))
        self.logoutButton.setText(_translate("memberMainWindow", "Logout"))
        self.actionBurak.setText(_translate("memberMainWindow", "Burak"))

