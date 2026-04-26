from pydantic import BaseModel, EmailStr, Field

# Base properties for a user
class UserBase(BaseModel):
    email: EmailStr  # Automatically validates that the string is a valid email format

# Used when a user is registering
class UserCreate(UserBase):
    # Enforces strong passwords
    password: str = Field(min_length=8, description="Password must be at least 8 characters")

# Used when we return a user to the client (hides password!)
class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True  # Tells Pydantic to read data from our SQLAlchemy model
