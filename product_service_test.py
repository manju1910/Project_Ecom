import unittest
from DAO import ProductService
from Entity.product import Product


class TestProductServiceModule(unittest.TestCase):
    # Setup: Arrange
    def setUp(self):
        self.product_service = ProductService()

    def test_add_product(self):
        name='broom'
        price=50
        description='kalimark broom'
        stock_quantity=30
        new_product = Product(name, price, description, stock_quantity)
        created_product = self.product_service.createProduct(new_product)
        self.assertTrue(created_product)


if __name__ == "__main__":
    unittest.main()
