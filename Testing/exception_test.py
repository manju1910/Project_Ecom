import unittest
import sys
sys.path.append('C:\Users\Manju\Desktop\Project_Ecom')

from DAO import CustomerService,ProductService
from Entity.customer import Customer
from Entity.product import Product


class TestException(unittest.TestCase):

    def setUp(self):
        self.customer_service = CustomerService()
        self.product_service = ProductService()

    def test_customer_id(self):
        customer_id=10002
        customer= self.customer_service.Check_customerid(customer_id)
        self.assertIsNotNone(customer)

    def test_product_id(self):
        product_id=20002
        product= self.product_service.Check_productid(product_id)
        self.assertIsNotNone(product)
 


if __name__ == "__main__":
    unittest.main()
