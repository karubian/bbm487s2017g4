import pymongo
from .Singleton import Singleton
from bson.objectid import ObjectId


@Singleton
class DbClient:
    def __init__(self):
        # self.uri = 'mongodb://library_manager:11223344@ds149030.mlab.com:49030/bbm487_library'
        self.uri = 'mongodb://localhost:27017/'
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client.bbm487_library
        self.db.users.create_index("username",unique=True)

    def find_user_by_username(self, username):
        found_user = self.db.users.find_one({"username": username})
        if found_user is None:
            return 0
        return found_user

    def find_user_by_id(self, user_id):
        if type(user_id) is str:
            found_user = self.db.users.find_one({"_id": ObjectId(user_id)})
        else:
            found_user = self.db.users.find_one({"_id": user_id})
        if found_user is None:
            return 0
        return found_user

    def find_book_by_title(self, title):
        found_book = self.db.books.find_one({"title": title})
        if found_book is None:
            return 0
        return found_book

    def find_book_by_id(self, book_id):
        if type(book_id) is str:
            found_book = self.db.books.find_one({"_id": ObjectId(book_id)})
        else:
            found_book = self.db.books.find_one({"_id": book_id})
        if found_book is None:
            return None
        return found_book

    def delete_user(self, username):
        self.db.users.delete_one({'username': username})
        return

    def delete_user_by_id(self, user_id):
        if type(user_id) is str:
            self.db.users.delete_one({"_id": ObjectId(user_id)})
        else:
            self.db.users.delete_one({'_id': user_id})

    def delete_loan_record(self, book_id):
        self.db.loans.delete_one({'book_id': book_id})

    def delete_book(self, title):
        self.db.books.delete_one({'title': title})

    def delete_book_by_id(self, book_id):
        if type(book_id) is str:
            self.db.books.delete_one({"_id": ObjectId(book_id)})
        else:
            self.db.books.delete_one({'_id': book_id})

    def add_new_book_db(self, new_book):
        try:
            result = self.db.books.insert_one(
                {
                    "title": new_book.title,
                    "author": new_book.author,
                    "year": new_book.publishedYear,
                    "description": new_book.description,
                    "isAvailable": new_book.isAvailable,
                    "waitingList": new_book.waitingList,
                    "publisher": new_book.publisher
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
                    "currentFine": new_user.currentFine,
                    "formerFine":new_user.formerFine,
                    "loanedBooks": new_user.loanedBooks,
                    "email": new_user.email_address,
                    "totalLoanedBooks": new_user.totalLoanedBooks,
                    "lastLoanedBook": new_user.lastLoanedBook
                }
            )
            return 1
        except:
            return None

    def add_loan_record(self, new_loan):
        try:
            result = self.db.loans.insert_one(
                {
                    "book_id": str(new_loan.book_id),
                    "user_id": str(new_loan.user_id),
                    "startDate": new_loan.startDate,
                    "returnDate": new_loan.returnDate,
                    "currentFine": new_loan.currentFine,
                    "status": new_loan.status
                }
            )
            return 1
        except:
            return None

    def find_loan_record(self, book_id):
        found_loan = self.db.loans.find_one({"book_id": book_id})
        if found_loan is None:
            return 0
        return found_loan

    def update_member_db(self, newUserInfo, userToUpdate):
        try:
            self.db.users.update_one({
                '_id': ObjectId(userToUpdate.id)}, {"$set": {
                "username": newUserInfo[0],
                "password": newUserInfo[1],
                "email": newUserInfo[2],
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
                '_id': ObjectId(updated_member.id)}, {"$set": {
                "username": updated_member.username,
                "password": updated_member.password,
                "email": updated_member.email_address,
                "name": updated_member.name,
                "surname": updated_member.surname,
                "waitingBooks": updated_member.waitingBooks,
                "currentFine": updated_member.currentFine,
                "formerFine":updated_member.formerFine,
                "loanedBooks": updated_member.loanedBooks,
                "totalLoanedBooks": updated_member.totalLoanedBooks,
                "lastLoanedBook": updated_member.lastLoanedBook
            }
            })
            return 1
        except:
            return None

    def update_loan_attributes_db(self, updated_loan):
        try:
            result = self.db.loans.update_one({
                'book_id': ObjectId(updated_loan.book_id)}, {"$set": {
                "currentFine": updated_loan.currentFine,
                "formerFine": updated_loan.formerFine,
                "status": updated_loan.status,
                "returnDate": updated_loan.returnDate,
                "startDate": updated_loan.startDate
            }
            })
            return 1
        except:
            return None

    def update_book_attributes_db(self, updated_book):
        try:
            result = self.db.books.update_one({
                '_id': ObjectId(updated_book.id)}, {"$set": {
                "title": updated_book.title,
                "author": updated_book.author,
                "year": updated_book.publishedYear,
                "description": updated_book.description,
                "isAvailable": updated_book.isAvailable,
                "waitingList": updated_book.waitingList,
                "publisher": updated_book.publisher
            }
            })
            return 1
        except:
            return None

    def update_book_db(self, newBookInfo, bookToUpdate):
        try:
            result = self.db.books.update_one({
                '_id': ObjectId(bookToUpdate.id)}, {"$set": {
                "title": newBookInfo[0],
                "author": newBookInfo[1],
                "year": newBookInfo[2],
                "description": newBookInfo[3],
                "publisher": newBookInfo[4]
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
