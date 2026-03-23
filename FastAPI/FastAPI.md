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

