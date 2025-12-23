class AuthService:
    def login(self, username, password):
        if username == 'elek' and password == 'alma':
            return 'TOKEN1223'
        raise ValueError('Nem jo a user vagy a jelszo')
