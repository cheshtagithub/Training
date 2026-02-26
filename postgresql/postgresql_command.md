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

### Like Clause
LIKE is used for pattern matching in text (string) columns.  
It is used with WHERE.

#### Syntax
```bash
SELECT column_name
FROM table_name
WHERE column_name LIKE pattern;
```

#### Wildcard Characters
🔷 % → Represents any number of characters  
🔷 _ → Represents exactly one character

**Example:**  
1️⃣ Names starting with 'A'  
```bash
company_db=# SELECT *
FROM employees
WHERE first_name LIKE 'A%';
 employee_id | first_name |  salary  | department_id 
-------------+------------+----------+---------------
           3 | Arjun      | 51000.00 |             1
           6 | Anita      | 53000.00 |             3
(2 rows)
```
2️⃣ Names ending with 'a'
```bash
company_db=# SELECT * 
company_db-# FROM employees
company_db-# WHERE first_name LIKE '%a';
 employee_id | first_name |  salary  | department_id 
-------------+------------+----------+---------------
           2 | Sneha      | 72000.00 |             2
           4 | Meera      | 68000.00 |             3
           6 | Anita      | 53000.00 |             3
           8 | Divya      | 71000.00 |             2
(4 rows)
```
3️⃣ Names containing 'an'
```bash
company_db=# SELECT*
company_db-# FROM employees
company_db-# WHERE first_name LIKE '%an%';
 employee_id | first_name |  salary  | department_id 
-------------+------------+----------+---------------
           1 | Karan      | 48000.00 |             1
           9 | Manish     | 59000.00 |             3
(2 rows)
```
4️⃣ Exactly 5-letter names
```bash
company_db=# SELECT *
company_db-# FROM employees
company_db-# WHERE first_name LIKE '_____';
 employee_id | first_name |  salary  | department_id 
-------------+------------+----------+---------------
           1 | Karan      | 48000.00 |             1
           2 | Sneha      | 72000.00 |             2
           3 | Arjun      | 51000.00 |             1
           4 | Meera      | 68000.00 |             3
           6 | Anita      | 53000.00 |             3
           7 | Rohit      | 62000.00 |             1
           8 | Divya      | 71000.00 |             2
(7 rows)
```

#### ⚠ Case Sensitivity in PostgreSQL
LIKE is case-sensitive.  
If you want case-insensitive search:  
Use ILIKE.

**Example:**
```bash
company_db=# SELECT *
company_db-# FROM employees
company_db-# WHERE first_name ILIKE 'a%';
 employee_id | first_name |  salary  | department_id 
-------------+------------+----------+---------------
           3 | Arjun      | 51000.00 |             1
           6 | Anita      | 53000.00 |             3
(2 rows)
```

### AND/OR operator
These are used in the WHERE clause to combine multiple conditions.

### AND Operator
**Definition:** Returns rows only if all conditions are true.

#### Syntax
```bash
SELECT column_name
FROM table_name
WHERE condition1 AND condition2;
```

**Example:**
```bash
company_db=# SELECT *
company_db-# FROM employees
company_db-# WHERE department_id = 2 AND salary > 70000;
 employee_id | first_name |  salary  | department_id 
-------------+------------+----------+---------------
           2 | Sneha      | 72000.00 |             2
           5 | Vikram     | 75000.00 |             2
           8 | Divya      | 71000.00 |             2
(3 rows)
```

### OR Operator
**Definition:** Returns rows if at least one condition is true.

#### Syntax
```bash
SELECT column_name
FROM table_name
WHERE condition1 OR condition2;
```

**Example:**
```bash
company_db=# SELECT *
company_db-# FROM employees
company_db-# WHERE department_id = 1 OR department_id = 3;
 employee_id | first_name |  salary  | department_id 
-------------+------------+----------+---------------
           1 | Karan      | 48000.00 |             1
           3 | Arjun      | 51000.00 |             1
           4 | Meera      | 68000.00 |             3
           6 | Anita      | 53000.00 |             3
           7 | Rohit      | 62000.00 |             1
           9 | Manish     | 59000.00 |             3
(6 rows)
```

### Drop table
DROP TABLE is used to permanently delete a table from the database.  
It removes:  
🔷 Table structure  
🔷 All data inside it  
🔷 Constraints  
🔷 Indexes  

#### Syntax
```bash 
DROP TABLE table_name;
```

**Example:**
Creating a dummy table to use DROP command.
```bash
company_db=# \dt
            List of relations
 Schema |    Name     | Type  |  Owner   
--------+-------------+-------+----------
 public | departments | table | postgres
 public | employees   | table | postgres
 public | test_table  | table | postgres
(3 rows)

company_db=# DROP TABLE test_table;
DROP TABLE
company_db=# \dt
            List of relations
 Schema |    Name     | Type  |  Owner   
--------+-------------+-------+----------
 public | departments | table | postgres
 public | employees   | table | postgres
(2 rows)
```

### Truncate table command
TRUNCATE is used to delete all rows from a table instantly.  
It is faster than DELETE because:  
🔷 It does not scan each row  
🔷 It does not log individual row deletions  
🔷 It resets storage immediately

