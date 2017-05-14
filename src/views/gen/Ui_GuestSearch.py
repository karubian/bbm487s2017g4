# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guestView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GuestSearch(object):
    def setupUi(self, GuestSearch):
        GuestSearch.setObjectName("GuestSearch")
        GuestSearch.resize(1154, 834)
        self.guestMainFrame = QtWidgets.QFrame(GuestSearch)
        self.guestMainFrame.setGeometry(QtCore.QRect(0, 0, 1151, 831))
        self.guestMainFrame.setStyleSheet("QFrame {\n"
                                          "border: 3px solid gray;\n"
                                          "border-radius: 40px;\n"
                                          "background: rgb(255, 255, 222);\n"
                                          "}")
        self.guestMainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.guestMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.guestMainFrame.setObjectName("guestMainFrame")
        self.greetingLabel = QtWidgets.QLabel(self.guestMainFrame)
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
        self.dateLabel = QtWidgets.QLabel(self.guestMainFrame)
        self.dateLabel.setGeometry(QtCore.QRect(30, 10, 141, 41))
        self.dateLabel.setStyleSheet("QLabel {\n"
                                     "border: 3px solid rgb(255, 255, 222);\n"
                                     "font-size:20px;\n"
                                     "}")
        self.dateLabel.setObjectName("dateLabel")
        self.frame = QtWidgets.QFrame(self.guestMainFrame)
        self.frame.setGeometry(QtCore.QRect(10, 180, 1121, 631))
        self.frame.setStyleSheet("QWidget {\n"
                                 "border: 2px solid gray;\n"
                                 "border-radius:10px;\n"
                                 "background: rgb(233, 255, 254);\n"
                                 "font-size:30px;\n"
                                 "}")
        self.frame.setObjectName("frame")
        self.authorLineEdit_ = QtWidgets.QLineEdit(self.frame)
        self.authorLineEdit_.setGeometry(QtCore.QRect(210, 160, 591, 42))
        self.authorLineEdit_.setStyleSheet("QLineEdit {\n"
                                           "background-color:white;border-radius:0px;\n"
                                           "\n"
                                           "}")
        self.authorLineEdit_.setObjectName("authorLineEdit_")
        self.authorLabel_ = QtWidgets.QLabel(self.frame)
        self.authorLabel_.setGeometry(QtCore.QRect(60, 160, 108, 42))
        self.authorLabel_.setStyleSheet("QLabel {\n"
                                        "background-color:white;border-radius:0px;\n"
                                        "\n"
                                        "}")
        self.authorLabel_.setObjectName("authorLabel_")
        self.yearLineEdit_ = QtWidgets.QLineEdit(self.frame)
        self.yearLineEdit_.setGeometry(QtCore.QRect(210, 210, 591, 42))
        self.yearLineEdit_.setStyleSheet("QLineEdit {\n"
                                         "background-color:white;border-radius:0px;\n"
                                         "\n"
                                         "}")
        self.yearLineEdit_.setObjectName("yearLineEdit_")
        self.yearLabel_ = QtWidgets.QLabel(self.frame)
        self.yearLabel_.setGeometry(QtCore.QRect(60, 210, 108, 42))
        self.yearLabel_.setStyleSheet("QLabel {\n"
                                      "background-color:white;border-radius:0px;\n"
                                      "\n"
                                      "}")
        self.yearLabel_.setObjectName("yearLabel_")
        self.titleLabel_ = QtWidgets.QLabel(self.frame)
        self.titleLabel_.setGeometry(QtCore.QRect(60, 110, 77, 42))
        self.titleLabel_.setStyleSheet("QLabel {\n"
                                       "background-color:white;border-radius:0px;\n"
                                       "\n"
                                       "}")
        self.titleLabel_.setObjectName("titleLabel_")
        self.titleLineEdit_ = QtWidgets.QLineEdit(self.frame)
        self.titleLineEdit_.setGeometry(QtCore.QRect(210, 110, 591, 42))
        self.titleLineEdit_.setStyleSheet("QLineEdit {\n"
                                          "background-color:white;\n"
                                          "border-radius:0px;\n"
                                          "}")
        self.titleLineEdit_.setText("")
        self.titleLineEdit_.setObjectName("titleLineEdit_")
        self.searchButton_ = QtWidgets.QPushButton(self.frame)
        self.searchButton_.setGeometry(QtCore.QRect(850, 100, 241, 71))
        self.searchButton_.setStyleSheet("QPushButton {\n"
                                         "color: white;\n"
                                         "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                         "font-size: 30px;\n"
                                         "border-radius:0px;\n"
                                         "}")
        self.searchButton_.setObjectName("searchButton_")
        self.searchBookWidget_ = QtWidgets.QTableWidget(self.frame)
        self.searchBookWidget_.setGeometry(QtCore.QRect(60, 270, 1031, 321))
        self.searchBookWidget_.setStyleSheet("QTableWidget{\n"
                                             "border-radius:0px;\n"
                                             "}")
        self.searchBookWidget_.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.searchBookWidget_.setAlternatingRowColors(False)
        self.searchBookWidget_.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.searchBookWidget_.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.searchBookWidget_.setShowGrid(True)
        self.searchBookWidget_.setGridStyle(QtCore.Qt.SolidLine)
        self.searchBookWidget_.setRowCount(0)
        self.searchBookWidget_.setColumnCount(0)
        self.searchBookWidget_.setObjectName("searchBookWidget_")
        self.searchBookWidget_.horizontalHeader().setCascadingSectionResizes(True)
        self.searchBookWidget_.horizontalHeader().setDefaultSectionSize(238)
        self.searchBookWidget_.horizontalHeader().setStretchLastSection(True)
        self.searchBookWidget_.verticalHeader().setCascadingSectionResizes(True)
        self.searchBookWidget_.verticalHeader().setStretchLastSection(False)
        self.resetButton = QtWidgets.QPushButton(self.frame)
        self.resetButton.setGeometry(QtCore.QRect(850, 180, 241, 71))
        self.resetButton.setStyleSheet("QPushButton {\n"
                                       "color: white;\n"
                                       "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                       "font-size: 30px;\n"
                                       "border-radius:0px;\n"
                                       "}")
        self.resetButton.setObjectName("resetButton")
        self.backButton = QtWidgets.QPushButton(self.guestMainFrame)
        self.backButton.setGeometry(QtCore.QRect(840, 50, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton {\n"
                                      "color: white;\n"
                                      "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                      "font-size: 30px;\n"
                                      "}")
        self.backButton.setObjectName("backButton")
        self.logoutPng = QtWidgets.QLabel(self.guestMainFrame)
        self.logoutPng.setGeometry(QtCore.QRect(850, 60, 81, 71))
        self.logoutPng.setStyleSheet("QLabel {\n"
                                     "border:none;\n"
                                     "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                     "}")
        self.logoutPng.setText("")
        self.logoutPng.setPixmap(QtGui.QPixmap("../project/resources/logout.png"))
        self.logoutPng.setScaledContents(True)
        self.logoutPng.setObjectName("logoutPng")

        self.retranslateUi(GuestSearch)
        QtCore.QMetaObject.connectSlotsByName(GuestSearch)

    def retranslateUi(self, GuestSearch):
        _translate = QtCore.QCoreApplication.translate
        GuestSearch.setWindowTitle(_translate("GuestSearch", "Form"))
        self.guestMainFrame.setWhatsThis(
            _translate("GuestSearch", "<html><head/><body><p>BUrak</p><p><br/></p></body></html>"))
        self.greetingLabel.setText(_translate("GuestSearch", "Welcome Guest"))
        self.dateLabel.setText(_translate("GuestSearch", "10.05.2017"))
        self.authorLabel_.setText(_translate("GuestSearch", "Author"))
        self.yearLabel_.setText(_translate("GuestSearch", "Year"))
        self.titleLabel_.setText(_translate("GuestSearch", "Title"))
        self.searchButton_.setText(_translate("GuestSearch", "Search"))
        self.searchBookWidget_.setSortingEnabled(True)
        self.resetButton.setText(_translate("GuestSearch", "Reset"))
        self.backButton.setText(_translate("GuestSearch", "Back"))
