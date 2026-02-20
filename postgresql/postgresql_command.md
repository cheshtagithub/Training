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

## CREATE Database
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

