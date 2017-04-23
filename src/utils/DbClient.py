import pymongo
from .Singleton import Singleton


@Singleton
class DbClient:
    def __init__(self):
        # self.uri = 'mongodb://library_manager:11223344@ds149030.mlab.com:49030/bbm487_library'
        self.uri = 'mongodb://localhost:27017/'
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client.bbm487_library

    def authorization(self, username, passkey):
        if self.db.users.find_one({"username": username, "password": passkey}) is not None:
            return 1
        return 0

    def find_user_by_username(self, username):
        new_user = None
        found_user = self.db.users.find_one({"username": username})
        if found_user is None:
            return 0
        return found_user

    def find_book_by_title(self, title):
        found_book = self.db.books.find_one({"title": title})
        if found_book is None:
            return 0
        return found_book

    def find_book_by_id(self, id):
        found_book = self.db.books.find_one({"_id": id})
        if found_book is None:
            return 0
        return found_book

    def delete_user(self, username):
        self.db.users.delete_one({'username': username})

    def delete_book(self, title):
        self.db.books.delete_one({'title': title})

    def add_new_book_db(self, new_book):
        try:
            result = self.db.books.insert_one(
                {
                    "title": new_book.title,
                    "author": new_book.author,
                    "year": new_book.publishedYear,
                    "isAvailable": new_book.isAvailable,
                    "waitingList": new_book.waitingList
                }
            )
            return 1
        except:
            return None

    def add_new_member_db(self, new_user):
        try:
            result = self.db.users.insert_one(
                {
                    "username": new_user.username,
                    "password": new_user.password,
                    "type": "member",
                    "name": new_user.name,
                    "surname": new_user.surname,
                    "waitingBooks": new_user.waitingBooks,
                    "fineAmount": new_user.fineAmount,
                    "loanedBooks": new_user.loanedBooks,
                    "email": new_user.email_address,
                    "totalLoanedBooks": new_user.totalLoanedBooks
                }
            )
            return 1
        except:
            return None

    def update_member_db(self, newUserInfo, userToUpdate):
        try:
            self.db.users.update_one({
                '_id': userToUpdate.id}, {"$set": {
                "username": newUserInfo[0],
                "password": newUserInfo[1],
                "email_address": newUserInfo[2],
                "name": newUserInfo[3],
                "surname": newUserInfo[4]
            }
            })
            return 1
        except:
            return None

    def update_member_attributes_db(self, updated_member):
        try:
            result = self.db.users.update_one({
                '_id': updated_member.id}, {"$set": {
                "username": updated_member.username,
                "password": updated_member.password,
                "email_address": updated_member.email_address,
                "name": updated_member.name,
                "surname": updated_member.surname,
                "waitingBooks": updated_member.waitingBooks,
                "fineAmount": updated_member.fineAmount,
                "loanedBooks": updated_member.loanedBooks,
                "email": updated_member.email_address,
                "totalLoanedBooks": updated_member.totalLoanedBooks
            }
            })
            return 1
        except:
            return None

    def update_book_attributes_db(self, updated_book):
        try:
            result = self.db.books.update_one({
                '_id': updated_book.id}, {"$set": {
                "title": updated_book.title,
                "author": updated_book.author,
                "year": updated_book.publishedYear,
                "isAvailable": updated_book.isAvailable,
                "waitingList": updated_book.waitingList,
            }
            })
            return 1
        except:
            return None

    def update_book_db(self, newBookInfo, bookToUpdate):
        try:
            result = self.db.books.update_one({
                '_id': bookToUpdate.id}, {"$set": {
                "title": newBookInfo[0],
                "author": newBookInfo[1],
                "year": newBookInfo[2],
            }
            })
            return 1
        except:
            return None

    def search_user_db(self, username, name, surname):
        for field in [username, name, surname]:
            if len(field) is 0:
                field = ""
        found_info = self.db.users.find({
            "type": "member",
            "username": {"$regex":
                             username, '$options': 'i'},
            "name": {"$regex":
                         name, '$options': 'i'},
            "surname": {"$regex":
                            surname, '$options': 'i'},
        })

        return found_info

    def search_book_db(self, title, author, year):
        for field in [title, author, year]:
            if len(field) is 0:
                field = ""
        found_info = self.db.books.find({
            "title": {"$regex":
                          title, '$options': 'i'},
            "author": {"$regex":
                           author, '$options': 'i'},
            "year": {"$regex":
                         year, '$options': 'i'},
        })

        return found_info

    def close_session(self):
        self.client.close()


        # result = self.db.users.insert_one(
        #     {
        #         "username": "burak",
        #         "password": "1122",
        #         "type":"member",
        #         "name":"İrem",
        #         "surname":"Özdal"
        #     })
        # print(result)
        # elif found_user["type"] == "member":
        #     new_user = Member(found_user["username"], found_user["password"])
        # elif found_user["type"] == "librarian":
        #     new_user = Librarian(found_user["username"], found_user["password"])
        # new_user.name = found_user["name"]
        # new_user.surname = found_user["surname"]
