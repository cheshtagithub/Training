# PostgreSQL

**Definition:** PostgreSQL is an open-source relational database management system (RDBMS).

It is used to:

🔷 Store data  
🔷 Manage data  
🔷 Query data  
🔷 Maintain relationships between data

It follows the SQL (Structured Query Language) standard.

## Why is it used?
PostgreSQL is used to store, manage, and retrieve structured data efficiently and securely.

It is mainly used in applications where:

🔷 Data needs to be stored reliably  
🔷 Multiple users access data simultaneously  
🔷 Complex queries are required  
🔷 Transactions must be safe and consistent  

## How to install PostgreSQL in ubuntu?

1️⃣ Update packages  
``` bash
sudo apt update
```  
2️⃣ Install PostgreSQL  
``` bash
sudo apt install postgresql postgresql-contrib
```  
3️⃣ Check if service is running  
``` bash
sudo systemctl status postgresql
```  
PostgreSQL will be installed after this.

## Switch to postgres user

``` bash
sudo -i -u postgres
```
### OR
``` bash
sudo -iu postgres
```

## Open PostgreSQL shell
```bash
psql
```

**EXAMPLE:** 
``` bash
cheshta@cheshta-Latitude-E7470:~$ sudo -iu postgres 
[sudo] password for cheshta: 
postgres@cheshta-Latitude-E7470:~$ psql
psql (12.22 (Ubuntu 12.22-0ubuntu0.20.04.4))
Type "help" for help.

postgres=# 
```

## Basic psql Commands
psql provides special built-in commands called meta-commands.
These commands start with a backslash (\) and are used to manage and navigate the PostgreSQL environment.
They are different from normal SQL commands.

### Commonly Used psql Commands
1️⃣ Help Command:  
🔷 \? → Shows all available psql commands.  
🔷 \h → Shows help for SQL commands.

2️⃣ Database Commands:  
🔷 \l → Lists all databases.  
🔷 \c → Connects to a specific database.  

3️⃣ Table and Schema Commands:  
🔷 \dt → Lists tables in the current database.  
🔷 \d → Describes a table.  
🔷 \dn → Lists schemas.  

4️⃣ Session Control Commands:  
🔷 \q → Quits psql.  
🔷 \\! → Executes a system (shell) command.  

## Data Types in PostgreSQL

**Definition:** While creating table, for each column, you specify a data type, i.e., what kind of data you want to store in the table fields. They ensure data integrity, consistency, and proper storage.

### Categories of Data Types  

1️⃣ Numeric Data Types: Used to store numerical values.

Includes:  
🔷 Small integers  
🔷 Standard integers  
🔷 Large integers  
🔷 Exact decimal numbers  
🔷 Floating point numbers  

These are used for storing quantities, prices, counts, measurements, etc.

2️⃣ Character Data Types: Used to store textual data.

Includes:  
🔷 Fixed-length strings  
🔷 Variable-length strings  
🔷 Unlimited-length text  

Used for names, addresses, descriptions, and textual information.

3️⃣ Date and Time Data Types: Used to store date and time values. 

Includes:  
🔷 Date  
🔷 Time  
🔷 Timestamp  
🔷 Time intervals

Used for tracking events, logs, transactions, and records.

4️⃣ Boolean Data Type: Used to store logical values.

Possible values:  
🔷 True  
🔷 False

Used for status fields such as active/inactive, yes/no, enabled/disabled.

5️⃣ Auto-Increment Type: Used to automatically generate unique numeric values.  
Commonly used for primary keys to uniquely identify records.

## Database commands

### Create databse
PostgreSQL provides two ways of creating a new database −  
🔷 Using CREATE DATABASE, an SQL command.  
🔷 Using createdb a command-line executable.

**Using CREATE DATABASE**

This command will create a database from PostgreSQL shell prompt.

#### Syntax
The basic syntax of CREATE DATABASE statement is as follows −  
``` bash
CREATE DATABASE dbname;
```

**Example:** Creating and connecting with a database.  
```bash
postgres=# CREATE DATABASE company_db;
CREATE DATABASE
postgres=# \c company_db
You are now connected to database "company_db" as user "postgres".
company_db=# 
```

### Alter database
ALTER DATABASE is used to modify the properties of an existing database, such as renaming the database, changing the owner of the database, changing the connection limit, etc.

#### Syntax
```bash
ALTER DATABASE name ACTION;
```

