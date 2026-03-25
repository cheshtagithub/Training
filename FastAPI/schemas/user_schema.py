from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(gt=0, lt=100)
    phone: str = Field(min_length=10, max_length=10)
    password: str = Field(min_length=8)
    is_active: bool = True