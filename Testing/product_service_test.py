import unittest
import sys
sys.path.append('C:\Users\Manju\Desktop\Project_Ecom')

from DAO import ProductService
from Entity.product import Product


class TestProductServiceModule(unittest.TestCase):

    def setUp(self):
        self.product_service = ProductService()

    def test_add_product(self):
        name='broom'
        price=50
        description='kalimark broom'
        stock_quantity=30
        #new_product = Product(name, price, description, stock_quantity)
        created_product = self.product_service.createProduct(name, price, description, stock_quantity)
        self.assertTrue(created_product)

    def test_display_product(self):
        product = self.product_service.display_product()
        self.assertIsNotNone(product)
        self.assertGreater(len(product), 0)   


if __name__ == "__main__":
    unittest.main()
