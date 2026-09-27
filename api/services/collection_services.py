from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.collection import Collection
from ..schemas.collection import CollectionEntry

async def get_collection(user_id: int, db: AsyncSession):
    statement = select(Collection).where(Collection.user_id == user_id)
    result = await db.scalars(statement)
    return list(result.all())

async def find_collectionEntry_by_id(user_id: int,entry_id: int, db : AsyncSession):
    statement = select(Collection).where(Collection.user_id == user_id, Collection.collection_id == entry_id)
    result = await db.scalars(statement)
    return result.first()

async def create_collectionEntry(user_id : int, item_id : int, statut : str | None, note :float | None, commentaire : str | None, db: AsyncSession):
    finalStatut = statut
    finalNote = note
    finalCommentaire = commentaire
    if statut is None:    
        finalStatut = "a_decouvrir"
    if note is None:     
        finalNote = 0
    if commentaire is None:    
        finalCommentaire = ""

    entry = Collection(
        user_id=user_id,
        item_id=item_id,
        statut=finalStatut,
        date=date.today(),
        note=finalNote,
        commentaire=finalCommentaire
    )

    db.add(entry)
    await db.commit()
    await db.refresh(entry)
    return entry


async def update_collectionEntry(user_id: int, entry_id: int, statut : str | None, note :float | None, commentaire : str | None, db: AsyncSession):
    entry = await find_collectionEntry_by_id(entry_id, user_id, db)
    if entry is None:
        return None
    if statut :    
        entry.statut = statut
    if note :     
        entry.note = note
    if commentaire :    
        entry.commentaire = commentaire

    await db.commit()
    await db.refresh(entry)
    return entry

async def delete_collectionEntry(user_id: int,entry_id: int, db: AsyncSession):
    entry = await find_collectionEntry_by_id(entry_id, user_id, db)
    if entry is None:
        return None
    await db.delete(entry) 
    await db.commit()
    return entry

async def get_stats(db: AsyncSession,user_id: int):
    status_statement = select(Collection.statut, func.count(Collection.collection_id)).where(Collection.user_id == user_id).group_by(Collection.statut)
    status_rows = (await db.execute(status_statement)).all()
    note_statement = select(func.avg(Collection.note)).where(Collection.user_id == user_id)
    average_note = await db.scalar(note_statement)
    return {
        "total": sum(count for _, count in status_rows),
        "par_statut": {statut: count for statut, count in status_rows},
        "note_moyenne": float(average_note) if average_note is not None else None,
    }