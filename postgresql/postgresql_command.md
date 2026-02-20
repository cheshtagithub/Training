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