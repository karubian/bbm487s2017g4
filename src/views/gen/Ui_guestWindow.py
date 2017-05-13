# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guestSearch.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_guestWindow(object):
    def setupUi(self, guestWindow):
        guestWindow.setObjectName("guestWindow")
        guestWindow.resize(1077, 673)
        guestWindow.setStyleSheet("QFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(guestWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.guestFrame = QtWidgets.QFrame(self.centralwidget)
        self.guestFrame.setGeometry(QtCore.QRect(0, 0, 1071, 671))
        self.guestFrame.setStyleSheet("QFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: rgb(255, 255, 222);\n"
"}")
        self.guestFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.guestFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.guestFrame.setObjectName("guestFrame")
        self.greetingLabel = QtWidgets.QLabel(self.guestFrame)
        self.greetingLabel.setGeometry(QtCore.QRect(30, 40, 381, 71))
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
        self.dateLabel = QtWidgets.QLabel(self.guestFrame)
        self.dateLabel.setGeometry(QtCore.QRect(30, 10, 101, 31))
        self.dateLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 255, 222);\n"
"font-size:15px;\n"
"}")
        self.dateLabel.setObjectName("dateLabel")
        self.guestFrame1 = QtWidgets.QFrame(self.guestFrame)
        self.guestFrame1.setGeometry(QtCore.QRect(10, 130, 1051, 531))
        self.guestFrame1.setStyleSheet("QWidget {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: rgb(255, 239, 211);\n"
"}")
        self.guestFrame1.setObjectName("guestFrame1")
        self.yearLabel = QtWidgets.QLabel(self.guestFrame1)
        self.yearLabel.setGeometry(QtCore.QRect(30, 170, 108, 42))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.yearLabel.setFont(font)
        self.yearLabel.setStyleSheet("QLabel {\n"
"background-color:white;\n"
"}")
        self.yearLabel.setObjectName("yearLabel")
        self.searchButton = QtWidgets.QPushButton(self.guestFrame1)
        self.searchButton.setGeometry(QtCore.QRect(790, 60, 241, 71))
        self.searchButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.searchButton.setObjectName("searchButton")
        self.yearLineEdit = QtWidgets.QLineEdit(self.guestFrame1)
        self.yearLineEdit.setGeometry(QtCore.QRect(180, 170, 591, 42))
        self.yearLineEdit.setStyleSheet("QLineEdit {\n"
"background-color:white;\n"
"border: 2px solid black;\n"
"}")
        self.yearLineEdit.setObjectName("yearLineEdit")
        self.authorLineEdit = QtWidgets.QLineEdit(self.guestFrame1)
        self.authorLineEdit.setGeometry(QtCore.QRect(180, 120, 591, 42))
        self.authorLineEdit.setStyleSheet("QLineEdit {\n"
"background-color:white;\n"
"border: 2px solid black;\n"
"}")
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.titleLabel = QtWidgets.QLabel(self.guestFrame1)
        self.titleLabel.setGeometry(QtCore.QRect(30, 70, 77, 42))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("QLabel {\n"
"background-color:white;\n"
"border: 2px solid black;\n"
"}")
        self.titleLabel.setObjectName("titleLabel")
        self.authorLabel = QtWidgets.QLabel(self.guestFrame1)
        self.authorLabel.setGeometry(QtCore.QRect(30, 120, 108, 42))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.authorLabel.setFont(font)
        self.authorLabel.setStyleSheet("QLabel {\n"
"background-color:white;\n"
"}")
        self.authorLabel.setObjectName("authorLabel")
        self.titleLineEdit = QtWidgets.QLineEdit(self.guestFrame1)
        self.titleLineEdit.setGeometry(QtCore.QRect(180, 70, 591, 42))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleLineEdit.setFont(font)
        self.titleLineEdit.setStyleSheet("QLineEdit {\n"
"background-color:white;\n"
"border: 2px solid black;\n"
"}")
        self.titleLineEdit.setText("")
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.resetButton = QtWidgets.QPushButton(self.guestFrame1)
        self.resetButton.setGeometry(QtCore.QRect(790, 140, 241, 71))
        self.resetButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.resetButton.setObjectName("resetButton")
        self.searchBookWidget = QtWidgets.QTableWidget(self.guestFrame1)
        self.searchBookWidget.setGeometry(QtCore.QRect(30, 240, 1001, 271))
        self.searchBookWidget.setStyleSheet("QTableWidget {\n"
"background-color:white;\n"
"border: 2px solid black;\n"
"border-radius:1px;\n"
"}")
        self.searchBookWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.searchBookWidget.setAlternatingRowColors(False)
        self.searchBookWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.searchBookWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.searchBookWidget.setShowGrid(True)
        self.searchBookWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.searchBookWidget.setRowCount(0)
        self.searchBookWidget.setColumnCount(0)
        self.searchBookWidget.setObjectName("searchBookWidget")
        self.searchBookWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.searchBookWidget.horizontalHeader().setDefaultSectionSize(238)
        self.searchBookWidget.horizontalHeader().setStretchLastSection(True)
        self.searchBookWidget.verticalHeader().setCascadingSectionResizes(True)
        self.searchBookWidget.verticalHeader().setStretchLastSection(False)
        self.backButton = QtWidgets.QPushButton(self.guestFrame)
        self.backButton.setGeometry(QtCore.QRect(800, 40, 241, 71))
        self.backButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"}")
        self.backButton.setObjectName("backButton")
        guestWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(guestWindow)
        QtCore.QMetaObject.connectSlotsByName(guestWindow)

    def retranslateUi(self, guestWindow):
        _translate = QtCore.QCoreApplication.translate
        guestWindow.setWindowTitle(_translate("guestWindow", "MainWindow"))
        self.guestFrame.setWhatsThis(_translate("guestWindow", "<html><head/><body><p>BUrak</p><p><br/></p></body></html>"))
        self.greetingLabel.setText(_translate("guestWindow", "Welcome Guest"))
        self.dateLabel.setText(_translate("guestWindow", "10.05.2017"))
        self.yearLabel.setText(_translate("guestWindow", "Year"))
        self.searchButton.setText(_translate("guestWindow", "Search"))
        self.titleLabel.setText(_translate("guestWindow", "Title"))
        self.authorLabel.setText(_translate("guestWindow", "Author"))
        self.resetButton.setText(_translate("guestWindow", "Reset"))
        self.searchBookWidget.setSortingEnabled(True)
        self.backButton.setText(_translate("guestWindow", "Back"))

