from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.user import Users

async def get_user(email: str, db : AsyncSession):
    statement = select(Users).where(Users.email == email)
    user = await db.scalars(statement)  
    return user.first()  

async def verif_user_mail(email: str, db : AsyncSession):
    return await get_user(email, db) is not None