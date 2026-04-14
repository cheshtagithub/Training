from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.schemas.auth import (
    ForgotPasswordRequest,
    LoginRequest,
    ResetPasswordRequest,
    SignupRequest,
)
from app.utils.email import send_email
from app.utils.security import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    decode_token_email,
)


router = APIRouter(tags=["Authentication"])

# Passlib context handles bcrypt hashing for passwords.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: SignupRequest, db: Session = Depends(get_db)) -> dict[str, str]:
    # Check whether the email is already registered.
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists",
        )

    # Hash the plain password before saving it in the database.
    hashed_password = pwd_context.hash(user.password)

    # Create a new user row using the validated request data.
    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}


@router.post("/login")
def login(user: LoginRequest, db: Session = Depends(get_db)) -> dict[str, str]:
    # Find the user record by email.
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Compare the incoming password with the stored bcrypt hash.
    if not pwd_context.verify(user.password, existing_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Create a JWT token that includes the user's email.
    access_token = create_access_token(
        data={"sub": existing_user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/forgot-password")
def forgot_password(
    user: ForgotPasswordRequest,
    db: Session = Depends(get_db),
) -> dict[str, str]:
    # Check whether the requested email belongs to an existing user.
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    # Create a short-lived reset token that carries the user's email.
    reset_token = create_access_token(
        data={"sub": existing_user.email},
        expires_delta=timedelta(minutes=30),
    )

    reset_link = f"http://localhost:8000/reset-password?token={reset_token}"
    email_subject = "Password Reset"
    email_body = f"Click the link below to reset your password:\n\n{reset_link}"

    # Send the reset link to the user's email address.
    send_email(
        to_email=existing_user.email,
        subject=email_subject,
        body=email_body,
    )

    return {"message": "Password reset link sent to your email"}


@router.post("/reset-password")
def reset_password(
    payload: ResetPasswordRequest,
    db: Session = Depends(get_db),
) -> dict[str, str]:
    # Decode the reset token and extract the user's email.
    email = decode_token_email(payload.token)

    # Fetch the account that matches the email from the token.
    existing_user = db.query(User).filter(User.email == email).first()
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    # Replace the stored password hash with the new password.
    existing_user.hashed_password = pwd_context.hash(payload.new_password)
    db.commit()

    return {"message": "Password updated successfully"}