**Example:**
Creating an example database practice_db to practice database commands.
```bash
postgres=# CREATE DATABASE practice_db;
CREATE DATABASE
postgres=# \l
                              List of databases
    Name     |  Owner   | Encoding | Collate | Ctype |   Access privileges   
-------------+----------+----------+---------+-------+-----------------------
 company_db  | postgres | UTF8     | en_IN   | en_IN | 
 postgres    | postgres | UTF8     | en_IN   | en_IN | 
 practice_db | postgres | UTF8     | en_IN   | en_IN | 
 template0   | postgres | UTF8     | en_IN   | en_IN | =c/postgres          +
             |          |          |         |       | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_IN   | en_IN | =c/postgres          +
             |          |          |         |       | postgres=CTc/postgres
(5 rows)
```
We cannot alter the database if we are connected to it.
```bash
practice_db=# ALTER DATABASE practice_db RENAME TO practice_new
practice_db-# ;
ERROR:  current database cannot be renamed
```
To alter the database, you must connect with other database first.
```bash
practice_db=# \c postgres
You are now connected to database "postgres" as user "postgres".
postgres=# ALTER DATABASE practice_db RENAME TO practice_new;
ALTER DATABASE
postgres=# \l
                              List of databases
     Name     |  Owner   | Encoding | Collate | Ctype |   Access privileges   
--------------+----------+----------+---------+-------+-----------------------
 company_db   | postgres | UTF8     | en_IN   | en_IN | 
 postgres     | postgres | UTF8     | en_IN   | en_IN | 
 practice_new | postgres | UTF8     | en_IN   | en_IN | 
 template0    | postgres | UTF8     | en_IN   | en_IN | =c/postgres          +
              |          |          |         |       | postgres=CTc/postgres
 template1    | postgres | UTF8     | en_IN   | en_IN | =c/postgres          +
              |          |          |         |       | postgres=CTc/postgres
(5 rows)
```

### Drop database
It removes the catalog entries for the database and deletes the directory containing the data. It can only be executed by the database owner. This command cannot be executed while you or anyone else is connected to the target database (connect to postgres or any other database to issue this command).

#### Syntax
```bash
DROP DATABASE [ IF EXISTS ] name
```

**Example:**
```bash
postgres=# DROP DATABASE practice_new;
DROP DATABASE
postgres=# \l
                             List of databases
    Name    |  Owner   | Encoding | Collate | Ctype |   Access privileges   
------------+----------+----------+---------+-------+-----------------------
 company_db | postgres | UTF8     | en_IN   | en_IN | 
 postgres   | postgres | UTF8     | en_IN   | en_IN | 
 template0  | postgres | UTF8     | en_IN   | en_IN | =c/postgres          +
            |          |          |         |       | postgres=CTc/postgres
 template1  | postgres | UTF8     | en_IN   | en_IN | =c/postgres          +
            |          |          |         |       | postgres=CTc/postgres
(4 rows)
```

## Table commands
### Create table  
 CREATE TABLE statement is used to create a new table in any of the given database.

 #### Syntax
 The basic syntax of creating a table is as follows:  
```bash 
CREATE TABLE table_name(
   column1 datatype,
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
   PRIMARY KEY( one or more columns )
);
```
**Example:**
```bash
company_db=# CREATE TABLE departments(
company_db(# department_id SERIAL PRIMARY KEY,
company_db(# department_name VARCHAR(100) NOT NULL UNIQUE
company_db(# );
CREATE TABLE
```

### Inserting data into table
INSERT INTO statement allows user to insert one or new rows into a table. One can insert a single row at a time or several rows as a result of a query.

#### Syntax
```bash
INSERT INTO TABLE_NAME (column1, column2, column3, ..., columnN)
VALUES (value1, value2, value3, ..., valueN);
```

**Example:**
```bash
INSERT INTO departments(department_name)
company_db-# VALUES
company_db-# ('IT')
company_db-# ('HR')
company_db-# ('Finance'),
company_db-# ('Marketing');
INSERT 0 4
company_db=# 
```

### Selecting data from table
SELECT statement is used to fetch the data from a database table that returns data in the form of result table. These result tables are called result-sets.

#### Syntax
```bash
SELECT column1, column2, columnN FROM table_name;
```
To fetch all the fields from the table:
```bash
SELECT * FROM table_name;
```

