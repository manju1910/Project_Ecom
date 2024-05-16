create database Ecom_application
use Ecom_application


CREATE TABLE Customer (
    customer_id INT PRIMARY KEY identity(10001,1),
    name VARCHAR(100),
    email VARCHAR(255),
    password VARCHAR(50)
);


CREATE TABLE Cart (
    cart_id INT PRIMARY KEY identity(30001,1),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Product (
    product_id INT PRIMARY KEY identity(20001,1),
    name VARCHAR(255),
    price INT,
    description VARCHAR(100),
    stock_quantity INT
);

CREATE TABLE Cart_items (
    cart_item_id INT PRIMARY KEY identity(31001,1),
    cart_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);


CREATE TABLE orders (
    order_id INT PRIMARY KEY identity(40001,1),
    customer_id INT,
    order_date VARCHAR(20),
    total_price INT,
    shipping_address VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);


CREATE TABLE Order_items (
    order_item_id INT PRIMARY KEY identity(41001,1),
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- Inserting values into the Customer table
INSERT INTO Customer ( name, email, password) VALUES
( 'John Doe', 'john@example.com', 'password123'),
( 'Jane Smith', 'jane@example.com', 'qwerty'),
( 'Alice Johnson', 'alice@example.com', 'securepass'),
( 'Bob Brown', 'bob@example.com', '123456'),
( 'Emily Davis', 'emily@example.com', 'password123');

-- Inserting values into the Cart table
INSERT INTO Cart ( customer_id) VALUES
( 10001),
( 10002),
( 10003),
( 10004),
( 10005);

-- Inserting values into the Product table
INSERT INTO Product ( name, price, description, stock_quantity) VALUES
( 'Laptop', 1000, 'High_performance_laptop', 10),
( 'Smartphone', 500, 'Latest_smartphone_model', 20),
( 'Headphones', 50, 'Noise-canceling_headphones', 30),
( 'Mouse', 20, 'Wireless_mouse', 40),
( 'Keyboard', 30, 'Mechanical_keyboard', 50);

-- Inserting values into the Cart_items table
INSERT INTO Cart_items ( cart_id, product_id, quantity) VALUES
( 30001, 20001, 2),
( 30001, 20002, 1),
( 30002, 20003, 3),
( 30003, 20004, 2),
( 30004, 20005, 1);

-- Inserting values into the orders table
INSERT INTO orders (customer_id, order_date, total_price, shipping_address) VALUES
( 10001, '2024-05-10', 2500, 'India'),
( 10002, '2024-05-10', 150, 'Srilanka'),
( 10003, '2024-05-10', 100, 'Canada'),
( 10004, '2024-05-10', 40, 'India'),
( 10005, '2024-05-10', 30, 'Malaysia');

-- Inserting values into the Order_items table
INSERT INTO Order_items ( order_id, product_id, quantity) VALUES
( 40001, 20001, 1),
( 40001, 20002, 1),
( 40002, 20003, 2),
( 40003, 20004, 1),
( 40004, 20005, 1);

