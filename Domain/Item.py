class Item(object):

    '''
      initialize object
    '''
    def __init__(self, name, sku, price, desr=''):
        self._name = name
        self._sku = sku
        self._desr = desr
        self._price = price

    '''
      Get item name
    '''
    def getName(self):
        return self._name

    '''
      Get SKU number
    '''
    def getSku(self):
        return self._sku

    '''
      Get item description
    '''
    def getDesr(self):
        return self._desr

    '''
     Get price
    '''
    def getPrice(self):
        return self._price
