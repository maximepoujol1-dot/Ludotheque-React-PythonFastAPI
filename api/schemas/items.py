from pydantic import BaseModel
from typing import Literal

class Items(BaseModel):
    id: int
    titre: str
    categorie: Literal["fps" , "rpg" , "rts","gestion"]
    description: str
    image_url: str
    annee: int
    studio: str
    directeur : str

    model_config = {"from_attributes": True}


class ItemsList(BaseModel):
    total: int 
    page: int
    limit: int
    results: list[Items]