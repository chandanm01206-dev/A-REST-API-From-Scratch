from fastapi import APIRouter, Depends
from app.models.user import User
from app.schemas.user import UserResponse
from app.api.dependencies import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    """
    Because of the Depends(get_current_user) injection:
    1. FastAPI checks for the Authorization header.
    2. It extracts the JWT token.
    3. It decodes the token.
    4. It fetches the user from the database.
    5. If any step fails, it returns a 401 Error automatically.
    """
    return current_user