**Example:**
```bash
company_db=# SELECT * FROM departments;
 department_id | department_name 
---------------+-----------------
             1 | IT
             2 | HR
             3 | Finance
             4 | Marketing
(4 rows)
```
### Filtering data from the table
We use WHERE clause to filter the data. WHERE clause is used to specify a condition while fetching the data from single table or joining with multiple tables.  
If the given condition is satisfied, only then it returns specific value from the table. You can filter out rows that you do not want included in the result-set by using the WHERE clause.  
The WHERE clause not only is used in SELECT statement, but it is also used in UPDATE, DELETE statement, etc., which we would examine in subsequent chapters.

#### Syntax
```bash
SELECT column1, column2, columnN
FROM table_name
WHERE [search_condition]
```

**Example:**
```bash
company_db=# SELECT * FROM departments
company_db-# WHERE department_name = 'IT';
 department_id | department_name 
---------------+-----------------
             1 | IT
(1 row)
```
```bash
company_db=# SELECT * FROM departments
company_db-# WHERE department_id > 2;
 department_id | department_name 
---------------+-----------------
             3 | Finance
             4 | Marketing
(2 rows)
```

### Updating data in the table
UPDATE statement is used to modify or change the existing records in a table. You can use WHERE clause with UPDATE statement to update the selected rows. Otherwise, all the rows would be updated.

#### Syntax
```bash
UPDATE table_name
SET column1 = value1, column2 = value2, ..., columnN = valueN
WHERE [condition];
```

**Example:**
```bash
company_db=# UPDATE departments
company_db-# SET department_name = 'Human Resources'
company_db-# WHERE department_name = 'HR';
UPDATE 1
```
```bash
company_db=# SELECT * FROM departments;
 department_id | department_name 
---------------+-----------------
             1 | IT
             3 | Finance
             4 | Marketing
             2 | Human Resources
(4 rows)
```

### Retrieving data in order
ORDER BY clause is used to sort the data in ascending or descending order, based on one or more columns.

#### Syntax
```bash
SELECT column-list
FROM table_name
[WHERE condition]
[ORDER BY column1, column2, .. columnN] [ASC | DESC];
```

**Example:**
```bash
company_db=# SELECT * FROM departments
company_db-# ORDER BY department_id;
 department_id | department_name 
---------------+-----------------
             1 | IT
             2 | Human Resources
             3 | Finance
             4 | Marketing
(4 rows)
```

### Deleting data from table
DELETE statement is used to delete the existing records from a table. You can use WHERE clause with DELETE statement to delete the selected rows. Otherwise, all the records would be deleted.

#### Syntax
```bash
DELETE FROM table_name
WHERE [condition];
```

**Example:**
```bash
company_db=# DELETE FROM departments
company_db-# WHERE department_name = 'Marketing';
DELETE 1
```
```bash
company_db=# SELECT * FROM departments;
 department_id | department_name 
---------------+-----------------
             1 | IT
             3 | Finance
             2 | Human Resources
(3 rows)
```

### Altering a table  
It is used to modify the structure of an existing table.  
We use it to:  
🔷 Add a column  
🔷 Remove a column  
🔷 Rename a column  
🔷 Change data type  
🔷 Add constraints

#### Syntax
1️⃣ Add Column  
```bash
ALTER TABLE table_name
ADD COLUMN column_name data_type;
```
**Example:**
```bash
company_db=# ALTER TABLE departments
company_db-# ADD COLUMN created_at DATE;
ALTER TABLE
```
```bash
company_db=# SELECT * FROM departments;
 department_id | department_name | created_at 
---------------+-----------------+------------
             1 | IT              | 
             3 | Finance         | 
             2 | Human Resources | 
(3 rows)
```
2️⃣ Rename a Column  
```bash
ALTER TABLE table_name
RENAME COLUMN old_column_name TO new_column_name;
```
**Example:**
```bash
company_db=# ALTER TABLE departments
company_db-# RENAME COLUMN department_name TO dept_name;
ALTER TABLE
```
```bash
company_db=# SELECT * FROM departments;
 department_id |    dept_name    | created_at 
---------------+-----------------+------------
             1 | IT              | 
             3 | Finance         | 
             2 | Human Resources | 
(3 rows)
```
3️⃣ Drop a Column
```bash
ALTER TABLE table_name
DROP COLUMN column_name;
```
**Example:**
```bash
company_db=# ALTER TABLE departments
company_db-# DROP COLUMN created_at;
ALTER TABLE
```
```bash
company_db=# SELECT * FROM departments;
 department_id |    dept_name    
---------------+-----------------
             1 | IT
             3 | Finance
             2 | Human Resources
(3 rows)
```

