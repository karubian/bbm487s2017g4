from models.Book import Book
from utils.DbClient import DbClient


class BookController:
    def __init__(self):
        self.client = DbClient.Instance()

    def get_book_by_title(self, title):
        found_book_info = self.client.find_book_by_title(title)
        new_book = self.instantiate_book(found_book_info)
        return new_book

    def get_book_by_id(self, book_id):
        found_book_info = self.client.find_book_by_id(book_id)
        if found_book_info is not None:
            new_book = self.instantiate_book(found_book_info)
            return new_book
        else:
            return None

    def update_book_attributes(self, book):
        self.client.update_book_attributes_db(book)

    def delete_one_book_by_id(self, book_id):
        self.client.delete_book_by_id(book_id)

    def add_new_book(self, title, author, year, description, publisher):
        new_book = Book(title, author, year)
        new_book.description = description
        new_book.publisher = publisher
        self.client.add_new_book_db(new_book)

    def instantiate_book(self,found_book_info):
        new_book = Book(found_book_info["title"], found_book_info["author"], found_book_info["year"])
        new_book.id = found_book_info["_id"]
        new_book.isAvailable = found_book_info["isAvailable"]
        new_book.waitingList = found_book_info["waitingList"]
        new_book.description = found_book_info["description"]
        new_book.publisher = found_book_info["publisher"]
        return new_book

    def update_book(self, newBookInfo, bookToUpdate):
        self.client.update_book_db(newBookInfo, bookToUpdate)

    def search_books(self, title, author, year):
        return self.client.search_book_db(title, author, year)
