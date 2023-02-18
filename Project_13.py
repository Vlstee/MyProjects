from random import random

class RandIter:
    def __init__(self, quant):
        self.quantity = quant
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.quantity > 0:
            self.cur += random()
            self.quantity -= 1
            return round(self.cur, 2)
        else:
            raise StopIteration


iterat = RandIter(8)

for i in iterat:
    print(list(iterat))