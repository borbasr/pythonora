class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_users(self, user):
        self.users.remove(user)

    def get_users(self):
        return self.users
