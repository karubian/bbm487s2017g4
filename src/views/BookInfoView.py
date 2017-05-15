from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_bookInfoWindow import Ui_bookInfoWindow


class BookInfoView(Ui_bookInfoWindow):
    def __init__(self, book):
        self.bookInfoWindow = QtWidgets.QMainWindow()
        self.ui = Ui_bookInfoWindow()
        self.ui.setupUi(self.bookInfoWindow)
        self.book = book
        self.ui.backButton.clicked.connect(self.terminate)
        self.update_scene()
        self.set_button_effects()

    def show(self):
        self.update_scene()
        self.bookInfoWindow.show()

    def terminate(self):
        self.bookInfoWindow.hide()

    def update_scene(self):
        self.ui.titleLabel.setText("Title : " + self.book.title)
        self.ui.authorLabel.setText("Author : " + self.book.author)
        self.ui.PublicationLabel.setText("Publication Date : " + str(self.book.publishedYear))
        self.ui.textBrowser.setPlainText(self.book.description)

    def set_button_effects(self):
        self.ui.backButton.released.connect(self.released_color_change)
        self.ui.backButton.pressed.connect(self.pressed_color_change)

    def released_color_change(self):
        self.bookInfoWindow.sender().setStyleSheet("QPushButton {\n"
                                                   "color: white;\n"
                                                   "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                                   "font-size: 30px;\n"
                                                   "border-radius:10px;\n"
                                                   "}")

    def pressed_color_change(self):
        self.bookInfoWindow.sender().setStyleSheet("QPushButton {\n"
                                                   "color: white;\n"
                                                   "background-color: red;\n"
                                                   "font-size: 30px;\n"
                                                   "border-radius:10px;\n"
                                                   "}")
