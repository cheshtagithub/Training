# Airline Assignment
Created database airline_db to solve the assignment.

## Tables created

### 1️⃣Flights
**🔗Code**
```bash
airline_db=# CREATE TABLE Flights (
airline_db(# flno INTEGER PRIMARY KEY,
airline_db(# from_city VARCHAR(50),
airline_db(# to_city VARCHAR(50),
airline_db(# distance INTEGER,
airline_db(# departs TIME,
airline_db(# arrives TIME,
airline_db(# price INTEGER
airline_db(# );
```
### 2️⃣Aircraft
**🔗Code**
```bash
airline_db=# CREATE TABLE Aircraft (
airline_db(# aid INTEGER PRIMARY KEY,
airline_db(# aname VARCHAR(100),
airline_db(# cruisingrange INTEGER
airline_db(# );
```
### 3️⃣Employees
**🔗Code**
```bash
airline_db=# CREATE TABLE Employees (
airline_db(# eid INTEGER PRIMARY KEY,
airline_db(# ename VARCHAR(100),
airline_db(# salary INTEGER
airline_db(# );
```
### 4️⃣Certified
**🔗Code**
```bash
airline_db=# CREATE TABLE Certified (
airline_db(# eid INTEGER,
airline_db(# aid INTEGER,
airline_db(# PRIMARY KEY (eid, aid),
airline_db(# FOREIGN KEY (eid) REFERENCES Employees(eid),
airline_db(# FOREIGN KEY (aid) REFERENCES Aircraft(aid)
airline_db(# );
```
## Solutions
### a. Find the names of aircraft such that all pilots certified to operate them earn more than $80,000.
**🔗Code**
```bash
airline_db=# SELECT a.aname
airline_db-# FROM aircraft a
airline_db-# WHERE NOT EXISTS(
airline_db(# SELECT 1
airline_db(# FROM certified c 
airline_db(# JOIN employees e ON c.eid=e.eid
airline_db(# WHERE c.aid=a.aid
airline_db(# AND e.salary<=80000
airline_db(# );
```
**Output**
```bash
         aname          
------------------------
 Boeing 737
 Boeing 747
 Boeing 777
 Airbus A330
 Bombardier Q400
 Airbus A350
 Boeing 787
 Cessna 172
 Boeing 757
 Gulfstream G650
 Dassault Falcon 8X
 Bombardier Global 7500
 Airbus Beluga
(13 rows)
```

### b. For each pilot who is certified for more than three aircraft, find the eid and the maximum cruisingrange of the aircraft for which she or he is certified.
**🔗Code**
```bash
airline_db=# SELECT c.eid, MAX(a.cruising_range) AS max_range
airline_db-# FROM Certified c
airline_db-# JOIN Aircraft a ON c.aid = a.aid
airline_db-# GROUP BY c.eid
airline_db-# HAVING COUNT(c.aid) > 3;
```
**Output**
```bash
 eid | max_range 
-----+-----------
 101 |      7500
(1 row)
```
### c. Find the names of pilots whose salary is less than the price of the cheapest route from Los Angeles to Honolulu.
**🔗Code**
```bash
airline_db=# SELECT e.ename
airline_db-# FROM Employees e
airline_db-# JOIN Certified c ON e.eid = c.eid
airline_db-# WHERE e.salary < (
airline_db(# SELECT MIN(price)
airline_db(# FROM Flights
airline_db(# WHERE from_city = 'Los Angeles'
airline_db(# AND to_city = 'Honolulu'
airline_db(# );
```
**Output**
```bash
 ename 
-------
(0 rows)
```

### d. For all aircraft with cruisingrange over 1000 miles, find the name of the aircraft and the average salary of all pilots certified for this aircraft.
**🔗Code**
```bash
airline_db=# SELECT a.aname, AVG(e.salary) AS avg_salary
airline_db-# FROM Aircraft a
airline_db-# JOIN Certified c ON a.aid = c.aid
airline_db-# JOIN Employees e ON c.eid = e.eid
airline_db-# WHERE a.cruising_range > 1000
airline_db-# GROUP BY a.aname;
```
**Output**
```bash
       aname        |     avg_salary      
--------------------+---------------------
 Airbus A319        |  80000.000000000000
 Airbus A320        |  82500.000000000000
 Airbus A321        |  76666.666666666667
 Airbus A330        |  88000.000000000000
 Airbus A350        | 114600.000000000000
 ATR 72             |  83666.666666666667
 Boeing 737         |  91000.000000000000
 Boeing 747         | 103833.333333333333
 Boeing 757         |  84500.000000000000
 Boeing 767         |  82000.000000000000
 Boeing 777         | 103428.571428571429
 Boeing 787         | 114166.666666666667
 Dassault Falcon 8X |  91000.000000000000
 Embraer E190       |  85333.333333333333
 Embraer Phenom 300 |  74000.000000000000
 Gulfstream G650    |  91500.000000000000
(16 rows)
```

