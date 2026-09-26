from sqlalchemy import select
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
    statement = select(Collection.note)
    note = await db.scalars(statement)
    all_note = note.all()
    if len(all_note) == 0:
        return 0
    stats = sum(all_note) / len(all_note)
    return stats