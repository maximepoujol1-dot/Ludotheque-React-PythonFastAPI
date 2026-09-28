from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, Query, status
from ..core.errors import Error
from ..db.session import get_db
from ..schemas.items import Items,ItemsList
from ..services.items_services import (find_item_by_id,get_all_item)
from typing import Annotated
router = APIRouter(prefix="/items", tags=["items"])

@router.get("",summary="recuperer la list des items", response_model=ItemsList, status_code=status.HTTP_200_OK)
async def listItems(q: Annotated[str | None, Query(min_length=2)] = None, categorie: str | None = None, page: int = Query(default=1, ge=1), limit: int = Query(default=12, ge=1, le=50), db: AsyncSession = Depends(get_db),):
    return await get_all_item(db, q=q, categorie=categorie, page=page, limit=limit)

@router.get("/{item_id}",summary="recuperer un item", response_model=Items, status_code=status.HTTP_200_OK)   
async def get_one_item(item_id : int, db : AsyncSession = Depends(get_db)):
    item = await find_item_by_id(item_id, db)
    if item is None :
        raise Error(f"item {item_id} introuvable", status.HTTP_404_NOT_FOUND)
    return item    