from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter,  Depends, HTTPException, status
from ..db.session import get_db
from ..schemas.items import Items
from ..services.items_services import (find_item_by_id,get_all_item)

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model={total, page, limit, results : List[Items]}, status_code:..HTTP_200_OK)
def listItems(db : AsyncSession = Depends(get_db)):
    total = 0
    page = 0
    limit = 0
    results = await get_all_item(db)
    return {total, page, limit, results}

@router.get("/{item_id}", response_model=Items, status_code.status.HTTP_200_OK)   
def get_one_item(item_id : int, db : AsyncSession = Depends(get_db)):
    item = await find_item_by_id(item_id, db)
    if item is None :
        raise HTTPException(status_code=404, detail=f"item {item_id} introuvable") 
    return item    