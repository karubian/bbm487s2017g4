import pymongo
from models import User


class DbClient:
    def __init__(self):
        self.uri = 'mongodb://lib_manager:11223344@ds149030.mlab.com:49030/bbm487_library'
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client.bbm487_library

    def authorization(self, username, passkey):
        if self.db.User.find({"username": username, "password": passkey}).count() > 0:
            found = self.db.User.find({"username": username, "password": passkey})
            self.close_session()
            return 1
        else:
            self.close_session()
            return 0

    def init_user(self, username, passkey):
        found = self.db.User.find({"username": username, "password": passkey})
        newuser = User.User(found[0]["username"], found[0]["password"])
        newuser.name = found[0]["name"]
        newuser.surname = found[0]["surname"]
        return newuser

    def close_session(self):
        self.client.close()




        # result = db.User.insert_one(
        #     {
        #         "username": "member",
        #         "password": "1122"
        #
        # })
        # print(result)
