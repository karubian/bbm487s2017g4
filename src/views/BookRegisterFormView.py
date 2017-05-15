from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_bookRegisterForm import Ui_bookRegisterForm
from controllers.BookController import BookController
import views.ErrorView as errorView


class BookRegisterFormView(Ui_bookRegisterForm):
    def __init__(self):
        self.bookRegisterFormScreen = QtWidgets.QDialog()
        self.ui = Ui_bookRegisterForm()
        self.bookController = BookController()
        self.ui.setupUi(self.bookRegisterFormScreen)
        self.ui.registerButton.clicked.connect(self.register_book)
        self.ui.cancelButton.clicked.connect(self.terminate)
        self.error = errorView.ErrorView()
        self.currentBook = None
        self.type = 0  # 0 for create user 1 for update user

    def show(self):
        self.bookRegisterFormScreen.show()

    def terminate(self):
        self.bookRegisterFormScreen.hide()

    def clear_forms(self):
        self.ui.authorLineEdit.setText("")
        self.ui.titleLineEdit.setText("")
        self.ui.yearLineEdit.setText("")
        self.ui.descriptionTextEdit.setPlainText("")
        self.ui.publisherLineEdit.setText("")

    def prepare_update(self, book):
        self.ui.authorLineEdit.setText(book.author)
        self.ui.titleLineEdit.setText(book.title)
        self.ui.yearLineEdit.setText(book.publishedYear)
        self.ui.descriptionTextEdit.setPlainText(book.description)
        self.ui.publisherLineEdit.setText(book.publisher)

    def register_book(self):
        author = self.ui.authorLineEdit.text()
        title = self.ui.titleLineEdit.text()
        year = self.ui.yearLineEdit.text()
        publisher = self.ui.publisherLineEdit.text()
        description = self.ui.descriptionTextEdit.toPlainText()
        if self.type is 0:
            validation_flag = 0
            for field in [author, title, year,description,publisher]:
                if len(field) == 0:
                    self.error.set_error_text("Please fill the blank fields.")
                    self.error.show()
                    validation_flag = 1
            if validation_flag is 0:
                self.bookController.add_new_book(title, author, year,description, publisher)
        elif self.type is 1:
            validation_flag = 0
            for field in [author, title, year,description,publisher]:
                if len(field) == 0:
                    self.error.set_error_text("Please fill the blank fields.")
                    self.error.show()
                    validation_flag = 1
            if validation_flag is 0:
                self.bookController.update_book([title, author, year, description, publisher], self.currentBook)
        self.bookRegisterFormScreen.hide()
        self.clear_forms()
