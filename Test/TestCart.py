from Domain.Cart import Cart
from Domain.Item import Item

class TestCart:

    def __init__(self):
        self.cart = Cart()

        self.cart.add(Item("A", "A-01", 'A item', 1.00))
        self.cart.add(Item("B", "B-01", 'B item', 2.00))
        self.cart.add(Item("C", "C-01", 'C item', 3.00))
        self.cart.add(Item("D", "D-01", 'D item', 4.00))
        self.cart.add(Item("F", "E-01", 'E item', 5.00))
        self.cart.add(Item("A", "A-01", 'A item', 1.00))

    def TestTotal(self):
        print("TestTotal")
        if self.cart.total() == 16.00:
            print("pass")
        else:
            print("failed")

    def TestCount(self):
        print("TestCount")
        if self.cart.count() == 6:
            print("pass")
        else:
            print("failed")

    def TestGetItem(self):
        print("TestGetItem")
        t = self.cart.getItem('B-01')
        if (type(t) is Item) and (t.getName() == "B"):
            print("pass")
        else:
            print("failed")

    def TestRemoveItem(self):
        print("TestRemoveItem")
        item = self.cart.remove('A-01')
        if (2 == item['count']):
            print("pass")
        else:
            print("failed")