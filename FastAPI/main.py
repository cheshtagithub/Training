# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Hello World"}

# from fastapi import FastAPI

# app = FastAPI()

# users = ["Rahul", "Aman", "Neha"]

# @app.get("/users")
# def get_users():
#     return {"users": users}

# from fastapi import FastAPI

# app = FastAPI()

# users = []

# @app.post("/users")
# def create_user(name: str):
#     users.append(name)
#     return {"message": "User added", "users": users}

# from fastapi import FastAPI

# app = FastAPI()

# users = []

# @app.get("/")
# def home():
#     return {"message": "Hello World"}

# @app.get("/users")
# def get_users():
#     return {"users": users}

# @app.post("/users")
# def create_user(name: str):
#     users.append(name)
#     return {"message": "User added", "users": users}

# @app.put("/users/{user_index}")
# def update_user(user_index: int, name: str):
#     users[user_index] = name
#     return {"message": "User updated", "users": users}

# @app.delete("/users/{user_index}")
# def delete_user(user_index: int):
#     deleted = users.pop(user_index)
#     return {"message": f"{deleted} deleted"}

# @app.get("/")
# def home():
#     return{"message": "Welcome to FastAPI"}

# @app.get("/hello")
# def hello():
#     return{"message": "Hello World"}

# products = ["Laptop", "Phone", "Tablet"]

# @app.get("/products")
# def product_list():
#     return {"products": products}

# @app.post("/products")
# def create_product(name: str):
#     products.append(name)
#     return {"message": "Product added", "products": products}

# @app.put("/products/{product_index}")
# def update_product(product_index: int, name: str):
#     products[product_index] = name
#     return {"message": "Product updated", "products": products}

# @app.delete("/products/{product_index}")
# def delete_product(product_index: int):
#     deleted = products.pop(product_index)
#     return {"message": f"{deleted} deleted"}

# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()

# users = []

# class User(BaseModel):
#     name: str
#     email: str
#     age: int = Field(gt=0)
#     is_active: bool = True


# @app.post("/users")
# def create_user(user: User):
#     users.append(user)

#     return {
#         "message": "User added",
#         "user": user
#     }

# @app.get("/users")
# def get_users():
#     return {"users": users}

from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

users = []

class User(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(gt=0, lt=100)
    phone: str = Field(min_length=10, max_length=10)
    password: str = Field(min_length=8)
    is_active: bool = True


@app.post("/users")
def create_user(user: User):

    users.append(user.model_dump())

    return {
        "message": "User added successfully",
        "user": user
    }


@app.get("/users")
def get_users():

    return {
        "users": users
    }