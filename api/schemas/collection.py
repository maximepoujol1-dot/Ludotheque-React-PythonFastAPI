from pydantic import BaseModel
from .items import Items
from datetime import date
from typing import Literal

class CollectionEntry(BaseModel):
    collection_id : int
    item : Items
    statut: Literal["a_decouvrir" , "en_cours" , "termine"] 
    date: date
    categorie : Literal["fps" , "rpg" , "rts","gestion"]
    note: float | None = None
    commentaire: str | None = None

    model_config = {"from_attributes": True}
