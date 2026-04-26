from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from app.config import settings

# Setup bcrypt for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check if the provided password matches the hash in the DB."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Convert a plain password to a secure hash."""
    return pwd_context.hash(password)

def create_access_token(data: dict) -> str:
    """Generate a JWT token for a user."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    # Sign the token using our SECRET_KEY
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
