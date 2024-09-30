import unittest
from unittest.mock import patch
from Creational import Shop  
class TestShopSingleton(unittest.TestCase):
    
    @patch.object(Shop, 'add_product')
    def test_add_product_using_mock(self, mock_add_product):
        shop = Shop()
        mock_add_product("Bananas")
        mock_add_product("Apples")
        self.assertEqual(mock_add_product.call_count, 2)
        shop.add_product("Bananas")
        shop.add_product("Apples")

        self.assertIn("Bananas", shop.get_books())
        self.assertIn("Apples", shop.get_books())

    def test_singleton_property(self):
        shop1 = Shop()
        shop2 = Shop()
        shop1.add_product("Grapes")
        self.assertIs(shop1, shop2)
        self.assertIn("Grapes", shop2.get_books())

unittest.main()
