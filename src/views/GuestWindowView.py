from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_GuestSearch import Ui_GuestSearch
from controllers.BookController import BookController
import datetime
import views.BookInfoView as bookInfoView


class GuestWindowView(Ui_GuestSearch):
    def __init__(self):
        self.guestSearchScreen = QtWidgets.QWidget()
        self.ui = Ui_GuestSearch()
        self.bookController = BookController()
        self.ui.setupUi(self.guestSearchScreen)
        self.ui.backButton.clicked.connect(self.return_login)
        self.ui.searchButton_.clicked.connect(self.search_books)
        self.ui.resetButton.clicked.connect(self.reset_book_filters)
        self.customize_scene()
        self.bookController = BookController()
        self.book_info = None
        self.current_book_queries = ["", "", ""]
        self.book_ids = []
        self.list_books()
        self.ui.searchBookWidget_.cellDoubleClicked.connect(self.show_book_info_search)

    def show(self):
        self.guestSearchScreen.show()

    def return_login(self):
        import views.LoginView as loginView
        self.login = loginView.LoginView()
        self.guestSearchScreen.hide()
        self.login.show()

    def customize_scene(self):
        self.ui.dateLabel.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.ui.searchBookWidget_.setColumnCount(3)
        self.ui.searchBookWidget_.setHorizontalHeaderLabels(["Title", "Author", "Published Year"])

    def list_books(self):
        self.book_ids = []
        query_result = self.bookController.search_books(self.current_book_queries[0], self.current_book_queries[1],
                                                        self.current_book_queries[2])
        i = 0
        current_row_count = query_result.count()
        self.ui.searchBookWidget_.setRowCount(current_row_count)
        for record in query_result:
            self.book_ids.insert(i, record["_id"])
            self.ui.searchBookWidget_.setItem(i, 0, QtWidgets.QTableWidgetItem(record["title"]))
            self.ui.searchBookWidget_.setItem(i, 1, QtWidgets.QTableWidgetItem(record["author"]))
            self.ui.searchBookWidget_.setItem(i, 2, QtWidgets.QTableWidgetItem(record["year"]))
            i = i + 1
        self.show()

    def search_books(self):
        search_title  = self.ui.titleLineEdit_.text()
        search_author = self.ui.authorLineEdit_.text()
        search_year   = self.ui.yearLineEdit_.text()
        self.current_book_queries = [search_title, search_author, search_year]
        self.list_books()

    def reset_book_filters(self):
        self.current_book_queries = ["", "", ""]
        self.ui.titleLineEdit_.setText("")
        self.ui.authorLineEdit_.setText("")
        self.ui.yearLineEdit_.setText("")
        self.list_books()

    def show_book_info_search(self):
        selected_row = self.ui.searchBookWidget_.currentRow()
        if selected_row > -1:
            selected_book_title = self.ui.searchBookWidget_.item(selected_row, 0).text()
            selected_book = self.bookController.get_book_by_title(selected_book_title)
            self.book_info = bookInfoView.BookInfoView(selected_book)
            self.book_info.update_scene()
            self.book_info.show()