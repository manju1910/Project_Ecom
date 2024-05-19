from abc import ABC,abstractmethod

class IOrderService(ABC):

    @abstractmethod
    def PlaceOrder(self,customer_id, pq_list, shippingAddress):
        pass

    @abstractmethod
    def GetOrdersByCustomer(self,customer_id):
        pass
