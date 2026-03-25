from fastapi import APIRouter
from schemas.user_schema import User

router = APIRouter()

users = []

@router.post("/users")
def create_user(user: User):

    users.append(user.model_dump())

    return {
        "message": "User added",
        "user": user
    }


@router.get("/users")
def get_users():

    return {
        "users": users
    }