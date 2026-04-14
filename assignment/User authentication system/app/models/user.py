from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.db.database import Base


class User(Base):
    # SQLAlchemy will create/use the "users" table for this model.
    __tablename__ = "users"

    # Primary key for each user record.
    id = Column(Integer, primary_key=True, index=True)

    # Stores the user's display or full name.
    name = Column(String, nullable=False)

    # Email must be unique and is indexed for faster lookups.
    email = Column(String, unique=True, index=True, nullable=False)

    # Stores the hashed password, never the plain-text password.
    hashed_password = Column(String, nullable=False)

    # Automatically stores when the user record was created.
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
