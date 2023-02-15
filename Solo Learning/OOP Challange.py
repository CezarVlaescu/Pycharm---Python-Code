class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def names(self):
        return f"The account owner is {self.name}"

    def bal(self):
        return f"The balance is {self.balance}"

    current_balance = 0

    def deposit(self):
        if self.balance < 50:
            return f"Your new balance is {self.current_balance} + {self.balance}"
        elif self.balance > 75:
            return f"Withdraw of {self.balance}"



