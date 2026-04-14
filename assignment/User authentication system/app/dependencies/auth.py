from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.db.database import get_db
from app.models.user import User
from app.utils.security import ALGORITHM


# Reads the Bearer token from the Authorization header.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    settings = get_settings()

    try:
        # Decode the token using the secret key and algorithm.
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])

        # Extract the user email stored in the "sub" claim.
        email: str | None = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # Fetch the user from the database using the email from the token.
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception

    return user
