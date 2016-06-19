import sys
from Domain.Item import Item

class Cart(object):

    def __init__(self):
        self._total = 0.0
        self._count = 0

        self.items = {}
        self.qty = {}

    '''
    Add item to cart
    @param Item
    '''
    def add(self, item):
        if (type(item) is Item) and (item.getSku() in self.items.keys()):
            self.qty[item.getSku()] += 1
        else:
            self.items[item.getSku()] = item
            self.qty[item.getSku()] = 1

        self._count += 1
        self._total += item.getPrice()

    '''
    @param string sku
    '''
    def remove(self, sku):
        if (self.qty[sku] > 0):
            self.qty[sku] -= 1
            self._count -= 1
            self._total -= self.items[sku].getPrice()
        elif (self.qty[sku] == 0):
            del self.items[sku]
            del self.qty[sku]

    '''
    Get number of items in cart
    @return int
    '''
    def count(self):
        return self._count

    '''
    Get total
    @return int
    '''
    def total(self):
        return self._total

    '''
    Get an item
    @param string sku
    @return Item
    '''
    def getItem(self, sku):
        return self.items[sku]
