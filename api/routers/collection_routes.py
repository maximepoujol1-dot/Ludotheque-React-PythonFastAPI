from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..db.session import get_db
from ..schemas.collection import CollectionEntry
from ..services.collection_services import (
    create_collectionEntry ,
    delete_collectionEntry ,
    find_collectionEntry_by_id,
    get_collection,
    update_collectionEntry,
    get_stats
)

router = APIRouter(prefix="/me/collection", tags=["collection"])

@router.get("/", response_model=list[CollectionEntry], status_code.status.HTTP_200_OK)
async def list_collection(db : AsyncSession = Depends(get_db)):
    collection = await get_collection(db)
    return collection

@router.post("/", response_model=CollectionEntry, status_code.status.HTTP_201_CREATED)
async def add_collection(elt: CollectionEntry, db: AsyncSession = Depends(get_db)):
    entry = await create_collectionEntry(elt,db)
    if entry is None :
        raise HTTPException(status_code=404, detail=f"entry introuvable")
    if entry == 0:
        raise HTTPException(status_code=409, detail=f"entry deja présente")
    return entry

@router.patch("/{entry_id}",response_model=CollectionEntry, status_code.status.HTTP_200_OK)
async def edit_collectionEntry(entry_id: int, newEntry: CollectionEntry, db: AsyncSession = Depends(get_db)):
    updated = await update_collectionEntry(entry_id, newEntry, db)
    if updated is None :
        raise HTTPException(status_code=404, detail=f"entry {entry_id} introuvable") 
    return newEntry   

@router.delete("/{entry_id}",response_model=CollectionEntry, status_code.status.HTTP_204_NO_CONTENT)
async def delete_collection(entry_id:int, db : AsyncSession = Depends(get_db)):
    deleted = await delete_collectionEntry(entry_id, db)
    if deleted is None :
        raise HTTPException(status_code=404, detail=f"entry {entry_id} introuvable") 
    return  

@router.get("/stats",{total, par_statut:{}, note_moyenne}, status_code.status.HTTP_200_OK) 
async def collection_stats(db : AsyncSession = Depends(get_db)):
    stat = await get_stats(db)
    return stat