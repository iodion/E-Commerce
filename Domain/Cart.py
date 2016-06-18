import sys
from Domain.Item import Item

class Cart(object):

    def __init__(self):
        self.items = {}

    '''
    Add item to cart
    @param Item
    '''
    def add(self, item):
        if (type(item) is Item) and (item.getSku() in self.items.keys()):
            self.items[item.getSku()]['count'] += 1
        else:
            self.items[item.getSku()] = {'count' : 1, 'item' : item}

    '''
    @param string sku
    '''
    def remove(self, sku):
        ret = self.items[sku]
        del self.items[sku]
        return ret

    '''
     Get number of items in cart
     @return int
    '''
    def count(self):
        count = 0
        for key, val in self.items.items():
            count += val['count']

        return count

    '''
    Get total
    @return int
    '''
    def total(self):
        total = 0
        for key,val in self.items.items():
            total += (val['count'] * val['item'].getPrice())

        return total

    '''
    Get an item
    @param string sku
    @return Item
    '''
    def getItem(self, sku):
        return self.items[sku]['item']
