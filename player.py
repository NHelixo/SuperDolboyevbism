class Player:
    def __init__(self):
        self.name = ""
        self.age = ""

        self.balance = 0
        self.profit = 1

        self.total_balance = 0
    def update_balance(self, value):
        self.balance += value

        if value > 0:
            self.total_balance += value



player = Player()
