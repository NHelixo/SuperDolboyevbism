from datetime import datetime
from random import randint


class Share:
    initial_price = 500

    def __init__(self):
        self.min_price_range = 1
        self.max_price_range = 1000

        self.price = Share.initial_price
        self.diff = 50

        self.update_time = datetime.now()
        self.time_out = 10

    def get_new_price(self):
        price = self.price
        if (datetime.now() - self.update_time).seconds >= self.time_out:
            self.update_time = datetime.now()
            direction = randint(1,3)
            if direction == 2:
                price -= randint(1, self.diff)

            elif direction == 3:
                price += randint(1, self.diff)
        
        return price

