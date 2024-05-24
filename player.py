class Player:
    def __init__(self):
        self.name = ""
        self.age = ""

        self.balance = 0
        self.profit = 1

        self.total_balance = 0
    
    def load_data(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.balance = data["balance"]
        self.profit = data["profit"]
        self.total_balance = data["total_balance"]

    def to_json(self):
        return {
            "name": self.name,
            "age": self.age,
            "balance": self.balance,
            "profit": self.profit,
            "total_balance": self.total_balance
        }

    def update_balance(self, value):
        self.balance += value

        if value > 0:
            self.total_balance += value



player = Player()
