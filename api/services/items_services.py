from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.item import Items

async def find_item_by_id(item_id : int, db: AsyncSession):
    return await db.get(Items,item_id)

async def get_all_item(db: AsyncSession,q: str | None = None, categorie: str | None = None, page: int = 1, limit: int = 12):
    query = select(Items)      

    if categorie : 
        query = query.where(Items.categorie == categorie)

    if q :
        query = query.where(Items.titre.ilike(f"%{q}%"))    

    count = select(func.count()).select_from(query.subquery())
    total_result = await db.execute(count)
    total = total_result.scalar_one()

    pagination = (page - 1) * limit
    statement = query.order_by(Items.id).offset(pagination).limit(limit)
    result = await db.scalars(statement)
    return {
        "total": total or 0,
        "page": page,
        "limit": limit,
        "results": result.all(),
    }