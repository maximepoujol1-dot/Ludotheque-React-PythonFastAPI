from pydantic import BaseModel
from .items import Item
from datetime import date
from typing import Literal

class CollectionGame(BaseModel):
    item : Item
    statut: Literal["a_decouvrir" , "en_cours" , "termine"] 
    date: date
    categorie : Literal["fps" , "rpg" , "rts","gestion"]
    note: float | None
    commentaire: str | None
