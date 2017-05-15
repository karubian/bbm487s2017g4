from utils.DbClient import DbClient
from models.Member import Member
from models.Librarian import Librarian


class UserController:
    def __init__(self):
        self.client = DbClient.Instance()

    def get_user_by_username(self, username):
        found_user_info = self.client.find_user_by_username(username)
        new_user = None
        if found_user_info["type"] == "member":
            new_user = self.instantiate_user(found_user_info)
        elif found_user_info["type"] == "librarian":
            new_user = Librarian(found_user_info["username"], found_user_info["password"], found_user_info["name"],
                                 found_user_info["surname"], found_user_info["email"])
        new_user.id = str(found_user_info["_id"])

        return new_user

    def get_user_by_id(self, user_id):
        found_user_info = self.client.find_user_by_id(user_id)
        new_user = None
        if found_user_info:
            if found_user_info["type"] == "member":
                new_user = self.instantiate_user(found_user_info)
            elif found_user_info["type"] == "librarian":
                new_user = Librarian(found_user_info["username"], found_user_info["password"], found_user_info["name"],
                                     found_user_info["surname"], found_user_info["email"])
            new_user.id = str(found_user_info["_id"])

            return new_user

    def authorization(self, username, passkey):
        if self.client.db.users.find_one({"username": username, "password": passkey}) is not None:
            return 1
        return 0

    def update_member_attributes(self, user):
        self.client.update_member_attributes_db(user)

    def delete_one_user(self, user_id):
        self.client.delete_user_by_id(str(user_id))

    def add_new_member(self, username, password, name, surname, email):
        new_user = Member(username, password, name, surname, email)
        return self.client.add_new_member_db(new_user)

    def update_member(self, newUserInfo, userToUpdate):
        self.client.update_member_db(newUserInfo, userToUpdate)

    def search_users(self, username, name, surname):
        return self.client.search_user_db(username, name, surname)

    def delete_from_all_waiting_lists(self, book_id):
        all_users = self.client.search_user_db("", "", "")
        for user in all_users:
            if book_id in user["waitingBooks"]:
                operated_user = self.instantiate_user(user)
                operated_user.waitingBooks.remove(str(book_id))
                self.update_member_attributes(operated_user)

    def delete_from_all_owned_books(self, book_id):
        all_users = self.client.search_user_db("", "", "")
        for user in all_users:
            if book_id in user["loanedBooks"]:
                operated_user = self.instantiate_user(user)
                operated_user.loanedBooks.remove(str(book_id))
                self.update_member_attributes(operated_user)


    def instantiate_user(self, found_user_info):
        new_user = Member(found_user_info["username"], found_user_info["password"], found_user_info["name"],
                          found_user_info["surname"], found_user_info["email"])
        new_user.waitingBooks = found_user_info["waitingBooks"]
        new_user.currentFine = found_user_info["currentFine"]
        new_user.loanedBooks = found_user_info["loanedBooks"]
        new_user.totalLoanedBooks = found_user_info["totalLoanedBooks"]
        new_user.lastLoanedBook = found_user_info["lastLoanedBook"]
        new_user.formerFine = found_user_info["formerFine"]
        new_user.id = str(found_user_info["_id"])
        return new_user
