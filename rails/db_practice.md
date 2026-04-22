```bash
ecommerce-app(dev):003> user.orders
  Order Load (4.5ms)  SELECT "orders".* FROM "orders" WHERE "orders"."user_id" = 1 /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Order:0x00007569c7e65950
  id: 60,
  user_id: 1,
  total_price: 25357,
  created_at: "2026-04-17 07:09:58.224997000 +0000",
  updated_at: "2026-04-17 07:09:58.224997000 +0000">]
ecommerce-app(dev):004> user.orders.size
  Order Count (2.9ms)  SELECT COUNT(*) FROM "orders" WHERE "orders"."user_id" = 1 /*application='EcommerceApp'*/
=> 1
ecommerce-app(dev):005> user = User.all
  User Load (1.6ms)  SELECT "users".* FROM "users" /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<User:0x00007569c70ee600
...
ecommerce-app(dev):006> user.orders
(ecommerce-app):6:in `<main>': undefined method `orders' for an instance of ActiveRecord::Relation (NoMethodError)
Did you mean?  order
               order!
ecommerce-app(dev):007> user.order
(ecommerce-app):7:in `<main>': The method .order() must contain arguments. (ArgumentError)

          raise ArgumentError, message || "The method .#{method_name}() must contain arguments."
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ecommerce-app(dev):008> user.order!
  User Load (1.5ms)  SELECT "users".* FROM "users" /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<User:0x00007569c70edd40
  id: 1,
  name: "Amit Sharma",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.090495000 +0000",
  updated_at: "2026-04-17 07:06:46.090495000 +0000">,
 #<User:0x00007569c70edc00
  id: 2,
Preparing full inspection value...
=> 
[#<User:0x00007569c70edd40
  id: 1,
  name: "Amit Sharma",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.090495000 +0000",
  updated_at: "2026-04-17 07:06:46.090495000 +0000">,
 #<User:0x00007569c70edc00
  id: 2,
  name: "Rahul Verma",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.111736000 +0000",
  updated_at: "2026-04-17 07:06:46.111736000 +0000">,
 #<User:0x00007569c70edac0
  id: 3,
  name: "Neha Singh",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.132084000 +0000",
  updated_at: "2026-04-17 07:06:46.132084000 +0000">,
 #<User:0x00007569c70ed980
  id: 4,
  name: "Priya Sharma",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.151035000 +0000",
  updated_at: "2026-04-17 07:06:46.151035000 +0000">,
 #<User:0x00007569c70ed840
  id: 5,
  name: "Rohit Gupta",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.167137000 +0000",
  updated_at: "2026-04-17 07:06:46.167137000 +0000">,
 #<User:0x00007569c70ed700
  id: 6,
  name: "Anjali Verma",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.182574000 +0000",
  updated_at: "2026-04-17 07:06:46.182574000 +0000">,
 #<User:0x00007569c70ed480
  id: 7,
  name: "Vikas Yadav",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.202076000 +0000",
  updated_at: "2026-04-17 07:06:46.202076000 +0000">,
 #<User:0x00007569c70ed340
  id: 8,
  name: "Sneha Kapoor",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.221633000 +0000",
  updated_at: "2026-04-17 07:06:46.221633000 +0000">,
 #<User:0x00007569c70ed200
  id: 9,
  name: "Arjun Mehta",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.240909000 +0000",
  updated_at: "2026-04-17 07:06:46.240909000 +0000">,
 #<User:0x00007569c70ed0c0
  id: 10,
  name: "Pooja Singh",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.254640000 +0000",
  updated_at: "2026-04-17 07:06:46.254640000 +0000">,
 "..."]
ecommerce-app(dev):009> user.order!.count
  User Count (1.5ms)  SELECT COUNT(*) FROM "users" /*application='EcommerceApp'*/
=> 50
ecommerce-app(dev):010> user = User.take
  User Load (225.9ms)  SELECT "users".* FROM "users" LIMIT 1 /*application='EcommerceApp'*/
=> 
#<User:0x00007569c70ef500
...
ecommerce-app(dev):011> user
=> 
#<User:0x00007569c70ef500
 id: 1,
 name: "Amit Sharma",
 email: "[FILTERED]",
 created_at: "2026-04-17 07:06:46.090495000 +0000",
 updated_at: "2026-04-17 07:06:46.090495000 +0000">
ecommerce-app(dev):012> user.email
=> "amit.sharma@gmail.com"
ecommerce-app(dev):013> User.take(2)
  User Load (213.4ms)  SELECT "users".* FROM "users" LIMIT 2 /*application='EcommerceApp'*/
=> 
[#<User:0x00007569c70eadc0
  id: 1,
  name: "Amit Sharma",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.090495000 +0000",
  updated_at: "2026-04-17 07:06:46.090495000 +0000">,
 #<User:0x00007569c70eac80
  id: 2,
  name: "Rahul Verma",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.111736000 +0000",
  updated_at: "2026-04-17 07:06:46.111736000 +0000">]
ecommerce-app(dev):014> User.order(:name).first
  User Load (2.9ms)  SELECT "users".* FROM "users" ORDER BY "users"."name" ASC LIMIT 1 /*application='EcommerceApp'*/
=> 
#<User:0x00007569c70eed80
 id: 47,
 name: "Aarti Gupta",
 email: "[FILTERED]",
 created_at: "2026-04-17 07:06:46.925480000 +0000",
 updated_at: "2026-04-17 07:06:46.925480000 +0000">
ecommerce-app(dev):015> User.first!
  User Load (2.6ms)  SELECT "users".* FROM "users" ORDER BY "users"."id" ASC LIMIT 1 /*application='EcommerceApp'*/
=> 
#<User:0x00007569c70ea500
 id: 1,
 name: "Amit Sharma",
 email: "[FILTERED]",
 created_at: "2026-04-17 07:06:46.090495000 +0000",
 updated_at: "2026-04-17 07:06:46.090495000 +0000">
ecommerce-app(dev):016> Review.first
  Review Load (3.5ms)  SELECT "reviews".* FROM "reviews" ORDER BY "reviews"."id" ASC LIMIT 1 /*application='EcommerceApp'*/
=> nil
ecommerce-app(dev):017> User.find_by name: 'Amit'
  User Load (3.8ms)  SELECT "users".* FROM "users" WHERE "users"."name" = 'Amit' LIMIT 1 /*application='EcommerceApp'*/
=> nil
ecommerce-app(dev):018> User.find_by name: 'Amit Sharma'
  User Load (2.1ms)  SELECT "users".* FROM "users" WHERE "users"."name" = 'Amit Sharma' LIMIT 1 /*application='EcommerceApp'*/
=> 
#<User:0x00007569c70e4c40
 id: 1,
 name: "Amit Sharma",
 email: "[FILTERED]",
 created_at: "2026-04-17 07:06:46.090495000 +0000",
 updated_at: "2026-04-17 07:06:46.090495000 +0000">
ecommerce-app(dev):019> Product.where("price>1000")
  Product Load (217.4ms)  SELECT "products".* FROM "products" WHERE (price>1000) /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Product:0x00007569c7099c68
  id: 1,
  name: "iPhone 13",
  price: 65000,
  created_at: "2026-04-17 07:07:23.728614000 +0000",
  updated_at: "2026-04-17 07:07:23.728614000 +0000",
  stock: 10,
  category_id: 1>,
Preparing full inspection value...
=> 
[#<Product:0x00007569c7099c68
  id: 1,
  name: "iPhone 13",
  price: 65000,
  created_at: "2026-04-17 07:07:23.728614000 +0000",
  updated_at: "2026-04-17 07:07:23.728614000 +0000",
  stock: 10,
  category_id: 1>,
 #<Product:0x00007569c70e6cc0
  id: 2,
  name: "Samsung Galaxy S23",
  price: 70000,
  created_at: "2026-04-17 07:07:23.752128000 +0000",
  updated_at: "2026-04-17 07:07:23.752128000 +0000",
  stock: 8,
  category_id: 1>,
 #<Product:0x00007569c70e6b80
  id: 3,
  name: "OnePlus 11",
  price: 55000,
  created_at: "2026-04-17 07:07:23.771580000 +0000",
  updated_at: "2026-04-17 07:07:23.771580000 +0000",
  stock: 12,
  category_id: 1>,
 #<Product:0x00007569c70e6a40
  id: 4,
  name: "MacBook Air",
  price: 90000,
  created_at: "2026-04-17 07:07:23.797392000 +0000",
  updated_at: "2026-04-17 07:07:23.797392000 +0000",
  stock: 5,
  category_id: 1>,
 #<Product:0x00007569c70e6900
  id: 5,
  name: "Dell Inspiron Laptop",
  price: 75000,
  created_at: "2026-04-17 07:07:23.813411000 +0000",
  updated_at: "2026-04-17 07:07:23.813411000 +0000",
  stock: 6,
  category_id: 1>,
 #<Product:0x00007569c70e67c0
  id: 6,
  name: "Nike Running Shoes",
  price: 5000,
  created_at: "2026-04-17 07:07:23.831115000 +0000",
  updated_at: "2026-04-17 07:07:23.831115000 +0000",
  stock: 20,
  category_id: 2>,
 #<Product:0x00007569c70e6680
  id: 7,
  name: "Adidas Sneakers",
  price: 4500,
  created_at: "2026-04-17 07:07:23.854069000 +0000",
  updated_at: "2026-04-17 07:07:23.854069000 +0000",
  stock: 25,
  category_id: 2>,
 #<Product:0x00007569c70e6540
  id: 8,
  name: "Levi's Jeans",
  price: 2000,
  created_at: "2026-04-17 07:07:23.883451000 +0000",
  updated_at: "2026-04-17 07:07:23.883451000 +0000",
  stock: 30,
  category_id: 2>,
 #<Product:0x00007569c70e6400
  id: 10,
  name: "Puma Hoodie",
  price: 1500,
  created_at: "2026-04-17 07:07:23.931794000 +0000",
  updated_at: "2026-04-17 07:07:23.931794000 +0000",
  stock: 40,
  category_id: 2>,
 #<Product:0x00007569c70e62c0
  id: 11,
  name: "Sofa Set",
  price: 25000,
  created_at: "2026-04-17 07:07:23.953616000 +0000",
  updated_at: "2026-04-17 07:07:23.953616000 +0000",
  stock: 5,
  category_id: 3>,
 "..."]
ecommerce-app(dev):020> Product.where("price>1000").count
  Product Count (2.8ms)  SELECT COUNT(*) FROM "products" WHERE (price>1000) /*application='EcommerceApp'*/
=> 35
ecommerce-app(dev):021> Product.where("price<1000").count
  Product Count (1.8ms)  SELECT COUNT(*) FROM "products" WHERE (price<1000) /*application='EcommerceApp'*/
=> 10
ecommerce-app(dev):022> Product.where("price<1000")
  Product Load (2.3ms)  SELECT "products".* FROM "products" WHERE (price<1000) /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Product:0x00007569c70e7800
  id: 9,
  name: "H&M T-Shirt",
  price: 800,
  created_at: "2026-04-17 07:07:23.909232000 +0000",
  updated_at: "2026-04-17 07:07:23.909232000 +0000",
  stock: 50,
  category_id: 2>,
Preparing full inspection value...
=> 
[#<Product:0x00007569c70e7800
  id: 9,
  name: "H&M T-Shirt",
  price: 800,
  created_at: "2026-04-17 07:07:23.909232000 +0000",
  updated_at: "2026-04-17 07:07:23.909232000 +0000",
  stock: 50,
  category_id: 2>,
 #<Product:0x00007569c70e76c0
  id: 17,
  name: "Atomic Habits Book",
  price: 500,
  created_at: "2026-04-17 07:07:24.101451000 +0000",
  updated_at: "2026-04-17 07:07:24.101451000 +0000",
  stock: 60,
  category_id: 4>,
 #<Product:0x00007569c70e7440
  id: 18,
  name: "Rich Dad Poor Dad",
  price: 450,
  created_at: "2026-04-17 07:07:24.123633000 +0000",
  updated_at: "2026-04-17 07:07:24.123633000 +0000",
  stock: 70,
  category_id: 4>,
 #<Product:0x00007569c70e7300
  id: 20,
  name: "Football",
  price: 800,
  created_at: "2026-04-17 07:07:24.159415000 +0000",
  updated_at: "2026-04-17 07:07:24.159415000 +0000",
  stock: 40,
  category_id: 5>,
 #<Product:0x00007569c70e7080
  id: 21,
  name: "Yoga Mat",
  price: 600,
  created_at: "2026-04-17 07:07:24.177610000 +0000",
  updated_at: "2026-04-17 07:07:24.177610000 +0000",
  stock: 50,
  category_id: 5>,
 #<Product:0x00007569c70e6f40
  id: 23,
  name: "Lipstick Kit",
  price: 800,
  created_at: "2026-04-17 07:07:24.224860000 +0000",
  updated_at: "2026-04-17 07:07:24.224860000 +0000",
  stock: 40,
  category_id: 6>,
 #<Product:0x00007569c70e6cc0
  id: 24,
  name: "Face Cream",
  price: 500,
  created_at: "2026-04-17 07:07:24.245786000 +0000",
  updated_at: "2026-04-17 07:07:24.245786000 +0000",
  stock: 60,
  category_id: 6>,
 #<Product:0x00007569c70e6b80
  id: 26,
  name: "Shampoo",
  price: 300,
  created_at: "2026-04-17 07:07:24.287165000 +0000",
  updated_at: "2026-04-17 07:07:24.287165000 +0000",
  stock: 70,
  category_id: 6>,
 #<Product:0x00007569c70e6a40
  id: 27,
  name: "Kids Toy Car",
  price: 600,
  created_at: "2026-04-17 07:07:24.310379000 +0000",
  updated_at: "2026-04-17 07:07:24.310379000 +0000",
  stock: 40,
  category_id: 7>,
 #<Product:0x00007569c70e6900
  id: 37,
  name: "Water Bottle",
  price: 500,
  created_at: "2026-04-17 07:07:24.517883000 +0000",
  updated_at: "2026-04-17 07:07:24.517883000 +0000",
  stock: 60,
  category_id: 9>]
ecommerce-app(dev):023> User.where("name LIKE ?","Am%")
  User Load (2.9ms)  SELECT "users".* FROM "users" WHERE (name LIKE 'Am%') /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<User:0x00007569c70e62c0
  id: 1,
  name: "Amit Sharma",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.090495000 +0000",
  updated_at: "2026-04-17 07:06:46.090495000 +0000">]
ecommerce-app(dev):024> User.where("name LIKE ?","Ra")
  User Load (2.0ms)  SELECT "users".* FROM "users" WHERE (name LIKE 'Ra') /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> []
ecommerce-app(dev):025> User.where("name LIKE ?","R")
  User Load (2.2ms)  SELECT "users".* FROM "users" WHERE (name LIKE 'R') /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> []
ecommerce-app(dev):026> User.where("name LIKE ?","Ra%")
  User Load (2.5ms)  SELECT "users".* FROM "users" WHERE (name LIKE 'Ra%') /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<User:0x00007569c7f69608
  id: 2,
  name: "Rahul Verma",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.111736000 +0000",
  updated_at: "2026-04-17 07:06:46.111736000 +0000">,
 #<User:0x00007569c7f694c8
  id: 24,
  name: "Ravi Kumar",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.513068000 +0000",
  updated_at: "2026-04-17 07:06:46.513068000 +0000">,
 #<User:0x00007569c7f69388
  id: 40,
  name: "Radhika Sharma",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.798356000 +0000",
  updated_at: "2026-04-17 07:06:46.798356000 +0000">,
 #<User:0x00007569c7f69248
  id: 50,
  name: "Rashi Mehta",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.984387000 +0000",
  updated_at: "2026-04-17 07:06:46.984387000 +0000">]
ecommerce-app(dev):027> Order.where(created_at: 1.day.ago..Time.now)
  Order Load (4.9ms)  SELECT "orders".* FROM "orders" WHERE "orders"."created_at" BETWEEN '2026-04-20 11:20:21.213865' AND '2026-04-21 11:20:21.214419' /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> []
ecommerce-app(dev):028> Order.where(created_at: 5.day.ago..Time.now)
  Order Load (1.7ms)  SELECT "orders".* FROM "orders" WHERE "orders"."created_at" BETWEEN '2026-04-16 11:20:33.056316' AND '2026-04-21 11:20:33.056620' /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Order:0x00007569c79a0dc0
  id: 1,
  user_id: 24,
  total_price: 72357,
  created_at: "2026-04-17 07:09:56.562550000 +0000",
  updated_at: "2026-04-17 07:09:56.562550000 +0000">,
 #<Order:0x00007569c61e7f80
  id: 2,
Preparing full inspection value...
=> 
[#<Order:0x00007569c79a0dc0
  id: 1,
  user_id: 24,
  total_price: 72357,
  created_at: "2026-04-17 07:09:56.562550000 +0000",
  updated_at: "2026-04-17 07:09:56.562550000 +0000">,
 #<Order:0x00007569c61e7f80
  id: 2,
  user_id: 34,
  total_price: 31534,
ecommerce-app(dev):029> Order.where(created_at: 5.day.ago..Time.now).count
  Order Count (2.5ms)  SELECT COUNT(*) FROM "orders" WHERE "orders"."created_at" BETWEEN '2026-04-16 11:20:42.570499' AND '2026-04-21 11:20:42.570848' /*application='EcommerceApp'*/
=> 100
ecommerce-app(dev):030> Order.count
  Order Count (1.9ms)  SELECT COUNT(*) FROM "orders" /*application='EcommerceApp'*/
=> 100
ecommerce-app(dev):031> Order.where(total_price: 500.2000)
  Order Load (229.0ms)  SELECT "orders".* FROM "orders" WHERE "orders"."total_price" = 500 /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> []
ecommerce-app(dev):032> Order.where(total_price: 500..2000)
  Order Load (2.8ms)  SELECT "orders".* FROM "orders" WHERE "orders"."total_price" BETWEEN 500 AND 2000 /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Order:0x00007569c61e5a00
  id: 16,
  user_id: 21,
  total_price: 1701,
  created_at: "2026-04-17 07:09:56.990454000 +0000",
  updated_at: "2026-04-17 07:09:56.990454000 +0000">,
 #<Order:0x00007569c61e58c0
  id: 35,
  user_id: 23,
  total_price: 1984,
  created_at: "2026-04-17 07:09:57.540133000 +0000",
  updated_at: "2026-04-17 07:09:57.540133000 +0000">,
 #<Order:0x00007569c61e5780
  id: 49,
  user_id: 19,
  total_price: 1598,
  created_at: "2026-04-17 07:09:57.937269000 +0000",
  updated_at: "2026-04-17 07:09:57.937269000 +0000">]
ecommerce-app(dev):033> Product.where(price: 1000..)
  Product Load (3.7ms)  SELECT "products".* FROM "products" WHERE "products"."price" >= 1000 /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Product:0x00007569c61e3fc0
  id: 1,
  name: "iPhone 13",
  price: 65000,
  created_at: "2026-04-17 07:07:23.728614000 +0000",
  updated_at: "2026-04-17 07:07:23.728614000 +0000",
  stock: 10,
  category_id: 1>,
Preparing full inspection value...
=> 
[#<Product:0x00007569c61e3fc0
  id: 1,
  name: "iPhone 13",
  price: 65000,
  created_at: "2026-04-17 07:07:23.728614000 +0000",
  updated_at: "2026-04-17 07:07:23.728614000 +0000",
  stock: 10,
  category_id: 1>,
 #<Product:0x00007569c61e3e80
ecommerce-app(dev):034> Product.where(price: ..1000)
  Product Load (1.6ms)  SELECT "products".* FROM "products" WHERE "products"."price" <= 1000 /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Product:0x00007569c61e99c0
  id: 9,
  name: "H&M T-Shirt",
  price: 800,
  created_at: "2026-04-17 07:07:23.909232000 +0000",
  updated_at: "2026-04-17 07:07:23.909232000 +0000",
  stock: 50,
  category_id: 2>,
Preparing full inspection value...
=> 
[#<Product:0x00007569c61e99c0
  id: 9,
  name: "H&M T-Shirt",
  price: 800,
  created_at: "2026-04-17 07:07:23.909232000 +0000",
  updated_at: "2026-04-17 07:07:23.909232000 +0000",
  stock: 50,
  category_id: 2>,
 #<Product:0x00007569c61e9880
ecommerce-app(dev):001> Product.where(id: [1,11,21])
  Product Load (3.1ms)  SELECT "products".* FROM "products" WHERE "products"."id" IN (1, 11, 21) /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Product:0x00007c037043db28
  id: 1,
  name: "iPhone 13",
  price: 65000,
  created_at:
   "2026-04-17 07:07:23.728614000 +0000",
  updated_at:
   "2026-04-17 07:07:23.728614000 +0000",
  stock: 10,
:
=> 
[#<Product:0x00007c037043db28
  id: 1,
  name: "iPhone 13",
  price: 65000,
  created_at:
   "2026-04-17 07:07:23.728614000 +0000",
  updated_at:
   "2026-04-17 07:07:23.728614000 +0000",
  stock: 10,
ecommerce-app(dev):002> Order.where(user_id: [1,2])
  Order Load (2.6ms)  SELECT "orders".* FROM "orders" WHERE "orders"."user_id" IN (1, 2) /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Order:0x00007c03704ceba0
  id: 21,
  user_id: 2,
  total_price: 34953,
  created_at: "2026-04-17 07:09:57.149922000 +0000",
  updated_at: "2026-04-17 07:09:57.149922000 +0000">,
 #<Order:0x00007c0370117f98
  id: 60,
  user_id: 1,
  total_price: 25357,
  created_at: "2026-04-17 07:09:58.224997000 +0000",
  updated_at: "2026-04-17 07:09:58.224997000 +0000">,
 #<Order:0x00007c0370117e58
  id: 82,
  user_id: 2,
  total_price: 29592,
  created_at: "2026-04-17 07:09:58.780184000 +0000",
  updated_at: "2026-04-17 07:09:58.780184000 +0000">]
ecommerce-app(dev):003> Product.where.not(price: 10000)
  Product Load (2.4ms)  SELECT "products".* FROM "products" WHERE "products"."price" != 10000 /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Product:0x00007c03718ae260
  id: 1,
  name: "iPhone 13",
  price: 65000,
  created_at: "2026-04-17 07:07:23.728614000 +0000",
  updated_at: "2026-04-17 07:07:23.728614000 +0000",
  stock: 10,
  category_id: 1>,
Preparing full inspection value...
=> 
[#<Product:0x00007c03718ae260
  id: 1,
  name: "iPhone 13",
  price: 65000,
  created_at: "2026-04-17 07:07:23.728614000 +0000",
  updated_at: "2026-04-17 07:07:23.728614000 +0000",
  stock: 10,
  category_id: 1>,
 #<Product:0x00007c03718ae120
  id: 2,
  name: "Samsung Galaxy S23",
  price: 70000,
  created_at: "2026-04-17 07:07:23.752128000 +0000",
  updated_at: "2026-04-17 07:07:23.752128000 +0000",
  stock: 8,
  category_id: 1>,
 #<Product:0x00007c03718add60
  id: 3,
  name: "OnePlus 11",
  price: 55000,
  created_at: "2026-04-17 07:07:23.771580000 +0000",
  updated_at: "2026-04-17 07:07:23.771580000 +0000",
  stock: 12,
  category_id: 1>,
 #<Product:0x00007c03718adae0
  id: 4,
  name: "MacBook Air",
  price: 90000,
  created_at: "2026-04-17 07:07:23.797392000 +0000",
  updated_at: "2026-04-17 07:07:23.797392000 +0000",
  stock: 5,
  category_id: 1>,
 #<Product:0x00007c03718ad9a0
  id: 5,
  name: "Dell Inspiron Laptop",
  price: 75000,
  created_at: "2026-04-17 07:07:23.813411000 +0000",
  updated_at: "2026-04-17 07:07:23.813411000 +0000",
  stock: 6,
  category_id: 1>,
 #<Product:0x00007c03718ad720
  id: 6,
  name: "Nike Running Shoes",
  price: 5000,
  created_at: "2026-04-17 07:07:23.831115000 +0000",
  updated_at: "2026-04-17 07:07:23.831115000 +0000",
  stock: 20,
  category_id: 2>,
 #<Product:0x00007c03718ad360
  id: 7,
  name: "Adidas Sneakers",
  price: 4500,
  created_at: "2026-04-17 07:07:23.854069000 +0000",
  updated_at: "2026-04-17 07:07:23.854069000 +0000",
  stock: 25,
  category_id: 2>,
 #<Product:0x00007c03718ad220
  id: 8,
  name: "Levi's Jeans",
  price: 2000,
  created_at: "2026-04-17 07:07:23.883451000 +0000",
  updated_at: "2026-04-17 07:07:23.883451000 +0000",
  stock: 30,
  category_id: 2>,
 #<Product:0x00007c03718ace60
  id: 9,
  name: "H&M T-Shirt",
  price: 800,
  created_at: "2026-04-17 07:07:23.909232000 +0000",
  updated_at: "2026-04-17 07:07:23.909232000 +0000",
  stock: 50,
  category_id: 2>,
 #<Product:0x00007c03718acd20
  id: 10,
  name: "Puma Hoodie",
  price: 1500,
  created_at: "2026-04-17 07:07:23.931794000 +0000",
  updated_at: "2026-04-17 07:07:23.931794000 +0000",
  stock: 40,
  category_id: 2>,
 "..."]
ecommerce-app(dev):004> Product.where.not(price: 10000).count
  Product Count (1.8ms)  SELECT COUNT(*) FROM "products" WHERE "products"."price" != 10000 /*application='EcommerceApp'*/
=> 44
ecommerce-app(dev):005> Product.where.not(id: [1, 2, 3, 4, 5])
  Product Load (2.3ms)  SELECT "products".* FROM "products" WHERE "products"."id" NOT IN (1, 2, 3, 4, 5) /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Product:0x00007c03718abf60
  id: 6,
  name: "Nike Running Shoes",
  price: 5000,
  created_at: "2026-04-17 07:07:23.831115000 +0000",
  updated_at: "2026-04-17 07:07:23.831115000 +0000",
  stock: 20,
  category_id: 2>,
Preparing full inspection value...
=> 
[#<Product:0x00007c03718abf60
  id: 6,
  name: "Nike Running Shoes",
  price: 5000,
  created_at: "2026-04-17 07:07:23.831115000 +0000",
  updated_at: "2026-04-17 07:07:23.831115000 +0000",
  stock: 20,
  category_id: 2>,
 #<Product:0x00007c03718abba0
  id: 7,
  name: "Adidas Sneakers",
  price: 4500,
  created_at: "2026-04-17 07:07:23.854069000 +0000",
  updated_at: "2026-04-17 07:07:23.854069000 +0000",
  stock: 25,
  category_id: 2>,
 #<Product:0x00007c03718ab920
  id: 8,
  name: "Levi's Jeans",
  price: 2000,
  created_at: "2026-04-17 07:07:23.883451000 +0000",
  updated_at: "2026-04-17 07:07:23.883451000 +0000",
  stock: 30,
  category_id: 2>,
 #<Product:0x00007c03718ab6a0
  id: 9,
  name: "H&M T-Shirt",
  price: 800,
  created_at: "2026-04-17 07:07:23.909232000 +0000",
  updated_at: "2026-04-17 07:07:23.909232000 +0000",
  stock: 50,
  category_id: 2>,
 #<Product:0x00007c03718ab560
  id: 10,
  name: "Puma Hoodie",
  price: 1500,
  created_at: "2026-04-17 07:07:23.931794000 +0000",
  updated_at: "2026-04-17 07:07:23.931794000 +0000",
  stock: 40,
  category_id: 2>,
 #<Product:0x00007c03718ab2e0
  id: 11,
  name: "Sofa Set",
  price: 25000,
  created_at: "2026-04-17 07:07:23.953616000 +0000",
  updated_at: "2026-04-17 07:07:23.953616000 +0000",
  stock: 5,
  category_id: 3>,
 #<Product:0x00007c03718ab1a0
  id: 12,
  name: "Dining Table",
  price: 18000,
  created_at: "2026-04-17 07:07:23.979510000 +0000",
  updated_at: "2026-04-17 07:07:23.979510000 +0000",
  stock: 4,
  category_id: 3>,
 #<Product:0x00007c03718aa7a0
  id: 13,
  name: "Wooden Chair",
  price: 3000,
  created_at: "2026-04-17 07:07:24.015187000 +0000",
  updated_at: "2026-04-17 07:07:24.015187000 +0000",
  stock: 20,
  category_id: 3>,
 #<Product:0x00007c03718aa660
  id: 14,
  name: "Bed Frame",
  price: 30000,
  created_at: "2026-04-17 07:07:24.031482000 +0000",
  updated_at: "2026-04-17 07:07:24.031482000 +0000",
  stock: 3,
ecommerce-app(dev):006> Product.where.not(id: [1, 2, 3, 4, 5]).count
  Product Count (1.5ms)  SELECT COUNT(*) FROM "products" WHERE "products"."id" NOT IN (1, 2, 3, 4, 5) /*application='EcommerceApp'*/
=> 40
ecommerce-app(dev):007> User.where.not(email: "")
  User Load (2.9ms)  SELECT "users".* FROM "users" WHERE "users"."email" != '' /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<User:0x00007c03706cd8c0
  id: 1,
  name: "Amit Sharma",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.090495000 +0000",
  updated_at: "2026-04-17 07:06:46.090495000 +0000">,
 #<User:0x00007c037011d358
  id: 2,
Preparing full inspection value...
=> 
[#<User:0x00007c03706cd8c0
  id: 1,
  name: "Amit Sharma",
  email: "[FILTERED]",
  created_at: "2026-04-17 07:06:46.090495000 +0000",
  updated_at: "2026-04-17 07:06:46.090495000 +0000">,
 #<User:0x00007c037011d358
  id: 2,
  name: "Rahul Verma",
ecommerce-app(dev):008> User.where.not("email LIKE ?", "%@gmail.com"))
/home/cheshta/.rbenv/versions/3.3.11/lib/ruby/gems/3.3.0/gems/irb-1.17.0/lib/irb.rb:428:in `full_message': (ecommerce-app):8: syntax error, unexpected ')', expecting end-of-input (SyntaxError)
..."email LIKE ?", "%@gmail.com"))
...                              ^

