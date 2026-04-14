from pydantic import BaseModel, Field


class SignupRequest(BaseModel):
    # Name sent by the client for the new user account.
    name: str

    # Email used as the unique login/identity field.
    email: str

    # Password must be at least 8 characters long.
    password: str = Field(..., min_length=8)


class LoginRequest(BaseModel):
    # Email used to identify the user during login.
    email: str

    # Raw password sent by the client for verification.
    password: str


class ForgotPasswordRequest(BaseModel):
    # Email of the account that needs a password reset link.
    email: str


class ResetPasswordRequest(BaseModel):
    # JWT reset token sent in the email link.
    token: str

    # New password that will replace the current one.
    new_password: str = Field(..., min_length=8)
