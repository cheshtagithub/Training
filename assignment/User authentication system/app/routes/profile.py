from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.models.user import User


router = APIRouter(tags=["Profile"])


@router.get("/profile")
def get_profile(current_user: User = Depends(get_current_user)) -> dict[str, str]:
    # The current user is resolved from the JWT token by the auth dependency.
    return {
        "name": current_user.name,
        "email": current_user.email,
    }