ecommerce-app(dev):009> User.where.not("email LIKE ?", "%@gmail.com")
  User Load (1.6ms)  SELECT "users".* FROM "users" WHERE NOT ((email LIKE '%@gmail.com')) /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> []
ecommerce-app(dev):010> Product.where(price: 1000).or(Product.where(stock: 0))
  Product Load (2.4ms)  SELECT "products".* FROM "products" WHERE ("products"."price" = 1000 OR "products"."stock" = 0) /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> []
ecommerce-app(dev):011> Product.where(price: 1000).or(Product.where(stock: 2))
  Product Load (2.3ms)  SELECT "products".* FROM "products" WHERE ("products"."price" = 1000 OR "products"."stock" = 2) /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> []
ecommerce-app(dev):012> Product.where(price: 800).or(Product.where(stock: 2))
  Product Load (1.6ms)  SELECT "products".* FROM "products" WHERE ("products"."price" = 800 OR "products"."stock" = 2) /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Product:0x00007c03700d1e08
  id: 9,
  name: "H&M T-Shirt",
  price: 800,
  created_at: "2026-04-17 07:07:23.909232000 +0000",
  updated_at: "2026-04-17 07:07:23.909232000 +0000",
  stock: 50,
  category_id: 2>,
 #<Product:0x00007c03700d1cc8
