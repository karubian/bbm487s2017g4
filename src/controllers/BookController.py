from models.Book import Book
from utils.DbClient import DbClient


class BookController:
    def __init__(self):
        self.client = DbClient.Instance()

    def get_book_by_title(self, title):
        found_book_info = self.client.find_book_by_title(title)
        new_book = Book(found_book_info["title"], found_book_info["author"], found_book_info["year"])
        new_book.id = found_book_info["_id"]
        new_book.isAvailable = found_book_info["isAvailable"]
        new_book.waitingList = found_book_info["waitingList"]
        return new_book

    def get_book_by_id(self, id):
        found_book_info = self.client.find_book_by_id(id)
        new_book = Book(found_book_info["title"], found_book_info["author"], found_book_info["year"])
        new_book.id = found_book_info["_id"]
        new_book.isAvailable = found_book_info["isAvailable"]
        new_book.waitingList = found_book_info["waitingList"]
        return new_book

    def update_book_attributes(self, book):
        self.client.update_book_attributes_db(book)

    def delete_one_book(self, title):
        self.client.delete_book(title)

    def add_new_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.client.add_new_book_db(new_book)

    def update_book(self, newBookInfo, bookToUpdate):
        self.client.update_book_db(newBookInfo, bookToUpdate)

    def search_books(self, title, author, year):
        return self.client.search_book_db(title, author, year)
