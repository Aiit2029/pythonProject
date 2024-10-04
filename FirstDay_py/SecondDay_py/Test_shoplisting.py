import unittest
from FirstDay_py.SecondDay_py.shoplist_demo import ShopList


class TestShopListing(unittest.TestCase):
    def setUp(self):
        self.shoplisting = ShopList({'蛋糕': 20, '牛奶': 3, '牙膏': 5, '拖鞋': 10})

    def test_get_shoplist_count(self):
        self.assertEqual(self.shoplisting.get_shoplist_count(), 4)

    def test_get_shoplisting_price(self):
        self.assertEqual(self.shoplisting.get_shoplisting_price(), 38)
