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

Used to understand available operations and syntax guidance.
2️⃣ Database Commands:  
🔷 \l → Lists all databases.  
🔷 \c → Connects to a specific database.  

Used for database navigation.
3️⃣ Table and Schema Commands:  
🔷 \dt → Lists tables in the current database.  
🔷 \d → Describes a table.  
🔷 \dn → Lists schemas.  

Used for inspecting database structure.
4️⃣ Session Control Commands:  
🔷 \q → Quits psql.  
🔷 \! → Executes a system (shell) command.  

Used for managing the working session.

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

## Create databse
PostgreSQL provides two ways of creating a new database −  
🔷 Using CREATE DATABASE, an SQL command.  
🔷 Using createdb a command-line executable.

### Using CREATE DATABASE

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

## Create table  
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

## Inserting data into table
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

## Selecting data from table
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
## Filtering data from the table
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

## Updating data in the table
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