### e. Find the names of pilots certified for some Boeing aircraft.
**🔗Code**
```bash
airline_db=# SELECT DISTINCT e.ename
airline_db-# FROM Employees e
airline_db-# JOIN Certified c ON e.eid = c.eid
airline_db-# JOIN Aircraft a ON c.aid = a.aid
airline_db-# WHERE a.aname LIKE 'Boeing%';
```
**Output**
```bash
      ename      
-----------------
 Abhishek Sinha
 Amit Verma
 Arjun Reddy
 Captain Johnson
 Captain Robert
 Captain Smith
 Deepak Mishra
 Gaurav Gupta
 Harsh Vardhan
 Kunal Kapoor
 Naveen Kumar
 Priya Singh
 Rahul Sharma
 Rajeev Malhotra
 Rohit Mehta
 Simran Kaur
 Vikram Singh
(17 rows)
```

### f. Find the aids of all aircraft that can be used on routes from Los Angeles to Chicago.
**🔗Code**
```bash
airline_db=# SELECT a.aid
airline_db-# FROM Aircraft a
airline_db-# JOIN Flights f
airline_db-# ON a.cruising_range >= f.distance
airline_db-# WHERE f.from_city = 'Los Angeles'
airline_db-# AND f.to_city = 'Chicago';
```
**Output**
```bash
 aid 
-----
   1
   2
   3
   4
   6
   7
   9
  10
  11
  12
  14
  15
  16
  17
  18
  19
  20
(17 rows)
```

### g. Identify the routes that can be piloted by every pilot who makes more than $100,000.
**🔗Code**
```bash
airline_db=# SELECT DISTINCT f.from_city, f.to_city
airline_db-# FROM Flights f
airline_db-# WHERE NOT EXISTS (
airline_db(# SELECT e.eid
airline_db(# FROM Employees e
airline_db(# WHERE e.salary > 100000
airline_db(# AND NOT EXISTS (
airline_db(# SELECT *
airline_db(# FROM Certified c
airline_db(# JOIN Aircraft a ON c.aid = a.aid
airline_db(# WHERE c.eid = e.eid
airline_db(# AND a.cruising_range >= f.distance
airline_db(# )
airline_db(# );
```
**Output**
```bash
  from_city  |  to_city  
-------------+-----------
 Ahmedabad   | Bangalore
 Bangalore   | Delhi
 Bangalore   | Dubai
 Bangalore   | Hyderabad
 Bangalore   | Kolkata
 Chennai     | Bangalore
 Chennai     | Delhi
 Chennai     | Mumbai
 Chennai     | Singapore
 Chicago     | New York
 Delhi       | Ahmedabad
 Delhi       | Bangalore
 Delhi       | Bangkok
 Delhi       | Chennai
 Delhi       | Dubai
 Delhi       | Jaipur
 Delhi       | Kolkata
 Delhi       | London
 Delhi       | Mumbai
 Delhi       | New York
 Delhi       | Singapore
 Delhi       | Sydney
 Hyderabad   | Delhi
 Hyderabad   | Mumbai
 Hyderabad   | Singapore
 Jaipur      | Mumbai
 Kolkata     | Chennai
 Kolkata     | Delhi
 Kolkata     | Dubai
 Los Angeles | Chicago
 Los Angeles | Honolulu
 Madison     | Chicago
 Madison     | New York
 Mumbai      | Chennai
 Mumbai      | Delhi
 Mumbai      | Dubai
 Mumbai      | Kolkata
 Mumbai      | London
 Mumbai      | Paris
 Mumbai      | Singapore
(40 rows)
```
### h. Print the enames of pilots who can operate planes with cruisingrange greater than 3000 miles but are not certified on any Boeing aircraft.
**🔗Code**
```bash
airline_db=# SELECT DISTINCT e.ename
airline_db-# FROM Employees e
airline_db-# JOIN Certified c ON e.eid = c.eid
airline_db-# JOIN Aircraft a ON c.aid = a.aid
airline_db-# WHERE a.cruising_range > 3000
airline_db-# AND e.eid NOT IN (
airline_db(# SELECT c.eid
airline_db(# FROM Certified c
airline_db(# JOIN Aircraft a ON c.aid = a.aid
airline_db(# WHERE a.aname LIKE 'Boeing%'
airline_db(# );
```
**Output**
```bash
     ename      
----------------
 Aditya Jain
 Farhan Ali
 Kritika Sharma
 Pankaj Tiwari
 Rakesh Kumar
 Shreya Sen
 Sonal Jain
 Suresh Iyer
 Tarun Bansal
 Varun Khanna
(10 rows)
```

### i. A customer wants to travel from Madison to New York with no more than two changes of flight. List the choice of departure times from Madison if the customer wants to arrive in New York by 6 p.m.
**🔗Code**
```bash
airline_db=# SELECT departs
airline_db-# FROM Flights
airline_db-# WHERE from_city = 'Madison'
airline_db-# AND to_city = 'New York'
airline_db-# AND arrives <= '18:00';
```
**Output**
```bash
 departs  
----------
 09:00:00
(1 row)
```

