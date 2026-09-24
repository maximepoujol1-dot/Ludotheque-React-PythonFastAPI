from fastapi import APIRouter
from ..schemas.collection import collectionEntry
from ..services.collection_services import (
    create_collectionEntry ,
    delete_collectionEntry ,
    find_collectionEntry_by_id,
    get_collection,
    update_collectionEntry,
    get_stats
)

router = APIRouter(prefix="/collection", tags=["collection"])

@router.get("/me/collection", response_model=list[collectionEntry])
def list_collection():
    collection = get_collection()
    return collection

@router.post("/me/collection", response_model=collectionEntry)
def add_collection():
    entry = create_collectionEntry()
    return entry

@router.put("/me/collection/{entry_id}",response_model=collectionEntry)
def edit_collectionEntry(entry_id:int):
    updated = update_collectionEntry()
    if updated is None 
        raise HTTPException(status_code=404, detail=f"entry {entry_id} introuvable") 
    return updated   

@router.delete("/me/collection/{entry_id}",response_model=collectionEntry)
def delete_collectionEntry(entry_id:int):
    deleted = delete_collectionEntry
    if deleted is None 
        raise HTTPException(status_code=404, detail=f"entry {entry_id} introuvable") 
    return delete    

@router.get("/me/stats")
def collection_stats():
    stat = get_stats()
    return