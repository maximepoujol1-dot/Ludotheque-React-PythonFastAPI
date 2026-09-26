from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.user import Users
from ..schemas.user import UserResponse

async def get_user(username: str, db : AsyncSession):
    statement = select(Users).where(Users.username == username)
    user = await db.scalars(statement).first()    
    return user