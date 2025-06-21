import unittest
from model import Product, ProductsList

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.product = Product('iphone 15 pro', 'apple', '999', '4.9')
        self.other_product = Product('galaxy s', 'samsung', '900', '4.0')
        self.products_list = ProductsList()
        self.products_list.products_list = [self.product, self.other_product]
    
    def test_init_product(self):
        self.assertEqual(self.product.product_dict,  {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'})

    def test_get_where(self):
        self.assertEqual(self.products_list.get_where('brand=apple'),  [self.product])
        self.assertEqual(self.products_list.get_where('brand=samsung'),  [self.other_product])
        self.assertEqual(self.products_list.get_where('price>950'),  [self.product])
        self.assertEqual(self.products_list.get_where('price<950'),  [self.other_product])

    
    def test_get_aggregate(self):
        self.assertEqual(self.products_list.get_aggregate('rating=max', [self.product, self.other_product]),  ['max', 4.9])
        self.assertEqual(self.products_list.get_aggregate('rating=min', [self.product, self.other_product]),  ['min', 4.0])
        self.assertEqual(self.products_list.get_aggregate('rating=avg', [self.product, self.other_product]),  ['avg', 4.45])

    def test_execute(self):
        self.assertEqual(self.products_list.execute(),  [self.product, self.other_product])
        self.assertEqual(self.products_list.execute(where='price>950'),  [self.product])
        self.assertEqual(self.products_list.execute(where='price>950', aggregate='rating=max'),  ['max', 4.9])

if __name__ == '__main__':
    unittest.main()