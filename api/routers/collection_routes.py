from typing import Annotated, Literal
from ..models.user import Users as User
from ..dependencies.auth import get_current_active_user
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..core.errors import Error
from ..db.session import get_db
from ..schemas.collection import CollectionStats, CollectionEntry, CollectionCreate, CollectionUpdate, Status
from ..services.collection_services import (
    create_collectionEntry ,
    delete_collectionEntry ,
    get_collection,
    update_collectionEntry,
    get_stats
)

router = APIRouter(prefix="/me/collection", tags=["collection"])
stats_router = APIRouter(prefix="/me", tags=["collection"]) 

@router.get("",summary="recuperer la collection", response_model=list[CollectionEntry], status_code=status.HTTP_200_OK)
async def list_collection(current_user: Annotated[User, Depends(get_current_active_user)],statut : Status | None = None ,tri: Literal["date", "note"] = "date", db : AsyncSession = Depends(get_db),):
    collection = await get_collection(current_user.id, statut, tri,db)
    return collection


@router.post("",summary="ajouter une entry de la collection", response_model=CollectionEntry, status_code=status.HTTP_201_CREATED)
async def add_collection(current_user: Annotated[User, Depends(get_current_active_user)], entryElt : CollectionCreate, db: AsyncSession = Depends(get_db),):
    entry = await create_collectionEntry(current_user.id, entryElt.item_id, entryElt.statut, entryElt.note, entryElt.commentaire, db)
    if entry is None :
        raise Error("entry introuvable", status.HTTP_404_NOT_FOUND)
    if entry == 0 :
        raise Error("item deja dans la collection", status.HTTP_409_CONFLICT) 
    return entry

@router.patch("/{entry_id}",summary="modifier une entry de la collection",response_model=CollectionEntry, status_code=status.HTTP_200_OK)
async def edit_collectionEntry(current_user: Annotated[User, Depends(get_current_active_user)],entry_id: int, edit: CollectionUpdate , db: AsyncSession = Depends(get_db),):
    updated = await update_collectionEntry(current_user.id, entry_id, edit.statut, edit.note, edit.commentaire, db)
    if updated is None :
        raise Error(f"entry {entry_id} introuvable", status.HTTP_404_NOT_FOUND)
    return updated 

@router.delete("/{entry_id}",summary="supprimer une entry de la collection", status_code=status.HTTP_204_NO_CONTENT)
async def delete_collection(current_user: Annotated[User, Depends(get_current_active_user)],entry_id:int, db : AsyncSession = Depends(get_db),):
    deleted = await delete_collectionEntry(current_user.id, entry_id, db)
    if deleted is None :
        raise Error(f"entry {entry_id} introuvable", status.HTTP_404_NOT_FOUND)
    return  

@router.get("/stats",summary="obtenir les stats de la collection", response_model=CollectionStats, status_code=status.HTTP_200_OK) 
async def collection_stats(current_user: Annotated[User, Depends(get_current_active_user)],db : AsyncSession = Depends(get_db),):
    stat = await get_stats(db, current_user.id)
    return stat