from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.item import Items

async def find_item_by_id(item_id : int, db: AsyncSession):
    return await db.get(Items,item_id)

async def get_all_item(db: AsyncSession):
    statement = select(Items)
    result = list(await db.scalars(statement).all())
    return {total,page,limit,results}