ecommerce-app(dev):013> Product.where(price: 1000).where(stock: 5)
  Product Load (1.9ms)  SELECT "products".* FROM "products" WHERE "products"."price" = 1000 AND "products"."stock" = 5 /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> []
ecommerce-app(dev):014> Product.where(price: 800).where(stock: 5) 
  Product Load (1.6ms)  SELECT "products".* FROM "products" WHERE "products"."price" = 800 AND "products"."stock" = 5 /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> []
ecommerce-app(dev):015> Product.where(price: 800).where(stock: 50)
  Product Load (1.6ms)  SELECT "products".* FROM "products" WHERE "products"."price" = 800 AND "products"."stock" = 50 /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Product:0x00007c03700d2f88
  id: 9,
  name: "H&M T-Shirt",
  price: 800,
  created_at: "2026-04-17 07:07:23.909232000 +0000",
  updated_at: "2026-04-17 07:07:23.909232000 +0000",
  stock: 50,
  category_id: 2>]
ecommerce-app(dev):016> Product.where(id: [1,2]).and(Product.where(id: [2,3]))
  Product Load (1.6ms)  SELECT "products".* FROM "products" WHERE "products"."id" IN (1, 2) AND "products"."id" IN (2, 3) /* loading for pp */ LIMIT 11 /*application='EcommerceApp'*/
