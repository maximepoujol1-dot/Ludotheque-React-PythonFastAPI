from typing import Literal

from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ..core.errors import Error
from ..models.collection import Collection
from ..models.item import Items
from ..schemas.collection import CollectionCreate, CollectionUpdate



async def get_collection(user_id: int,statut: str | None,tri: Literal["date", "note"], db: AsyncSession):
    statement = select(Collection).options(selectinload(Collection.item)).where(Collection.user_id == user_id)
    if statut:                                                        
        statement = statement.where(Collection.statut == statut)
    if tri == "note":                                                
        statement = statement.order_by(Collection.note.desc().nulls_last(), Collection.id)
    else:
        statement = statement.order_by(Collection.date.desc(), Collection.id.desc())
    result = await db.scalars(statement)
    return list(result.all())

async def find_collectionEntry_by_id(user_id: int,entry_id: int, db : AsyncSession):
    statement = select(Collection).options(selectinload(Collection.item)).where(Collection.user_id == user_id, Collection.id == entry_id).execution_options(populate_existing=True)
    result = await db.scalars(statement)
    return result.first()

async def create_collectionEntry(user_id : int, item_id : int, statut : str | None, note :float | None, commentaire : str | None, db: AsyncSession):
    if await db.get(Items, item_id) is None:
        return None 
    
    entry = Collection(
        user_id=user_id,
        item_id=item_id,
        statut=statut,
        note=note,
        commentaire=commentaire
    )

    db.add(entry)
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        return 0
    return await find_collectionEntry_by_id(user_id, entry.id, db)


async def update_collectionEntry(user_id: int, entry_id: int, statut : str | None, note :float | None, commentaire : str | None, db: AsyncSession):
    entry = await find_collectionEntry_by_id(user_id, entry_id, db)
    if entry is None:
        return None
    if statut is not None:    
        entry.statut = statut
    if note is not None:     
        entry.note = note
    if commentaire is not None:    
        entry.commentaire = commentaire

    await db.commit()
    return await find_collectionEntry_by_id(user_id, entry_id, db)

async def delete_collectionEntry(user_id: int,entry_id: int, db: AsyncSession):
    entry = await find_collectionEntry_by_id(user_id, entry_id, db)
    if entry is None:
        return None
    await db.delete(entry) 
    await db.commit()
    return True 

async def get_stats(db: AsyncSession,user_id: int):
    status_statement = select(Collection.statut, func.count(Collection.id)).where(Collection.user_id == user_id).group_by(Collection.statut)
    status_rows = (await db.execute(status_statement)).all()
    note_statement = select(func.avg(Collection.note)).where(Collection.user_id == user_id)
    average_note = await db.scalar(note_statement)
    return {
        "total": sum(count for _, count in status_rows),
        "par_statut": {statut: count for statut, count in status_rows},
        "note_moyenne": float(average_note) if average_note is not None else None,
    }