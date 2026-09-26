from pydantic import BaseModel
from typing import Literal

class Items(BaseModel):
    item_id: int
    name: str
    categorie: Literal["fps" , "rpg" , "rts","gestion"]
    description: str
    image: str
    annee: int

    model_config = {"from_attributes": True}