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