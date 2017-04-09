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
        memberMainWindow.resize(726, 507)
        memberMainWindow.setStyleSheet("QFrame {\n"
                                       "border: 3px solid gray;\n"
                                       "border-radius: 40px;\n"
                                       "background: white;\n"
                                       "}")
        self.centralwidget = QtWidgets.QWidget(memberMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.memberMainFrame = QtWidgets.QFrame(self.centralwidget)
        self.memberMainFrame.setGeometry(QtCore.QRect(0, 0, 721, 511))
        self.memberMainFrame.setStyleSheet("QFrame {\n"
                                           "border: 3px solid gray;\n"
                                           "border-radius: 40px;\n"
                                           "background: rgb(255, 255, 222);\n"
                                           "}")
        self.memberMainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.memberMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.memberMainFrame.setObjectName("memberMainFrame")
        self.greetingLabel = QtWidgets.QLabel(self.memberMainFrame)
        self.greetingLabel.setGeometry(QtCore.QRect(30, 10, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.greetingLabel.setFont(font)
        self.greetingLabel.setStyleSheet("QLabel {\n"
                                         "border: 3px solid rgb(255, 255, 222);\n"
                                         "}\n"
                                         "")
        self.greetingLabel.setWordWrap(False)
        self.greetingLabel.setObjectName("greetingLabel")
        self.dateLabel = QtWidgets.QLabel(self.memberMainFrame)
        self.dateLabel.setGeometry(QtCore.QRect(30, 10, 81, 20))
        self.dateLabel.setStyleSheet("QLabel {\n"
                                     "border: 3px solid rgb(255, 255, 222);\n"
                                     "}")
        self.dateLabel.setObjectName("dateLabel")
        self.tabWidget = QtWidgets.QTabWidget(self.memberMainFrame)
        self.tabWidget.setGeometry(QtCore.QRect(20, 110, 681, 361))
        self.tabWidget.setStyleSheet("QWidget {\n"
                                     "border: 2px solid gray;\n"
                                     "border-radius: 0px;\n"
                                     "background: rgb(233, 255, 254);\n"
                                     "}")
        self.tabWidget.setObjectName("tabWidget")
        self.homeTab = QtWidgets.QWidget()
        self.homeTab.setObjectName("homeTab")
        self.avatarSection = QtWidgets.QGraphicsView(self.homeTab)
        self.avatarSection.setGeometry(QtCore.QRect(500, 30, 131, 151))
        self.avatarSection.setStyleSheet("")
        self.avatarSection.setObjectName("avatarSection")
        self.totalBooksLabel = QtWidgets.QLabel(self.homeTab)
        self.totalBooksLabel.setGeometry(QtCore.QRect(40, 20, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.totalBooksLabel.setFont(font)
        self.totalBooksLabel.setStyleSheet("QLabel {\n"
                                           "border: 3px solid rgb(233, 255, 254);\n"
                                           "}")
        self.totalBooksLabel.setObjectName("totalBooksLabel")
        self.lastBookLabel = QtWidgets.QLabel(self.homeTab)
        self.lastBookLabel.setGeometry(QtCore.QRect(40, 60, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lastBookLabel.setFont(font)
        self.lastBookLabel.setStyleSheet("QLabel {\n"
                                         "border: 3px solid rgb(233, 255, 254);\n"
                                         "}")
        self.lastBookLabel.setObjectName("lastBookLabel")
        self.fineLabel = QtWidgets.QLabel(self.homeTab)
        self.fineLabel.setGeometry(QtCore.QRect(40, 100, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fineLabel.setFont(font)
        self.fineLabel.setStyleSheet("QLabel {\n"
                                     "border: 3px solid rgb(233, 255, 254);\n"
                                     "}")
        self.fineLabel.setObjectName("fineLabel")
        self.payFineButton = QtWidgets.QPushButton(self.homeTab)
        self.payFineButton.setGeometry(QtCore.QRect(40, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.payFineButton.setFont(font)
        self.payFineButton.setStyleSheet("QPushButton {\n"
                                         "color: white;\n"
                                         "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                         "font-size: 20px;\n"
                                         "}")
        self.payFineButton.setObjectName("payFineButton")
        self.tabWidget.addTab(self.homeTab, "")
        self.searchBooksTab = QtWidgets.QWidget()
        self.searchBooksTab.setObjectName("searchBooksTab")
        self.formLayoutWidget = QtWidgets.QWidget(self.searchBooksTab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 20, 391, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.searchBookForm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.searchBookForm.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.searchBookForm.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.searchBookForm.setFormAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.searchBookForm.setContentsMargins(0, 0, 0, 0)
        self.searchBookForm.setObjectName("searchBookForm")
        self.titleLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.titleLineEdit.setStyleSheet("QLineEdit {\n"
                                         "background-color:white;\n"
                                         "}")
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.searchBookForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleLineEdit)
        self.iSBNLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.iSBNLabel.setStyleSheet("QLabel {\n"
                                     "background-color:white;\n"
                                     "}")
        self.iSBNLabel.setObjectName("iSBNLabel")
        self.searchBookForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.iSBNLabel)
        self.iSBNLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.iSBNLineEdit.setStyleSheet("QLineEdit {\n"
                                        "background-color:white;\n"
                                        "}")
        self.iSBNLineEdit.setObjectName("iSBNLineEdit")
        self.searchBookForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.iSBNLineEdit)
        self.authorLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.authorLabel.setStyleSheet("QLabel {\n"
                                       "background-color:white;\n"
                                       "}")
        self.authorLabel.setObjectName("authorLabel")
        self.searchBookForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.authorLabel)
        self.authorLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.authorLineEdit.setStyleSheet("QLineEdit {\n"
                                          "background-color:white;\n"
                                          "}")
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.searchBookForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.authorLineEdit)
        self.categoryLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.categoryLabel.setStyleSheet("QLabel {\n"
                                         "background-color:white;\n"
                                         "}")
        self.categoryLabel.setObjectName("categoryLabel")
        self.searchBookForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
        self.titleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.titleLabel.setStyleSheet("QLabel {\n"
                                      "background-color:white;\n"
                                      "}")
        self.titleLabel.setObjectName("titleLabel")
        self.searchBookForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.categoryLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.categoryLineEdit.setStyleSheet("QLineEdit {\n"
                                            "background-color:white;\n"
                                            "}")
        self.categoryLineEdit.setObjectName("categoryLineEdit")
        self.searchBookForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.categoryLineEdit)
        self.bookSearchButton = QtWidgets.QPushButton(self.searchBooksTab)
        self.bookSearchButton.setGeometry(QtCore.QRect(450, 20, 141, 31))
        self.bookSearchButton.setStyleSheet("QPushButton {\n"
                                            "color: white;\n"
                                            "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                            "font-size: 20px;\n"
                                            "}")
        self.bookSearchButton.setObjectName("bookSearchButton")
        self.waitingListButton = QtWidgets.QPushButton(self.searchBooksTab)
        self.waitingListButton.setGeometry(QtCore.QRect(450, 100, 141, 31))
        self.waitingListButton.setStyleSheet("QPushButton {\n"
                                             "color: white;\n"
                                             "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                             "font-size: 15px;\n"
                                             "}")
        self.waitingListButton.setObjectName("waitingListButton")
        self.checkoutButton = QtWidgets.QPushButton(self.searchBooksTab)
        self.checkoutButton.setGeometry(QtCore.QRect(450, 60, 141, 31))
        self.checkoutButton.setStyleSheet("QPushButton {\n"
                                          "color: white;\n"
                                          "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                          "font-size: 20px;\n"
                                          "}")
        self.checkoutButton.setObjectName("checkoutButton")
        self.searchScrollArea = QtWidgets.QScrollArea(self.searchBooksTab)
        self.searchScrollArea.setGeometry(QtCore.QRect(50, 170, 531, 131))
        self.searchScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.searchScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.searchScrollArea.setWidgetResizable(True)
        self.searchScrollArea.setObjectName("searchScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 506, 127))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.searchScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.searchBooksTab, "")
        self.viewBooksTab = QtWidgets.QWidget()
        self.viewBooksTab.setObjectName("viewBooksTab")
        self.pushButton_4 = QtWidgets.QPushButton(self.viewBooksTab)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 200, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "color: white;\n"
                                        "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                        "font-size: 20px;\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.viewScrollArea = QtWidgets.QScrollArea(self.viewBooksTab)
        self.viewScrollArea.setGeometry(QtCore.QRect(30, 40, 591, 141))
        self.viewScrollArea.setWidgetResizable(True)
        self.viewScrollArea.setObjectName("viewScrollArea")
        self.viewScrollAreaWidgetContents = QtWidgets.QWidget()
        self.viewScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 587, 137))
        self.viewScrollAreaWidgetContents.setObjectName("viewScrollAreaWidgetContents")
        self.viewScrollArea.setWidget(self.viewScrollAreaWidgetContents)
        self.tabWidget.addTab(self.viewBooksTab, "")
        self.logoutButton = QtWidgets.QPushButton(self.memberMainFrame)
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
        memberMainWindow.setCentralWidget(self.centralwidget)
        self.actionBurak = QtWidgets.QAction(memberMainWindow)
        self.actionBurak.setObjectName("actionBurak")

        self.retranslateUi(memberMainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(memberMainWindow)

    def retranslateUi(self, memberMainWindow):
        _translate = QtCore.QCoreApplication.translate
        memberMainWindow.setWindowTitle(_translate("memberMainWindow", "Home - Member"))
        memberMainWindow.setWhatsThis(
            _translate("memberMainWindow", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.memberMainFrame.setWhatsThis(
            _translate("memberMainWindow", "<html><head/><body><p>BUrak</p><p><br/></p></body></html>"))
        self.greetingLabel.setText(_translate("memberMainWindow", "Welcome back, John Doe"))
        self.dateLabel.setText(_translate("memberMainWindow", "10.05.2017"))
        self.totalBooksLabel.setText(_translate("memberMainWindow", "Total Loaned Books : 5"))
        self.lastBookLabel.setText(_translate("memberMainWindow", "Last Loaned Book : Sapiens"))
        self.fineLabel.setText(_translate("memberMainWindow", "Current Fine Amount : $23"))
        self.payFineButton.setText(_translate("memberMainWindow", "Pay Fine"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), _translate("memberMainWindow", "Home"))
        self.iSBNLabel.setText(_translate("memberMainWindow", "ISBN"))
        self.authorLabel.setText(_translate("memberMainWindow", "Author"))
        self.categoryLabel.setText(_translate("memberMainWindow", "Category"))
        self.titleLabel.setText(_translate("memberMainWindow", "Title"))
        self.bookSearchButton.setText(_translate("memberMainWindow", "Search"))
        self.waitingListButton.setText(_translate("memberMainWindow", "Add to waiting list"))
        self.checkoutButton.setText(_translate("memberMainWindow", "Checkout"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchBooksTab),
                                  _translate("memberMainWindow", "Search For Books"))
        self.pushButton_4.setText(_translate("memberMainWindow", "Return selected book"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.viewBooksTab),
                                  _translate("memberMainWindow", "View My Books"))
        self.logoutButton.setText(_translate("memberMainWindow", "Logout"))
        self.actionBurak.setText(_translate("memberMainWindow", "Burak"))
