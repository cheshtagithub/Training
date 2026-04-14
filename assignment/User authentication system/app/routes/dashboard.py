from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.models.user import User


router = APIRouter(tags=["Dashboard"])


@router.get("/dashboard")
def read_dashboard(current_user: User = Depends(get_current_user)) -> dict[str, str]:
    # Only authenticated users can reach this route.
    return {"message": f"Welcome, {current_user.name}"}
