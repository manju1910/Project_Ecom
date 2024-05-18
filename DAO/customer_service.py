from tabulate import tabulate
from MyException.customer_exception import CustomerNotFoundException
from Utility.DBconn import DBconnection
from Interface import ICustomerService

class CustomerService(DBconnection,ICustomerService):

    def display_customer(self):
        try:
            self.cursor.execute("Select * from Customer")
            cust = self.cursor.fetchall() # Get all data
            headers = [column [0] for column in self.cursor.description]
            print(tabulate (cust, headers=headers, tablefmt="psql"))
        except Exception as e:
            print(e)


    def create_customer(self,customer_name,customer_email,customer_password):
        try:
            self.cursor.execute(
                """INSERT INTO customer (name, email, password) VALUES ( ?, ?, ?)
                declare @a int = (select max(customer_id) from customer)
                insert into cart (customer_id)
                values (@a)   """,
                (customer_name,customer_email,customer_password)
            )
            self.conn.commit()  
            print("Customer registered successfully.....")
        except Exception as e:
            print(e)
  
            

    def delete_customer(self,customer_id):
        rows_deleted = self.cursor.execute(
            """declare @a int = ?;
                    delete from Order_items
                    where order_id= (select order_id
                                    from orders
                                    where customer_id=@a)
                    delete from orders
                    where customer_id=@a

                    delete from Cart_items
                    where cart_id = (select cart_id
                                    from Cart
                                    where customer_id=@a)

                    delete from Cart
                    where customer_id=@a

                    delete from customer
                    where customer_id= @a
            """,
            (customer_id)
        ).rowcount
        self.conn.commit()
        try: 
            if rows_deleted == 0:
                raise CustomerNotFoundException(customer_id)
        except CustomerNotFoundException as e:
            print(e)


    def check_customerid(self,customer_id):
        self.cursor.execute("""
        select customer_id from Customer
        where customer_id= ? """,(customer_id)
        )
        row=self.cursor.fetchall()
        order_list = [ro[0] for ro in row]
        try:
            if len(order_list)==0:
                raise CustomerNotFoundException(customer_id)
        except CustomerNotFoundException as e:
            print(e)
        finally:
            return len(order_list)
                            