from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_bookInfoWindow import Ui_bookInfoWindow


class BookInfoView(Ui_bookInfoWindow):
    def __init__(self,book):
        self.bookInfoWindow = QtWidgets.QMainWindow()
        self.ui = Ui_bookInfoWindow()
        self.ui.setupUi(self.bookInfoWindow)
        self.book = book
        self.ui.backButton.clicked.connect(self.terminate)
        self.update_scene()

    def show(self):
        self.bookInfoWindow.show()

    def terminate(self):
        self.bookInfoWindow.hide()

    def update_scene(self):
        self.ui.titleLabel.setText("Title : " + self.book.title)
        self.ui.authorLabel.setText("Author : " + self.book.author)
        self.ui.PublicationLabel.setText("Publication Date : " + str(self.book.publishedYear))
        print(self.book.description)
        self.ui.textBrowser.insertPlainText(self.book.description)
