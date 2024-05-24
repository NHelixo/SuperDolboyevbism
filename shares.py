from datetime import datetime
from random import randint


class Share:
    price = 500
    def __init__(self):
        self.min_price_range = 1
        self.max_price_range = 1000

        self.diff = 50

        self.update_time = datetime.now()
        self.time_out = 10
    def update_price(self):
        if (datetime.now() - self.update_time).seconds >= self.time_out:
            self.update_time = datetime.now()
            direction = randint(1,3)
            if direction == 2:
                self.price -= randint(1, self.diff)

            elif direction == 3:
                self.price += randint(1, self.diff)

