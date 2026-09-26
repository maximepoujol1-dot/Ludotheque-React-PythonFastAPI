from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.collection import Collection
from ..schemas.collection import CollectionEntry

async def get_collection(db : AsyncSession):
    statement = select(Collection)
    stat = await db.scalars(statement)
    return list(stat.all())

async def find_collectionEntry_by_id(entry_id: int, db : AsyncSession):
    return await db.get(Collection,entry_id)

async def create_collectionEntry(newEntry: CollectionEntry, db: AsyncSession):
    entry = Collection(
        statut=newEntry.statut,
        note=newEntry.note,
        commentaire=newEntry.commentaire,
        item_id=newEntry.item_id,
        categorie=newEntry.categorie,
        date=newEntry.date,
    )

    db.add(entry)
    await db.commit()
    await db.refresh(entry)
    return entry


async def update_collectionEntry(entry_id: int, newEntry: CollectionEntry, db: AsyncSession):
    entry = await db.get(Collection, entry_id)
    if entry is None:
        return None
    entry.statut = newEntry.statut
    entry.note = newEntry.note
    entry.commentaire = newEntry.commentaire

    await db.commit()
    await db.refresh(entry)
    return entry

async def delete_collectionEntry(entry_id: int, db: AsyncSession):
    entry = await db.get(Collection, entry_id)
    if entry is None:
        return None
    await db.delete(entry) 
    await db.commit()
    return entry

async def get_stats(db: AsyncSession):
    status_statement = select(Collection.statut, func.count(Collection.collection_id)).group_by(Collection.statut)
    status_rows = (await db.execute(status_statement)).all()
    note_statement = select(func.avg(Collection.note))
    average_note = await db.scalar(note_statement)
    return {
        "total": sum(count for _, count in status_rows),
        "par_statut": {statut: count for statut, count in status_rows},
        "note_moyenne": float(average_note) if average_note is not None else None,
    }