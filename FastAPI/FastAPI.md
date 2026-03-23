# What is API
APIs are mechanisms that enable two software components-such as the frontend and backend of an application- to communicate with each other using a defined set of rules, protocols, and data formats.

# What is FastAPI
FastAPI = Framework to build APIs using Python  
API = a way for frontend / apps to talk to backend  
Example:  
App asks: Give me user data 
FastAPI backend sends response (JSON)  

FastAPI is built on two important libraries:   Starlette and Pydantic.

**1. Starlette**

Starlette is a lightweight ASGI web framework/toolkit used for building async web services in Python.  
FastAPI uses Starlette for the web part of the application.

##### What Starlette handles
Starlette manages things like:  
🔹 Routing (URLs)  
🔹 HTTP requests & responses  
🔹 Middleware  
🔹 WebSockets  
🔹 Background tasks  
🔹 Async support  

**2. Pydantic**

Pydantic is a library used for data validation and data parsing using Python type hints.  
FastAPI uses Pydantic to validate incoming request data automatically.

##### What Pydantic does
🔹 Data validation  
🔹 Data parsing  
🔹 Type checking  
🔹 Serialization (convert Python -> JSON)  
🔹 Automatic API schema generation


## Why FastAPI is popular
🔹 Very fast  
🔹 Easy to learn (Python-based)  
🔹 Automatic API docs (big advantage)  
🔹 Used in ML + Data projects  
🔹 Supports async programming  
🔹 Easy to build REST APIs  

## Installation
Create Virtual Environment
```bash
python -m venv fastapi-env
```

Activate
```bash
source fastapi-env/bin/activate
```

Install FastAPI and Uvicorn
```bash
pip install fastapi uvicorn
```

**What is Uvicorn**
Uvicorn is an ASGI server used to run FastAPI applications.

Run server
```bash
uvicorn main:app --reload
```
Meaning:  
```bash
Part	  |   Meaning
----------+------------------------------------------
main	  |   Python file name
app	      |   FastAPI object
--reload  |   Auto restart server when code changes
```

## HTTP Methods in FastAPI
HTTP methods define what action the client wants to perform on the server.  
They are used in APIs to perform CRUD operations.

CRUD meaning:
```bash
Operation   |   Meaning
------------+-------------
Create	    | Add new data
Read	    | Get data
Update	    | Modify data
Delete	    | Remove data
```

### 1. GET Method
**Definition:**GET is used to retrieve data from the server.

Example Uses:  
🔹 Get list of users  
🔹 Get product details  
🔹 Get order information  

**Example:**
```bash
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@app.get("/users")
def get_users():
    return {"message": "List of users"}
```

### 2. POST Method
**Definition:**POST is used to create new data on the server.

Example Uses:  
🔹 Add new user  
🔹 Create order  
🔹 Register account  

### 3. PUT Method
**Definition:** PUT is used to update existing data completely.

Example Uses:  
🔹 Update user details  
🔹 Replace a product record

### 4. PATCH Method
**Definition:** PATCH is used to update only part of the data.

Example Uses:  
🔹 Update only email  
🔹 Update user password

### 5. DELETE Method
**Definition:** DELETE is used to remove data from the server.

Example Uses:  
🔹 Delete user  
🔹 Delete order  
🔹 Remove product

### Summary Table
```bash
Method |     Purpose       |  CRUD
-------+-------------------+-------------
GET    | Retrieve data     |  Read
POST   | Create data       |  Create
PUT    | Update full data  |  Update
PATCH  |Update partial data|  Update
DELETE | Remove data        |  Delete
```

##  Parameters in FastAPI
When a client sends a request, it often sends extra information with the URL.   
These extra values are called parameters.

There are two main types:
```bash
Type           | Where it appears |  Example
---------------+------------------+----------
Path Parameter | Inside URL path  | /users/10
Query Parameter| After ? in URL   | /users?name=Rahul
```

### 1️⃣ Path Parameters
A Path Parameter is a value inside the URL path.  
**Example URL:**
```bash
/users/3
```
Here:
```bash
3 = path parameter
```
It usually represents IDs or indexes.

### 2️⃣ Query Parameters
Query parameters appear after ? in the URL.  
**Example:**
```bash
/search?name=rahul
```
Here:
```bash
name = query parameter
```

### path vs query
```bash
Feature  |  Path Parameter  |  Query Parameter
---------+------------------+-------------------
Location |  Inside URL      |  After ?
Example  |  /users/10       |  /users?limit=10
Use Case | Identify resource|  Filtering / searching
```
