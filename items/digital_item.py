from .item import Item

class DigitalItem(Item):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.quantity = 1

    def sell(self, amount):
        self.quantity = 1
        return True

    def stock(self, amount):
        self.quantity = 1
        return True
