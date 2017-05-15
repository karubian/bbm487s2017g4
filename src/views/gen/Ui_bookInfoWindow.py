# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookInfo.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bookInfoWindow(object):
    def setupUi(self, bookInfoWindow):
        bookInfoWindow.setObjectName("bookInfoWindow")
        bookInfoWindow.resize(796, 583)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bookInfoWindow.sizePolicy().hasHeightForWidth())
        bookInfoWindow.setSizePolicy(sizePolicy)
        bookInfoWindow.setMinimumSize(QtCore.QSize(796, 583))
        bookInfoWindow.setMaximumSize(QtCore.QSize(796, 583))
        bookInfoWindow.setStyleSheet("QFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(bookInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bookInfoFrame = QtWidgets.QFrame(self.centralwidget)
        self.bookInfoFrame.setGeometry(QtCore.QRect(0, 10, 791, 571))
        self.bookInfoFrame.setStyleSheet("QFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: rgb(255, 255, 222);\n"
"}")
        self.bookInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bookInfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bookInfoFrame.setObjectName("bookInfoFrame")
        self.headerLabel = QtWidgets.QLabel(self.bookInfoFrame)
        self.headerLabel.setGeometry(QtCore.QRect(30, 10, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.headerLabel.setFont(font)
        self.headerLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 255, 222);\n"
"font-size:40px;\n"
"}")
        self.headerLabel.setWordWrap(False)
        self.headerLabel.setObjectName("headerLabel")
        self.bookInfoWidget = QtWidgets.QWidget(self.bookInfoFrame)
        self.bookInfoWidget.setGeometry(QtCore.QRect(10, 80, 771, 481))
        self.bookInfoWidget.setStyleSheet("QWidget {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: rgb(255, 239, 211);\n"
"}")
        self.bookInfoWidget.setObjectName("bookInfoWidget")
        self.image = QtWidgets.QGraphicsView(self.bookInfoWidget)
        self.image.setGeometry(QtCore.QRect(600, 20, 131, 151))
        self.image.setObjectName("image")
        self.titleLabel = QtWidgets.QLabel(self.bookInfoWidget)
        self.titleLabel.setGeometry(QtCore.QRect(40, 30, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 239, 211);\n"
"font-size:30px;\n"
"}")
        self.titleLabel.setObjectName("titleLabel")
        self.authorLabel = QtWidgets.QLabel(self.bookInfoWidget)
        self.authorLabel.setGeometry(QtCore.QRect(40, 90, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.authorLabel.setFont(font)
        self.authorLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 239, 211);\n"
"font-size:30px;\n"
"}")
        self.authorLabel.setObjectName("authorLabel")
        self.descLabel = QtWidgets.QLabel(self.bookInfoWidget)
        self.descLabel.setGeometry(QtCore.QRect(40, 200, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.descLabel.setFont(font)
        self.descLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 239, 211);\n"
"font-size:30px;\n"
"}")
        self.descLabel.setObjectName("descLabel")
        self.textBrowser = QtWidgets.QTextBrowser(self.bookInfoWidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 280, 611, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("QWidget {\n"
"border: 3px solid rgb(255, 239, 211);\n"
"border-radius: 0px;\n"
"background: rgb(255, 239, 211);\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.PublicationLabel = QtWidgets.QLabel(self.bookInfoWidget)
        self.PublicationLabel.setGeometry(QtCore.QRect(40, 140, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.PublicationLabel.setFont(font)
        self.PublicationLabel.setStyleSheet("QLabel {\n"
"border: 3px solid rgb(255, 239, 211);\n"
"font-size:30px;\n"
"}")
        self.PublicationLabel.setObjectName("PublicationLabel")
        self.backButton = QtWidgets.QPushButton(self.bookInfoFrame)
        self.backButton.setGeometry(QtCore.QRect(560, 10, 181, 61))
        self.backButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
"font-size: 30px;\n"
"border-radius:10px;\n"
"}")
        self.backButton.setObjectName("backButton")
        bookInfoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(bookInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(bookInfoWindow)

    def retranslateUi(self, bookInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        bookInfoWindow.setWindowTitle(_translate("bookInfoWindow", "MainWindow"))
        self.headerLabel.setText(_translate("bookInfoWindow", "Book Information"))
        self.titleLabel.setText(_translate("bookInfoWindow", "Title : Learning Linux Binary Analysis"))
        self.authorLabel.setText(_translate("bookInfoWindow", "Author :  Ryan \"elfmaster\" O\'Neill"))
        self.descLabel.setText(_translate("bookInfoWindow", "Book Description:"))
        self.textBrowser.setHtml(_translate("bookInfoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffefd3;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:15pt; color:#333333; background-color:#ffefd3;\">Learning Linux Binary Analysis is packed with knowledge and code that will teach you the inner workings of the ELF format, and the methods used by hackers and security analysts for virus analysis, binary patching, software protection and more.</span></p></body></html>"))
        self.PublicationLabel.setText(_translate("bookInfoWindow", "Publication Date :   February 29, 2016"))
        self.backButton.setText(_translate("bookInfoWindow", "Back"))