=> 
[#<Product:0x00007c037011d718
  id: 2,
  name: "Samsung Galaxy S23",
  price: 70000,
  created_at: "2026-04-17 07:07:23.752128000 +0000",
  updated_at: "2026-04-17 07:07:23.752128000 +0000",
  stock: 8,
  category_id: 1>]
  ```

  ### Practice on expense_tracker
  ```bash
  expense-tracker(dev):001> u1 = User.create(name: "Cheshta", email: "cheshta@gmail.com")
expense-tracker(dev):002> User.all
  TRANSACTION (0.8ms)  BEGIN /*application='ExpenseTracker'*/
  User Exists? (4.8ms)  SELECT 1 AS one FROM "users" WHERE "users"."email" = 'cheshta@gmail.com' LIMIT 1 /*application='ExpenseTracker'*/
  User Create (2.9ms)  INSERT INTO "users" ("name", "email", "created_at", "updated_at") VALUES ('Cheshta', 'cheshta@gmail.com', '2026-04-22 10:07:17.590127', '2026-04-22 10:07:17.590127') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (4.3ms)  COMMIT /*application='ExpenseTracker'*/
  User Load (2.0ms)  SELECT "users".* FROM "users" /* loading for pp */ LIMIT 11 /*application='ExpenseTracker'*/
