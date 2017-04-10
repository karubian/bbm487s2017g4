import pymongo
from models.Member import Member
from models.Librarian import Librarian
from .Singleton import Singleton


@Singleton
class DbClient:
    def __init__(self):
        self.uri = 'mongodb://library_manager:11223344@ds149030.mlab.com:49030/bbm487_library'
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client.bbm487_library

    def authorization(self, username, passkey, isLibrary):
        if isLibrary:
            if self.db.librarians.find_one({"username": username, "password": passkey}) is not None:
            # found = self.db.members.find({"username": username, "password": passkey})
                return 1
        else:
            if self.db.members.find_one({"username": username, "password": passkey}) is not None:
                return 1

        return 0

    def find_user_by_username(self, username,type_bool):
        new_user = None
        if type_bool:
            found_user = self.db.librarians.find_one({"username": username})
            new_user = Librarian(found_user["username"], found_user["password"])
        else:
            found_user = self.db.members.find_one({"username": username})
            new_user = Member(found_user["username"], found_user["password"])
            new_user.name = found_user["name"]
            new_user.surname = found_user["surname"]

        return new_user

    def list_all_users(self):
        found = self.db.members.find({})
        member_list = []
        for record in found:
            member_list.append(record["username"])
        return member_list

    def close_session(self):
        self.client.close()
        # result = self.db.librarians.insert_one(
        #     {
        #         "username": "librarian",
        #         "password": "1122"
        #
        #     })
        # print(result)