### Group By
The PostgreSQL GROUP BY clause is used in collaboration with the SELECT statement to group together those rows in a table that have identical data. This is done to eliminate redundancy in the output and/or compute aggregates that apply to these groups. The GROUP BY clause follows the WHERE clause in a SELECT statement and precedes the ORDER BY clause.

#### Syntax
```bash
SELECT column-list
FROM table_name
WHERE [ conditions ]
GROUP BY column1, column2....columnN
ORDER BY column1, column2....columnN
```

**Example:**
Creating table employees to practice group by.
```bash
company_db=# CREATE TABLE employees(employee_id SERIAL PRIMARY KEY,
company_db(# first_name VARCHAR(50) NOT NULL,
company_db(# salary NUMERIC(10,2) NOT NULL,
company_db(# department_id INTEGER REFERENCES departments(department_id)
company_db(# );
CREATE TABLE
```
Employees table:  
```bash
 employee_id | first_name |  salary  | department_id 
-------------+------------+----------+---------------
           7 | Rohit      | 62000.00 |             1
           1 | Karan      | 48000.00 |             1
           3 | Arjun      | 51000.00 |             1
           5 | Vikram     | 75000.00 |             2
           2 | Sneha      | 72000.00 |             2
           8 | Divya      | 71000.00 |             2
           4 | Meera      | 68000.00 |             3
           9 | Manish     | 59000.00 |             3
           6 | Anita      | 53000.00 |             3
(9 rows)
```
Using group by on above table:
```bash
company_db=# SELECT department_id, COUNT(*)
company_db-# FROM employees
company_db-# GROUP BY department_id;
 department_id | count 
---------------+-------
             3 |     3
             2 |     3
             1 |     3
(3 rows)
```
```bash
company_db=# SELECT department_id, SUM(salary)
company_db-# FROM employees
company_db-# GROUP BY department_id;
 department_id |    sum    
---------------+-----------
             3 | 180000.00
             2 | 218000.00
             1 | 161000.00
(3 rows)
```
```bash
company_db=# SELECT department_id, AVG(salary)
company_db-# FROM employees
company_db-# GROUP BY department_id;
 department_id |        avg         
---------------+--------------------
             3 | 60000.000000000000
             2 | 72666.666666666667
             1 | 53666.666666666667
(3 rows)
```

### Having clause
The HAVING clause allows us to pick out particular rows where the function's result meets some condition. The WHERE clause places conditions on the selected columns, whereas the HAVING clause places conditions on groups created by the GROUP BY clause.

#### Syntax
```bash 
SELECT column1, column2
FROM table1, table2
WHERE [ conditions ]
GROUP BY column1, column2
HAVING [ conditions ]
ORDER BY column1, column2
```

**Example:**
Show Departments Having More Than 2 Employees
```bash
company_db=# SELECT department_id, COUNT(*)
company_db-# FROM employees
company_db-# GROUP BY department_id
company_db-# HAVING COUNT(*) > 2;
 department_id | count 
---------------+-------
             3 |     3
             2 |     3
             1 |     3
(3 rows)
```
Show Departments Where Average Salary > 60000
```bash
company_db=# SELECT department_id, AVG(salary)
company_db-# FROM employees
company_db-# GROUP BY department_id
company_db-# HAVING AVG(salary) > 60000;
 department_id |        avg         
---------------+--------------------
             2 | 72666.666666666667
(1 row)
```
### Distinct keyword
DISTINCT keyword is used in conjunction with SELECT statement to eliminate all the duplicate records and fetching only unique records. There may be a situation when you have multiple duplicate records in a table. While fetching such records, it makes more sense to fetch only unique records instead of fetching duplicate records.

#### Syntax
```bash
SELECT DISTINCT column1, column2, .... , columnN
FROM table_name
WHERE [condition]
```

**Example:**
```bash
company_db=# SELECT DISTINCT department_id
company_db-# FROM employees;
 department_id 
---------------
             3
             2
             1
(3 rows)
```

### Limit and Offset clause 
LIMIT is used to restrict the number of rows returned.  
OFFSET is used to skip a number of rows before starting to return rows.

#### Syntax
```bash
SELECT column_name
FROM table_name
LIMIT number
OFFSET number;
```

**Example:**
```bash
company_db=# SELECT *
company_db-# FROM employees
company_db-# LIMIT 3
company_db-# OFFSET 2;
 employee_id | first_name |  salary  | department_id 
-------------+------------+----------+---------------
           3 | Arjun      | 51000.00 |             1
           4 | Meera      | 68000.00 |             3
           5 | Vikram     | 75000.00 |             2
(3 rows)
```
