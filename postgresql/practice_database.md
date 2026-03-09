**making ecommerce database and tables:**
```bash
postgres=# CREATE DATABASE ecommerce_db
postgres-# ;
CREATE DATABASE
postgres=# \c ecommerce_db 
You are now connected to database "ecommerce_db" as user "postgres".
ecommerce_db=# create table customers(
ecommerce_db(# customer_id int primary key,
ecommerce_db(# name varchar(100),
ecommerce_db(# email varchar(100),
ecommerce_db(# city varchar(50)
ecommerce_db(# );
CREATE TABLE
ecommerce_db=# create table categories(
ecommerce_db(# category_id int primary key,
ecommerce_db(# category_name varchar(100)
ecommerce_db(# );
CREATE TABLE
ecommerce_db=# create table products(
ecommerce_db(# product_id int primary key,
ecommerce_db(# product_name varchar(100),
ecommerce_db(# category_id int,
ecommerce_db(# price int,
ecommerce_db(# foreign key (category_id) references categories(category_id)
ecommerce_db(# );
CREATE TABLE
ecommerce_db=# create table orders(
ecommerce_db(# order_id int primary key,
ecommerce_db(# customer_id int,
ecommerce_db(# order_date date,
ecommerce_db(# foreign key (customer_id) references customers(customer_id)
ecommerce_db(# );
CREATE TABLE
ecommerce_db=# create table order_items(
ecommerce_db(# order_item_id int primary key,
ecommerce_db(# order_id int,
ecommerce_db(# product_id int,
ecommerce_db(# quantity int,
ecommerce_db(# foreign key (order_id) references orders(order_id),
ecommerce_db(# foreign key (product_id) references products(product_id)
ecommerce_db(# );
CREATE TABLE
ecommerce_db=# create table payments(
ecommerce_db(# payment_id int primary key,
ecommerce_db(# order_id int,
ecommerce_db(# payment_method varchar(50),
ecommerce_db(# amount int,
ecommerce_db(# foreign key (order_id) references orders(order_id)
ecommerce_db(# );
CREATE TABLE
ecommerce_db=# create table suppliers(
ecommerce_db(# supplier_id int primary key,
ecommerce_db(# supplier_name varchar(100),
ecommerce_db(# city varchar(50)
ecommerce_db(# );
CREATE TABLE
ecommerce_db=# create table product_suppliers(
ecommerce_db(# id int primary key,
ecommerce_db(# product_id int,
ecommerce_db(# supplier_id int,
ecommerce_db(# foreign key (product_id) references products(product_id),
ecommerce_db(# foreign key (supplier_id) references suppliers(supplier_id)
ecommerce_db(# );
CREATE TABLE
ecommerce_db=# \dt
               List of relations
 Schema |       Name        | Type  |  Owner   
--------+-------------------+-------+----------
 public | categories        | table | postgres
 public | customers         | table | postgres
 public | order_items       | table | postgres
 public | orders            | table | postgres
 public | payments          | table | postgres
 public | product_suppliers | table | postgres
 public | products          | table | postgres
 public | suppliers         | table | postgres
(8 rows)
```
1. Show all customers
```bash
ecommerce_db=# select * from customers ;
 customer_id |  name  |      email       |   city    
-------------+--------+------------------+-----------
           1 | Rahul  | rahul@gmail.com  | Delhi
           2 | Anita  | anita@gmail.com  | Mumbai
           3 | Vikas  | vikas@gmail.com  | Pune
           4 | Priya  | priya@gmail.com  | Bangalore
           5 | Amit   | amit@gmail.com   | Hyderabad
           6 | Neha   | neha@gmail.com   | Chennai
           7 | Karan  | karan@gmail.com  | Delhi
           8 | Sneha  | sneha@gmail.com  | Pune
           9 | Rohit  | rohit@gmail.com  | Mumbai
          10 | Pooja  | pooja@gmail.com  | Delhi
          11 | Arjun  | arjun@gmail.com  | Bangalore
          12 | Simran | simran@gmail.com | Chennai
          13 | Manish | manish@gmail.com | Hyderabad
          14 | Divya  | divya@gmail.com  | Kolkata
          15 | Nikhil | nikhil@gmail.com | Pune
          16 | Megha  | megha@gmail.com  | Mumbai
          17 | Yash   | yash@gmail.com   | Delhi
          18 | Sonal  | sonal@gmail.com  | Bangalore
          19 | Varun  | varun@gmail.com  | Hyderabad
          20 | Riya   | riya@gmail.com   | Pune
          21 | Deepak | deepak@gmail.com | Delhi
          22 | Tina   | tina@gmail.com   | Mumbai
          23 | Harsh  | harsh@gmail.com  | Chennai
          24 | Kavya  | kavya@gmail.com  | Bangalore
          25 | Aditya | aditya@gmail.com | Hyderabad
(25 rows)
```
2. Show all products with price greater than 5000.
```bash
ecommerce_db=# select product_name,price from products where price>5000;
  product_name  | price 
----------------+-------
 Laptop         | 60000
 Mobile         | 30000
 Microwave      |  8000
 Sofa           | 25000
 Dining Table   | 18000
 Tablet         | 20000
 Air Fryer      |  7000
 Vacuum Cleaner |  9000
(8 rows)
```
3. Show all customers who live in Delhi.
```bash
ecommerce_db=# select name,city from customers
ecommerce_db-# where city='Delhi';
  name  | city  
--------+-------
 Rahul  | Delhi
 Karan  | Delhi
 Pooja  | Delhi
 Yash   | Delhi
 Deepak | Delhi
(5 rows)
```
4. Show product name and price sorted by price in descending order.
```bash
ecommerce_db=# select product_name,price
ecommerce_db-# from products 
ecommerce_db-# order by price desc;
   product_name    | price 
-------------------+-------
 Laptop            | 60000
 Mobile            | 30000
 Sofa              | 25000
 Tablet            | 20000
 Dining Table      | 18000
 Vacuum Cleaner    |  9000
 Microwave         |  8000
 Air Fryer         |  7000
 Smart Watch       |  5000
 Mixer Grinder     |  3500
 Sneakers          |  3500
 Jacket            |  3000
 Cricket Bat       |  2500
 Headphones        |  2000
 Jeans             |  1500
 Perfume           |  1500
 Basketball        |  1300
 Football          |  1200
 Toy Car           |   900
 T-Shirt           |   800
 Data Science Book |   800
 Teddy Bear        |   700
 Python Book       |   650
 Face Cream        |   600
 SQL Book          |   500
(25 rows)
```
5. Show all products that belong to the Electronics category.
```bash
ecommerce_db=# select product_name
ecommerce_db-# from products p
ecommerce_db-# join categories c
ecommerce_db-# on p.category_id = c.category_id
ecommerce_db-# where category_name = 'Electronics'
ecommerce_db-# ;
 product_name 
--------------
 Laptop
 Mobile
 Headphones
 Tablet
 Smart Watch
(5 rows)
```
6. Show all orders placed after 2024-02-10
```bash
ecommerce_db=# select * from orders 
where order_date > '2024-02-10'
;
 order_id | customer_id | order_date 
----------+-------------+------------
       13 |          13 | 2024-02-11
       14 |          14 | 2024-02-12
       15 |          15 | 2024-02-14
       16 |          16 | 2024-02-16
       17 |          17 | 2024-02-18
       18 |          18 | 2024-02-20
       19 |          19 | 2024-02-21
       20 |          20 | 2024-02-22
       21 |          21 | 2024-02-23
       22 |          22 | 2024-02-24
       23 |          23 | 2024-02-25
       24 |          24 | 2024-02-26
       25 |          25 | 2024-02-27
(13 rows)
```
7. Show distinct cities from customers table
```bash
ecommerce_db=# select distinct city
ecommerce_db-# from customers ;
   city    
-----------
 Mumbai
 Pune
 Delhi
 Chennai
 Hyderabad
 Bangalore
 Kolkata
(7 rows)
```
8. Show top 5 most expensive products
```bash
ecommerce_db=# select product_name,price
ecommerce_db-# from products 
ecommerce_db-# order by price desc
ecommerce_db-# limit 5;
 product_name | price 
--------------+-------
 Laptop       | 60000
 Mobile       | 30000
 Sofa         | 25000
 Tablet       | 20000
 Dining Table | 18000
(5 rows)
```
9. Show product name and category name
```bash
ecommerce_db=# select product_name, category_name 
ecommerce_db-# from categories c
ecommerce_db-# join products p
ecommerce_db-# on p.category_id = c.category_id;
   product_name    |  category_name  
-------------------+-----------------
 Laptop            | Electronics
 Mobile            | Electronics
 Headphones        | Electronics
 T-Shirt           | Clothing
 Jeans             | Clothing
 SQL Book          | Books
 Mixer Grinder     | Home Appliances
 Microwave         | Home Appliances
 Football          | Sports
 Cricket Bat       | Sports
 Face Cream        | Beauty
 Perfume           | Beauty
 Sofa              | Furniture
 Dining Table      | Furniture
 Teddy Bear        | Toys
 Toy Car           | Toys
 Tablet            | Electronics
 Smart Watch       | Electronics
 Jacket            | Clothing
 Sneakers          | Clothing
 Data Science Book | Books
 Python Book       | Books
 Air Fryer         | Home Appliances
 Vacuum Cleaner    | Home Appliances
 Basketball        | Sports
(25 rows)
```
10. Show customer name and their order date
```bash
ecommerce_db=# select c.name,o.order_date from customers c
ecommerce_db-# join orders o on c.customer_id = o.customer_id;
  name  | order_date 
--------+------------
 Rahul  | 2024-01-10
 Anita  | 2024-01-12
 Vikas  | 2024-01-15
 Priya  | 2024-01-18
 Amit   | 2024-01-20
 Rahul  | 2024-01-25
 Karan  | 2024-02-01
 Sneha  | 2024-02-03
 Rohit  | 2024-02-05
 Pooja  | 2024-02-07
 Arjun  | 2024-02-08
 Simran | 2024-02-10
 Manish | 2024-02-11
 Divya  | 2024-02-12
 Nikhil | 2024-02-14
 Megha  | 2024-02-16
 Yash   | 2024-02-18
 Sonal  | 2024-02-20
 Varun  | 2024-02-21
 Riya   | 2024-02-22
 Deepak | 2024-02-23
 Tina   | 2024-02-24
 Harsh  | 2024-02-25
 Kavya  | 2024-02-26
 Aditya | 2024-02-27
(25 rows)
```
11. Show customer name and payment method used
```bash
ecommerce_db=# select c.name,p.payment_method
from customers c
join orders o on c.customer_id = o.customer_id
join payments p on o.order_id = p.order_id;
  name  | payment_method 
--------+----------------
 Rahul  | UPI
 Anita  | Credit Card
 Vikas  | Debit Card
 Priya  | UPI
 Amit   | Net Banking
 Rahul  | UPI
 Karan  | UPI
 Sneha  | Credit Card
 Rohit  | Debit Card
 Pooja  | UPI
 Arjun  | Net Banking
 Simran | UPI
 Manish | Debit Card
 Divya  | UPI
 Nikhil | Credit Card
 Megha  | UPI
 Yash   | UPI
 Sonal  | Debit Card
 Varun  | Credit Card
 Riya   | UPI
 Deepak | Net Banking
 Tina   | UPI
 Harsh  | Debit Card
 Kavya  | UPI
 Aditya | Credit Card
(25 rows)
```
12. Show order_id, product_name, and quantity for all orders
```bash
ecommerce_db=# select oi.order_id,p.product_name,oi.quantity
ecommerce_db-# FROM orders o
ecommerce_db-# JOIN order_items oi ON o.order_id = oi.order_id
ecommerce_db-# JOIN products p ON oi.product_id = p.product_id;
 order_id |   product_name    | quantity 
----------+-------------------+----------
        1 | Laptop            |        1
        1 | Headphones        |        2
        2 | Mobile            |        1
        2 | T-Shirt           |        3
        3 | SQL Book          |        2
        3 | Jeans             |        1
        4 | Mixer Grinder     |        1
        5 | Microwave         |        1
        6 | Mobile            |        1
        6 | SQL Book          |        1
        7 | Football          |        2
        7 | Headphones        |        1
        8 | Cricket Bat       |        1
        9 | Face Cream        |        3
       10 | Perfume           |        1
       11 | Sofa              |        1
       12 | Teddy Bear        |        2
       13 | Toy Car           |        1
       14 | Tablet            |        1
       15 | Smart Watch       |        1
       16 | Jacket            |        2
       17 | Sneakers          |        1
       18 | Data Science Book |        1
       19 | Python Book       |        2
       20 | Air Fryer         |        1
       21 | Vacuum Cleaner    |        1
       22 | Basketball        |        2
       23 | Dining Table      |        1
       24 | Football          |        1
       25 | Cricket Bat       |        1
(30 rows)
```
13. 