### j. Compute the difference between the average salary of a pilot and the average salary of all employees (including pilots).
**🔗Code**
```bash
airline_db=# SELECT
airline_db-# (
airline_db(# SELECT AVG(salary)
airline_db(# FROM Employees
airline_db(# WHERE eid IN (SELECT eid FROM Certified)
airline_db(# ) -
airline_db-# (
airline_db(# SELECT AVG(salary)
airline_db(# FROM Employees
airline_db(# ) AS salary_difference;
```
**Output**
```bash
 salary_difference 
-------------------
 7543.704891740177
(1 row)
```

### k. Print the name and salary of every nonpilot whose salary is more than the average salary for pilots.
**🔗Code**
```bash
airline_db=# SELECT ename, salary
airline_db-# FROM Employees
airline_db-# WHERE eid NOT IN (SELECT eid FROM Certified)
airline_db-# AND salary >
airline_db-# (
airline_db(# SELECT AVG(e.salary)
airline_db(# FROM Employees e
airline_db(# JOIN Certified c ON e.eid = c.eid
airline_db(# );
```
**Output**
```bash
 ename | salary 
-------+--------
(0 rows)
```

### l. Print the names of employees who are certified only on aircrafts with cruising range longer than 1000 miles.
**🔗Code**
```bash
airline_db=# SELECT e.ename
airline_db-# FROM Employees e
airline_db-# WHERE e.eid IN (SELECT eid FROM Certified)
airline_db-# AND NOT EXISTS (
airline_db(# SELECT *
airline_db(# FROM Certified c
airline_db(# JOIN Aircraft a ON c.aid = a.aid
airline_db(# WHERE c.eid = e.eid
airline_db(# AND a.cruising_range <= 1000
airline_db(# );

```
**Output**
```bash
      ename      
-----------------
 Rahul Sharma
 Priya Singh
 Amit Verma
 Rohit Mehta
 Suresh Iyer
 Vikram Singh
 Aditya Jain
 Arjun Reddy
 Rakesh Kumar
 Simran Kaur
 Deepak Mishra
 Farhan Ali
 Shreya Sen
 Tarun Bansal
 Isha Gupta
 Manish Yadav
 Naveen Kumar
 Kunal Kapoor
 Rajeev Malhotra
 Harsh Vardhan
 Pankaj Tiwari
 Sonal Jain
 Varun Khanna
 Abhishek Sinha
 Gaurav Gupta
 Kritika Sharma
 Captain Robert
 Captain Smith
 Captain Johnson
(29 rows)
```

### m. Print the names of employees who are certified only on aircrafts with cruising range longer than 1000 miles, but on at least two such aircrafts.
**🔗Code**
```bash
airline_db=# SELECT e.ename
airline_db-# FROM Employees e
airline_db-# JOIN Certified c ON e.eid = c.eid
airline_db-# JOIN Aircraft a ON c.aid = a.aid
airline_db-# GROUP BY e.eid, e.ename
airline_db-# HAVING COUNT(*) >= 2
airline_db-# AND NOT EXISTS (
airline_db(# SELECT *
airline_db(# FROM Certified c2
airline_db(# JOIN Aircraft a2 ON c2.aid = a2.aid
airline_db(# WHERE c2.eid = e.eid
airline_db(# AND a2.cruising_range <= 1000
airline_db(# );
```
**Output**
```bash
      ename      
-----------------
 Rahul Sharma
 Priya Singh
 Amit Verma
 Rohit Mehta
 Suresh Iyer
 Vikram Singh
 Arjun Reddy
 Deepak Mishra
 Shreya Sen
 Naveen Kumar
 Kunal Kapoor
 Harsh Vardhan
 Abhishek Sinha
 Gaurav Gupta
 Captain Robert
 Captain Smith
 Captain Johnson
(17 rows)
```
### n. Print the names of employees who are certified only on aircrafts with cruising range longer than 1000 miles and who are certified on some Boeing aircraft.
**🔗Code**
```bash
airline_db=# SELECT DISTINCT e.ename
airline_db-# FROM Employees e
airline_db-# JOIN Certified c ON e.eid = c.eid
airline_db-# JOIN Aircraft a ON c.aid = a.aid
airline_db-# WHERE a.aname LIKE 'Boeing%'
airline_db-# AND NOT EXISTS (
airline_db(# SELECT *
airline_db(# FROM Certified c2
airline_db(# JOIN Aircraft a2 ON c2.aid = a2.aid
airline_db(# WHERE c2.eid = e.eid
airline_db(# AND a2.cruising_range <= 1000
airline_db(# );
```
**Output**
```bash
      ename      
-----------------
 Abhishek Sinha
 Amit Verma
 Arjun Reddy
 Captain Johnson
 Captain Robert
 Captain Smith
 Deepak Mishra
 Gaurav Gupta
 Harsh Vardhan
 Kunal Kapoor
 Naveen Kumar
 Priya Singh
 Rahul Sharma
 Rajeev Malhotra
 Rohit Mehta
 Simran Kaur
 Vikram Singh
(17 rows)
```