#### Syntax
```bash
TRUNCATE TABLE table_name;
```

**Example:**  
Creating test_table to implement truncate.
```bash
company_db=# SELECT * FROM test_table;
 id | name 
----+------
  1 | A
  2 | B
  3 | C
(3 rows)

company_db=# TRUNCATE TABLE test_table ;
TRUNCATE TABLE
company_db=# SELECT * FROM test_table;
 id | name 
----+------
(0 rows)
```

## JOINS
A JOIN is used to combine rows from two or more tables based on a related column.  
Usually based on:  
🔷 PRIMARY KEY  
🔷 FOREIGN KEY  

### Types of Joins
🔷 INNER JOIN  
🔷 LEFT JOIN  
🔷 RIGHT JOIN  
🔷 FULL JOIN  
🔷 OUTER JOIN  
🔷 SELF JOIN  

#### 1️⃣ INNER JOIN
Returns only matching rows from both tables.

**Example:**
```bash
company_db=# SELECT e.name, e.salary, d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;
  name   |  salary  | department_name 
---------+----------+-----------------
 Alice   | 45000.00 | HR
 Bob     | 75000.00 | IT
 Charlie | 68000.00 | IT
 David   | 52000.00 | Sales
 Emma    | 49000.00 | HR
 Frank   | 88000.00 | Finance
 Grace   | 72000.00 | Marketing
 Hannah  | 61000.00 | Operations
 Ishaan  | 95000.00 | IT
 Karan   | 53000.00 | Finance
 Lavanya | 66000.00 | Marketing
 Mohit   | 58000.00 | Operations
 Nisha   | 62000.00 | HR
(13 rows)
```

#### 2️⃣ LEFT JOIN (LEFT OUTER JOIN)
Returns:  
🔷 All rows from LEFT table  
🔷 Matching rows from right  
🔷 If no match → NULL

**Example:**
```bash
company_db=# SELECT e.name, d.department_name
company_db-# FROM employees e
company_db-# LEFT JOIN departments d
company_db-# ON e.department_id = d.department_id;
  name   | department_name 
---------+-----------------
 Alice   | HR
 Bob     | IT
 Charlie | IT
 David   | Sales
 Emma    | HR
 Frank   | Finance
 Grace   | Marketing
 Hannah  | Operations
 Ishaan  | IT
 Jiya    | 
 Karan   | Finance
 Lavanya | Marketing
 Mohit   | Operations
 Nisha   | HR
 Om      | 
(15 rows)
```

#### 3️⃣ RIGHT JOIN (RIGHT OUTER JOIN)
Returns:  
🔷 All rows from RIGHT table  
🔷 Matching rows from left  
🔷 If no match → NULL

**Example:**
```bash
company_db=# SELECT e.name, d.department_name
company_db-# FROM employees e
company_db-# RIGHT JOIN departments d
company_db-# ON e.department_id = d.department_id;
  name   | department_name 
---------+-----------------
 Alice   | HR
 Bob     | IT
 Charlie | IT
 David   | Sales
 Emma    | HR
 Frank   | Finance
 Grace   | Marketing
 Hannah  | Operations
 Ishaan  | IT
 Karan   | Finance
 Lavanya | Marketing
 Mohit   | Operations
 Nisha   | HR
(13 rows)
```

#### 4️⃣ FULL JOIN (FULL OUTER JOIN)
Returns:  
🔷 All rows from LEFT  
🔷 All rows from RIGHT  
🔷 Matched where possible  

**Example:**
```bash
company_db=# SELECT e.name, d.department_name
FROM departments d
FULL JOIN employees e  
ON e.department_id = d.department_id;
  name   | department_name 
---------+-----------------
 Alice   | HR
 Bob     | IT
 Charlie | IT
 David   | Sales
 Emma    | HR
 Frank   | Finance
 Grace   | Marketing
 Hannah  | Operations
 Ishaan  | IT
 Jiya    | 
 Karan   | Finance
 Lavanya | Marketing
 Mohit   | Operations
 Nisha   | HR
 Om      | 
(15 rows)
```

#### 5️⃣ OUTER JOIN
Important:  
🔷 LEFT JOIN = LEFT OUTER JOIN  
🔷 RIGHT JOIN = RIGHT OUTER JOIN  
🔷 FULL JOIN = FULL OUTER JOIN  
The word OUTER is optional

**Example:**
```bash
LEFT OUTER JOIN
```
Same as
```bash
LEFT JOIN
```

#### 6️⃣ SELF JOIN
Self join means:  
👉 A table joins with itself.

**Example:**
Adding manager column to employees to implement self join.
```bash
company_db=# SELECT e.name AS employee,
company_db-# m.name AS manager
company_db-# FROM employees e
company_db-# LEFT JOIN employees m
company_db-# ON e.manager_id = m.employee_id;
 employee | manager 
----------+---------
 Alice    | 
 Emma     | 
 Frank    | 
 Grace    | 
 Hannah   | 
 Ishaan   | 
 Jiya     | 
 Lavanya  | 
 Mohit    | 
 Nisha    | 
 Om       | 
 Bob      | Alice
 Charlie  | Alice
 David    | Bob
 Karan    | Frank
(15 rows)
```