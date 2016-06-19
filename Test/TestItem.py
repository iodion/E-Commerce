from Domain.Item import Item

class TestItem:

    def __init__(self):
        self.item = Item("Bicycle", "BIC-2013", 56.99, "BMX")

    def testGetName(self):
        print("testGetName")
        if self.item.getName() == "Bicycle":
            print("Pass")
        else:
            print("Failed")

    def testGetSku(self):
        print("testGetSku")
        if self.item.getSku() == "BIC-2013":
            print("Pass")
        else:
            print("Failed")

    def testGetDesr(self):
        print("testGetDesr")
        if self.item.getDesr() == "BMX":
            print("Pass")
        else:
            print("Failed")

    def testGetPrice(self):
        print("testGetPrice")
        if self.item.getPrice() == 56.99:
            print("Pass")
        else:
            print("Failed")