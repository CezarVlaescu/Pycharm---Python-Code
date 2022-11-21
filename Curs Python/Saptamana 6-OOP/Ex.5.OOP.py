class util():
    def __init__(self, user, password):
        self.__set__ = ()
        self.user = user
        self.password = password
class izatori(util):
    def __init__(self, user, password):
        super().__init__(user, password)
        self.user = user
        self.password = input('Scrie parola : ')
class utilizatori(izatori):
    def parole(self):
        return f'{self.password}'

cal = util('Cezar', '22222')
print(cal.__set__)
print(cal)






