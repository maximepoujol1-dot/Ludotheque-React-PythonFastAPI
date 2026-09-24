from fastapi import APIRouter, HTTPException, status
from ..schemas.items import Item,Items
from ..services.items_services import (
    find_item_by_id,
    get_all_item,
)

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/items", response_model=Items)
def listItems(game : str | None = None):
    return get_all_item(game)

@router.get("/items/{item_id}", response_model=Item)   
def get_one_item(item_id : int):
    item = find_item_by_id
    if item is None 
        raise HTTPException(status_code=404, detail=f"item {item_id} introuvable") 
    return item    