from typing import Annotated
import jwt
from fastapi import Depends, status
from jwt.exceptions import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession
from ..core.errors import Error
from ..core.security import DUMMY_HASH, TokenData, oauth2_scheme, verify_password
from ..db.session import get_db
from ..models.user import Users as User
from ..services.user_service import get_user
from ..core.config import settings


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],db: AsyncSession = Depends(get_db),):
    credentials_exception = Error("Could not validate credentials", status.HTTP_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception
    user = await get_user(token_data.email, db)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise Error("Inactive user", status.HTTP_400_BAD_REQUEST)
    return current_user


async def authenticate_user(db: AsyncSession, email: str, password: str):
    user = await get_user(email, db)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user
