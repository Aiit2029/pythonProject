class ShopList(object):
    def __init__(self,shoplisting):
        self.shoplisting = shoplisting

    def get_shoplist_count(self):
        return len(self.shoplisting)

    def get_shoplisting_price(self):
        total_price = 0
        for price in self.shoplisting.values():
            total_price += price
        return total_price
