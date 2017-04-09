from utils.DbClient import DbClient


class UserController:
    def __init__(self):
        self.client = DbClient.Instance()

    def get_user_by_username(self, username,type_id):
        return self.client.find_user_by_username(username,type_id)

    def get_all_users(self):
        return self.client.list_all_users()

aa = UserController()
aa.get_all_users()