=> 
[#<User:0x000073b10dc17320
  id: 1,
  name: "Cheshta",
  email: "[FILTERED]",
  created_at:
   "2026-04-22 10:07:17.590127000 +0000",
  updated_at:
   "2026-04-22 10:07:17.590127000 +0000">]
expense-tracker(dev):003> u2 = User.create(name: "Rahul", email: "rahul@gmail.com")
  TRANSACTION (1.0ms)  BEGIN /*application='ExpenseTracker'*/
  User Exists? (4.2ms)  SELECT 1 AS one FROM "users" WHERE "users"."email" = 'rahul@gmail.com' LIMIT 1 /*application='ExpenseTracker'*/
  User Create (1.9ms)  INSERT INTO "users" ("name", "email", "created_at", "updated_at") VALUES ('Rahul', 'rahul@gmail.com', '2026-04-22 10:07:51.471353', '2026-04-22 10:07:51.471353') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (2.5ms)  COMMIT /*application='ExpenseTracker'*/
=> 
#<User:0x000073b10c4c5b40
...
expense-tracker(dev):004> food = Category.create(name: "Food")
expense-tracker(dev):005> travel = Category.create(name: "Travel")
expense-tracker(dev):006> shopping = Category.create(name: "Shopping")
  TRANSACTION (1.7ms)  BEGIN /*application='ExpenseTracker'*/
  Category Exists? (9.2ms)  SELECT 1 AS one FROM "categories" WHERE "categories"."name" = 'Food' LIMIT 1 /*application='ExpenseTracker'*/
  Category Create (4.9ms)  INSERT INTO "categories" ("name", "created_at", "updated_at") VALUES ('Food', '2026-04-22 10:08:16.664741', '2026-04-22 10:08:16.664741') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (2.7ms)  COMMIT /*application='ExpenseTracker'*/
  TRANSACTION (1.1ms)  BEGIN /*application='ExpenseTracker'*/
  Category Exists? (5.0ms)  SELECT 1 AS one FROM "categories" WHERE "categories"."name" = 'Travel' LIMIT 1 /*application='ExpenseTracker'*/
  Category Create (1.8ms)  INSERT INTO "categories" ("name", "created_at", "updated_at") VALUES ('Travel', '2026-04-22 10:08:16.697348', '2026-04-22 10:08:16.697348') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (2.4ms)  COMMIT /*application='ExpenseTracker'*/
  TRANSACTION (1.1ms)  BEGIN /*application='ExpenseTracker'*/
  Category Exists? (4.0ms)  SELECT 1 AS one FROM "categories" WHERE "categories"."name" = 'Shopping' LIMIT 1 /*application='ExpenseTracker'*/
  Category Create (1.5ms)  INSERT INTO "categories" ("name", "created_at", "updated_at") VALUES ('Shopping', '2026-04-22 10:08:16.719147', '2026-04-22 10:08:16.719147') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (2.6ms)  COMMIT /*application='ExpenseTracker'*/
