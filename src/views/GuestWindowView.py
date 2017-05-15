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
        self.list_books()
        self.ui.searchBookWidget_.cellDoubleClicked.connect(self.show_book_info_search)
        self.set_button_effects()

    def show(self):
        self.guestSearchScreen.show()

    def return_login(self):
        import views.LoginView as loginView
        self.login = loginView.LoginView()
        self.guestSearchScreen.hide()
        self.login.show()

    def customize_scene(self):
        self.ui.dateLabel.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.ui.searchBookWidget_.setColumnCount(4)
        self.ui.searchBookWidget_.setHorizontalHeaderLabels(["Title", "Author", "Published Year", "Book ID"])
        self.ui.searchBookWidget_.horizontalHeaderItem(2).setTextAlignment(QtCore.Qt.AlignLeft)

    def list_books(self):
        query_result = self.bookController.search_books(self.current_book_queries[0], self.current_book_queries[1],
                                                        self.current_book_queries[2])
        i = 0
        current_row_count = query_result.count()
        self.ui.searchBookWidget_.setRowCount(current_row_count)
        for record in query_result:
            self.ui.searchBookWidget_.setItem(i, 0, QtWidgets.QTableWidgetItem(record["title"]))
            self.ui.searchBookWidget_.setItem(i, 1, QtWidgets.QTableWidgetItem(record["author"]))
            self.ui.searchBookWidget_.setItem(i, 2, QtWidgets.QTableWidgetItem(record["year"]))
            self.ui.searchBookWidget_.setItem(i, 3, QtWidgets.QTableWidgetItem(str(record["_id"])))
            self.ui.searchBookWidget_.item(i, 2).setTextAlignment(QtCore.Qt.AlignLeft)
            i = i + 1
        self.show()

    def search_books(self):
        search_title = self.ui.titleLineEdit_.text()
        search_author = self.ui.authorLineEdit_.text()
        search_year = self.ui.yearLineEdit_.text()
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
            selected_book_id = self.ui.searchBookWidget_.item(selected_row, 3).text()
            selected_book = self.bookController.get_book_by_id(str(selected_book_id))
            self.book_info = bookInfoView.BookInfoView(selected_book)
            self.book_info.update_scene()
            self.book_info.show()


    def set_button_effects(self):
        self.ui.backButton.released.connect(self.released_color_change)
        self.ui.backButton.pressed.connect(self.pressed_color_change)
        self.ui.resetButton.released.connect(self.released_color_change)
        self.ui.resetButton.pressed.connect(self.pressed_color_change)
        self.ui.searchButton_.released.connect(self.released_color_change)
        self.ui.searchButton_.pressed.connect(self.pressed_color_change)


    def released_color_change(self):
        self.guestSearchScreen.sender().setStyleSheet("QPushButton {\n"
                                                  "color: white;\n"
                                                  "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                                  "font-size: 30px;\n"
                                                  "border-radius:10px;\n"
                                                  "}")

    def pressed_color_change(self):
        self.guestSearchScreen.sender().setStyleSheet("QPushButton {\n"
                                                  "color: white;\n"
                                                  "background-color: red;\n"
                                                  "font-size: 30px;\n"
                                                  "border-radius:10px;\n"
                                                  "}")