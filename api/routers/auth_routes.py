from datetime import timedelta
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from ..core.config import settings
from ..db.session import get_db
from ..core.errors import Error
from ..dependencies.auth import authenticate_user, get_current_active_user
from ..models.user import Users as User
from ..schemas.user import UserInput, UserResponse
from ..core.security import Token, create_access_token, get_password_hashed
from ..services.user_service import verif_user_mail
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register",summary="creer un nouvel utilisateur",  response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserInput,db: AsyncSession = Depends(get_db)):

    mail = await verif_user_mail(user.email, db)
    if mail :
        raise Error("mail deja présente", status.HTTP_409_CONFLICT)
    newPassword = get_password_hashed(user.password)
    newUser = User(
        email=user.email,
        password_hash=newPassword,
        disabled=False,
    )
    db.add(newUser)
    await db.commit()
    await db.refresh(newUser)

    return newUser

@router.post("/login",summary="connecter un utilisateur",  response_model=Token, status_code=status.HTTP_200_OK)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: AsyncSession = Depends(get_db),):
    
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise Error("Incorrect email or password", status.HTTP_401_UNAUTHORIZED)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@router.get("/me" , summary="recuperer l'utilisateur",response_model=UserResponse, status_code=status.HTTP_200_OK)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)],):
    return current_user