=> 
#<Category:0x000073b10ed09750
...
expense-tracker(dev):007> Category.all
  Category Load (1.6ms)  SELECT "categories".* FROM "categories" /* loading for pp */ LIMIT 11 /*application='ExpenseTracker'*/
=> 
[#<Category:0x000073b10c4ce240
  id: 1,
  name: "Food",
  created_at:
   "2026-04-22 10:08:16.664741000 +0000",
  updated_at:
   "2026-04-22 10:08:16.664741000 +0000">,
 #<Category:0x000073b10c4ce100
Preparing full inspection value...
=> 
[#<Category:0x000073b10c4ce240
  id: 1,
  name: "Food",
  created_at:
   "2026-04-22 10:08:16.664741000 +0000",
  updated_at:
   "2026-04-22 10:08:16.664741000 +0000">,
 #<Category:0x000073b10c4ce100
  id: 2,
  name: "Travel",
  created_at:
   "2026-04-22 10:08:16.697348000 +0000",
  updated_at:
   "2026-04-22 10:08:16.697348000 +0000">,
 #<Category:0x000073b10c4cde80
  id: 3,
  name: "Shopping",
  created_at:
   "2026-04-22 10:08:16.719147000 +0000",
  updated_at:
   "2026-04-22 10:08:16.719147000 +0000">]
expense-tracker(dev):008> Budget.create(monthly_limit: 5000, user: u1, category: food)
expense-tracker(dev):009> Budget.create(monthly_limit: 3000, user: u1, category: travel) 
expense-tracker(dev):010> Budget.create(monthly_limit: 7000, user: u2, category: shopping)
  TRANSACTION (0.7ms)  BEGIN /*application='ExpenseTracker'*/
  Budget Exists? (3.6ms)  SELECT 1 AS one FROM "budgets" WHERE "budgets"."category_id" = 1 AND "budgets"."user_id" = 1 LIMIT 1 /*application='ExpenseTracker'*/
  Budget Create (4.0ms)  INSERT INTO "budgets" ("monthly_limit", "user_id", "category_id", "created_at", "updated_at") VALUES (5000, 1, 1, '2026-04-22 10:09:04.977285', '2026-04-22 10:09:04.977285') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (2.3ms)  COMMIT /*application='ExpenseTracker'*/
  TRANSACTION (0.9ms)  BEGIN /*application='ExpenseTracker'*/
  Budget Exists? (3.8ms)  SELECT 1 AS one FROM "budgets" WHERE "budgets"."category_id" = 2 AND "budgets"."user_id" = 1 LIMIT 1 /*application='ExpenseTracker'*/
  Budget Create (2.8ms)  INSERT INTO "budgets" ("monthly_limit", "user_id", "category_id", "created_at", "updated_at") VALUES (3000, 1, 2, '2026-04-22 10:09:04.996623', '2026-04-22 10:09:04.996623') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (5.1ms)  COMMIT /*application='ExpenseTracker'*/
  TRANSACTION (2.9ms)  BEGIN /*application='ExpenseTracker'*/
  Budget Exists? (6.0ms)  SELECT 1 AS one FROM "budgets" WHERE "budgets"."category_id" = 3 AND "budgets"."user_id" = 2 LIMIT 1 /*application='ExpenseTracker'*/
  Budget Create (2.4ms)  INSERT INTO "budgets" ("monthly_limit", "user_id", "category_id", "created_at", "updated_at") VALUES (7000, 2, 3, '2026-04-22 10:09:05.024365', '2026-04-22 10:09:05.024365') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (3.3ms)  COMMIT /*application='ExpenseTracker'*/
=> 
#<Budget:0x000073b10c4c7080
 id: 3,
 monthly_limit: 7000,
 user_id: 2,
 category_id: 3,
 created_at:
  "2026-04-22 10:09:05.024365000 +0000",
 updated_at:
  "2026-04-22 10:09:05.024365000 +0000">
expense-tracker(dev):011> Budget.all
  Budget Load (2.1ms)  SELECT "budgets".* FROM "budgets" /* loading for pp */ LIMIT 11 /*application='ExpenseTracker'*/
=> 
[#<Budget:0x000073b10c4cf140
  id: 1,
  monthly_limit: 5000,
  user_id: 1,
  category_id: 1,
  created_at:
   "2026-04-22 10:09:04.977285000 +0000",
  updated_at:
   "2026-04-22 10:09:04.977285000 +0000">,
 #<Budget:0x000073b10c4cf000
  id: 2,
  monthly_limit: 3000,
  user_id: 1,
  category_id: 2,
  created_at:
   "2026-04-22 10:09:04.996623000 +0000",
  updated_at:
   "2026-04-22 10:09:04.996623000 +0000">,
 #<Budget:0x000073b10c4ced80
  id: 3,
  monthly_limit: 7000,
  user_id: 2,
  category_id: 3,
  created_at:
   "2026-04-22 10:09:05.024365000 +0000",
  updated_at:
   "2026-04-22 10:09:05.024365000 +0000">]
expense-tracker(dev):012> Expense.create(amount: 200, description: "Lunch", date: Date.today, user: u1, category: food)
expense-tracker(dev):013> Expense.create(amount: 1500, description: "Train Ticket", date: Date.today - 5, user: u1, category: travel)
expense-tracker(dev):014> Expense.create(amount: 300, description: "Snacks", date: Date.today - 20, user: u1, category: food)
expense-tracker(dev):015> Expense.create(amount: 2500, description: "Shoes", date: Date.today - 40, user: u2, category: shopping)
expense-tracker(dev):016> Expense.create(amount: 100, description: "Coffee", date: Date.today, user: u2, category: food)
  TRANSACTION (1.4ms)  BEGIN /*application='ExpenseTracker'*/
  Expense Create (9.9ms)  INSERT INTO "expenses" ("amount", "description", "date", "user_id", "category_id", "created_at", "updated_at") VALUES (200, 'Lunch', '2026-04-22', 1, 1, '2026-04-22 10:09:58.982673', '2026-04-22 10:09:58.982673') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (2.5ms)  COMMIT /*application='ExpenseTracker'*/
  TRANSACTION (0.9ms)  BEGIN /*application='ExpenseTracker'*/
  Expense Create (5.0ms)  INSERT INTO "expenses" ("amount", "description", "date", "user_id", "category_id", "created_at", "updated_at") VALUES (1500, 'Train Ticket', '2026-04-17', 1, 2, '2026-04-22 10:09:59.011351', '2026-04-22 10:09:59.011351') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (3.2ms)  COMMIT /*application='ExpenseTracker'*/
  TRANSACTION (1.0ms)  BEGIN /*application='ExpenseTracker'*/
  Expense Create (6.0ms)  INSERT INTO "expenses" ("amount", "description", "date", "user_id", "category_id", "created_at", "updated_at") VALUES (300, 'Snacks', '2026-04-02', 1, 1, '2026-04-22 10:09:59.034650', '2026-04-22 10:09:59.034650') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (4.6ms)  COMMIT /*application='ExpenseTracker'*/
  TRANSACTION (1.1ms)  BEGIN /*application='ExpenseTracker'*/
  Expense Create (5.9ms)  INSERT INTO "expenses" ("amount", "description", "date", "user_id", "category_id", "created_at", "updated_at") VALUES (2500, 'Shoes', '2026-03-13', 2, 3, '2026-04-22 10:09:59.055366', '2026-04-22 10:09:59.055366') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (2.8ms)  COMMIT /*application='ExpenseTracker'*/
  TRANSACTION (1.0ms)  BEGIN /*application='ExpenseTracker'*/
  Expense Create (5.8ms)  INSERT INTO "expenses" ("amount", "description", "date", "user_id", "category_id", "created_at", "updated_at") VALUES (100, 'Coffee', '2026-04-22', 2, 1, '2026-04-22 10:09:59.073540', '2026-04-22 10:09:59.073540') RETURNING "id" /*application='ExpenseTracker'*/
  TRANSACTION (4.9ms)  COMMIT /*application='ExpenseTracker'*/
=> 
#<Expense:0x000073b10c4cf280
 id: 5,
 amount: 100,
 description: "Coffee",
 date: "2026-04-22",
 user_id: 2,
 category_id: 1,
 created_at:
  "2026-04-22 10:09:59.073540000 +0000",
 updated_at:
  "2026-04-22 10:09:59.073540000 +0000">
```  