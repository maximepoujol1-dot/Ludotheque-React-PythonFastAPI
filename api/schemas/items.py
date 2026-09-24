from pydantic import BaseModel
from typing import Literal

class Item(BaseModel):
    item_id: int
    name: str
    categorie: Literal["fps" , "rpg" , "rts","gestion"]
    description: str
    image: str
    annee: int

class Items(BaseModel):
    listItems : list[Item] = []