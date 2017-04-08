# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MemberHome(object):
    def setupUi(self, MemberHome):
        MemberHome.setObjectName("MemberHome")
        MemberHome.resize(752, 558)
        MemberHome.setStyleSheet("QFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: white;\n"
"}")
        self.MemberHomeWidget = QtWidgets.QWidget(MemberHome)
        self.MemberHomeWidget.setObjectName("MemberHomeWidget")
        self.HomeFrame = QtWidgets.QFrame(self.MemberHomeWidget)
        self.HomeFrame.setGeometry(QtCore.QRect(20, 20, 721, 511))
        self.HomeFrame.setStyleSheet("QFrame {\n"
"color: gray;\n"
"}")
        self.HomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HomeFrame.setObjectName("HomeFrame")
        self.GreetingLabel = QtWidgets.QLabel(self.HomeFrame)
        self.GreetingLabel.setGeometry(QtCore.QRect(30, 10, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.GreetingLabel.setFont(font)
        self.GreetingLabel.setStyleSheet("QLabel {\n"
"border: 3px solid white;\n"
"}")
        self.GreetingLabel.setWordWrap(False)
        self.GreetingLabel.setObjectName("GreetingLabel")
        self.DateLabel = QtWidgets.QLabel(self.HomeFrame)
        self.DateLabel.setGeometry(QtCore.QRect(30, 10, 81, 20))
        self.DateLabel.setStyleSheet("QLabel {\n"
"border: 3px solid white;\n"
"}")
        self.DateLabel.setObjectName("DateLabel")
        self.MainTabFrame = QtWidgets.QTabWidget(self.HomeFrame)
        self.MainTabFrame.setGeometry(QtCore.QRect(20, 110, 681, 361))
        self.MainTabFrame.setStyleSheet("QWidget {\n"
"border: 2px solid gray;\n"
"border-radius: 0px;\n"
"background: white;\n"
"}")
        self.MainTabFrame.setObjectName("MainTabFrame")
        self.HomeTab = QtWidgets.QWidget()
        self.HomeTab.setObjectName("HomeTab")
        self.AvatarView = QtWidgets.QGraphicsView(self.HomeTab)
        self.AvatarView.setGeometry(QtCore.QRect(500, 30, 131, 151))
        self.AvatarView.setObjectName("AvatarView")
        self.TotalLoaned = QtWidgets.QLabel(self.HomeTab)
        self.TotalLoaned.setGeometry(QtCore.QRect(40, 20, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TotalLoaned.setFont(font)
        self.TotalLoaned.setStyleSheet("QLabel {\n"
"border: 3px solid white;\n"
"}")
        self.TotalLoaned.setObjectName("TotalLoaned")
        self.LastLoaned = QtWidgets.QLabel(self.HomeTab)
        self.LastLoaned.setGeometry(QtCore.QRect(40, 60, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LastLoaned.setFont(font)
        self.LastLoaned.setStyleSheet("QLabel {\n"
"border: 3px solid white;\n"
"}")
        self.LastLoaned.setObjectName("LastLoaned")
        self.CurrentFine = QtWidgets.QLabel(self.HomeTab)
        self.CurrentFine.setGeometry(QtCore.QRect(40, 100, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CurrentFine.setFont(font)
        self.CurrentFine.setStyleSheet("QLabel {\n"
"border: 3px solid white;\n"
"}")
        self.CurrentFine.setObjectName("CurrentFine")
        self.PayFineButton = QtWidgets.QPushButton(self.HomeTab)
        self.PayFineButton.setGeometry(QtCore.QRect(40, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.PayFineButton.setFont(font)
        self.PayFineButton.setStyleSheet("\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"border-width: 1px;\n"
"border-color: #fff;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 20px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}")
        self.PayFineButton.setObjectName("PayFineButton")
        self.MainTabFrame.addTab(self.HomeTab, "")
        self.SearchTab = QtWidgets.QWidget()
        self.SearchTab.setObjectName("SearchTab")
        self.formLayoutWidget = QtWidgets.QWidget(self.SearchTab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 20, 391, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.SearchForm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.SearchForm.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.SearchForm.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.SearchForm.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.SearchForm.setContentsMargins(0, 0, 0, 0)
        self.SearchForm.setObjectName("SearchForm")
        self.titleLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.SearchForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleLineEdit)
        self.iSBNLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.iSBNLabel.setObjectName("iSBNLabel")
        self.SearchForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.iSBNLabel)
        self.iSBNLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.iSBNLineEdit.setObjectName("iSBNLineEdit")
        self.SearchForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.iSBNLineEdit)
        self.AuthorLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.AuthorLabel.setObjectName("AuthorLabel")
        self.SearchForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.AuthorLabel)
        self.AuthorForm = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.AuthorForm.setObjectName("AuthorForm")
        self.SearchForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.AuthorForm)
        self.categoryLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.categoryLabel.setObjectName("categoryLabel")
        self.SearchForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
        self.titleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.titleLabel.setObjectName("titleLabel")
        self.SearchForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.categoryLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.categoryLineEdit.setObjectName("categoryLineEdit")
        self.SearchForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.categoryLineEdit)
        self.SearchButton = QtWidgets.QPushButton(self.SearchTab)
        self.SearchButton.setGeometry(QtCore.QRect(450, 20, 141, 31))
        self.SearchButton.setStyleSheet("\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"border-width: 1px;\n"
"border-color: #fff;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 20px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}")
        self.SearchButton.setObjectName("SearchButton")
        self.WaitingButton = QtWidgets.QPushButton(self.SearchTab)
        self.WaitingButton.setGeometry(QtCore.QRect(450, 100, 141, 31))
        self.WaitingButton.setStyleSheet("\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"border-width: 1px;\n"
"border-color: #fff;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 16px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}")
        self.WaitingButton.setObjectName("WaitingButton")
        self.CheckoutButton = QtWidgets.QPushButton(self.SearchTab)
        self.CheckoutButton.setGeometry(QtCore.QRect(450, 60, 141, 31))
        self.CheckoutButton.setStyleSheet("\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"border-width: 1px;\n"
"border-color: #fff;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 20px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}")
        self.CheckoutButton.setObjectName("CheckoutButton")
        self.scrollArea = QtWidgets.QScrollArea(self.SearchTab)
        self.scrollArea.setGeometry(QtCore.QRect(50, 170, 531, 131))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.ResultContents = QtWidgets.QWidget()
        self.ResultContents.setGeometry(QtCore.QRect(0, 0, 506, 127))
        self.ResultContents.setObjectName("ResultContents")
        self.scrollArea.setWidget(self.ResultContents)
        self.MainTabFrame.addTab(self.SearchTab, "")
        self.ViewBookTab = QtWidgets.QWidget()
        self.ViewBookTab.setObjectName("ViewBookTab")
        self.ReturnButton = QtWidgets.QPushButton(self.ViewBookTab)
        self.ReturnButton.setGeometry(QtCore.QRect(30, 200, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.ReturnButton.setFont(font)
        self.ReturnButton.setStyleSheet("\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"border-width: 1px;\n"
"border-color: #fff;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 20px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}")
        self.ReturnButton.setObjectName("ReturnButton")
        self.MyBooksScroll = QtWidgets.QScrollArea(self.ViewBookTab)
        self.MyBooksScroll.setGeometry(QtCore.QRect(30, 30, 601, 141))
        self.MyBooksScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.MyBooksScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MyBooksScroll.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.MyBooksScroll.setWidgetResizable(True)
        self.MyBooksScroll.setObjectName("MyBooksScroll")
        self.ResultWidget = QtWidgets.QWidget()
        self.ResultWidget.setGeometry(QtCore.QRect(0, 0, 576, 137))
        self.ResultWidget.setObjectName("ResultWidget")
        self.MyBooksScroll.setWidget(self.ResultWidget)
        self.MainTabFrame.addTab(self.ViewBookTab, "")
        self.LogoutButton = QtWidgets.QPushButton(self.HomeFrame)
        self.LogoutButton.setGeometry(QtCore.QRect(520, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.LogoutButton.setFont(font)
        self.LogoutButton.setStyleSheet("\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"border-width: 1px;\n"
"border-color: #fff;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 20px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}")
        self.LogoutButton.setObjectName("LogoutButton")
        MemberHome.setCentralWidget(self.MemberHomeWidget)
        self.actionBurak = QtWidgets.QAction(MemberHome)
        self.actionBurak.setObjectName("actionBurak")

        self.retranslateUi(MemberHome)
        self.MainTabFrame.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MemberHome)

    def retranslateUi(self, MemberHome):
        _translate = QtCore.QCoreApplication.translate
        MemberHome.setWindowTitle(_translate("MemberHome", "MainWindow"))
        MemberHome.setWhatsThis(_translate("MemberHome", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.HomeFrame.setWhatsThis(_translate("MemberHome", "<html><head/><body><p>BUrak</p><p><br/></p></body></html>"))
        self.GreetingLabel.setText(_translate("MemberHome", "Welcome back, John Doe"))
        self.DateLabel.setText(_translate("MemberHome", "10.05.2017"))
        self.TotalLoaned.setText(_translate("MemberHome", "Total Loaned Books : 5"))
        self.LastLoaned.setText(_translate("MemberHome", "Last Loaned Book : Sapiens"))
        self.CurrentFine.setText(_translate("MemberHome", "Current Fine Amount : $23"))
        self.PayFineButton.setText(_translate("MemberHome", "Pay Fine"))
        self.MainTabFrame.setTabText(self.MainTabFrame.indexOf(self.HomeTab), _translate("MemberHome", "Home"))
        self.iSBNLabel.setText(_translate("MemberHome", "ISBN"))
        self.AuthorLabel.setText(_translate("MemberHome", "Author"))
        self.categoryLabel.setText(_translate("MemberHome", "Category"))
        self.titleLabel.setText(_translate("MemberHome", "Title"))
        self.SearchButton.setText(_translate("MemberHome", "Search"))
        self.WaitingButton.setText(_translate("MemberHome", "Add to waiting list"))
        self.CheckoutButton.setText(_translate("MemberHome", "Checkout"))
        self.MainTabFrame.setTabText(self.MainTabFrame.indexOf(self.SearchTab), _translate("MemberHome", "Search For Books"))
        self.ReturnButton.setText(_translate("MemberHome", "Return selected book"))
        self.MainTabFrame.setTabText(self.MainTabFrame.indexOf(self.ViewBookTab), _translate("MemberHome", "View My Books"))
        self.LogoutButton.setText(_translate("MemberHome", "Logout"))
        self.actionBurak.setText(_translate("MemberHome", "Burak"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MemberHome = QtWidgets.QMainWindow()
    ui = Ui_MemberHome()
    ui.setupUi(MemberHome)
    MemberHome.show()
    sys.exit(app.exec_())

