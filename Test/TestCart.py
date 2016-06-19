from Domain.Cart import Cart
from Domain.Item import Item

class TestCart:

    def __init__(self):
        self.cart = Cart()

        self.cart.add(Item("A", "A-01", 1.00, 'A item'))
        self.cart.add(Item("B", "B-01", 2.00, 'B item'))
        self.cart.add(Item("C", "C-01", 3.00, 'C item'))
        self.cart.add(Item("D", "D-01", 4.00, 'D item'))
        self.cart.add(Item("F", "E-01", 5.00, 'E item'))
        self.cart.add(Item("A", "A-01", 1.00, 'A item'))

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
        prev = self.cart.count()
        self.cart.remove('A-01')
        now = self.cart.count()

        if (now + 1 == prev):
            print("pass")
        else:
            print("failed")