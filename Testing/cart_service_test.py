import unittest
import sys
sys.path.append('C:\Users\Manju\Desktop\Project_Ecom')

from DAO import CartService
from Entity.cart import Cart


class TestCartServiceModule(unittest.TestCase):

    def setUp(self):
        self.cart_service = CartService()

    def test_add_to_cart(self):
        customer_id=10004
        prod_id=20003
        quantity=5
        added_product = self.cart_service.Add_to_cart(customer_id,prod_id,quantity)
        self.assertTrue(added_product)
 


if __name__ == "__main__":
    unittest.main()
