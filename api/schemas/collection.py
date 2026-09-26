from pydantic import BaseModel, Field
from .items import Items
from datetime import date
from typing import Literal

Status = Literal["a_decouvrir", "en_cours", "termine"]
Category = Literal["fps", "rpg", "rts", "gestion"]

class CollectionEntry(BaseModel):
    collection_id: int
    item: Items
    statut: Status
    date: date
    categorie: Category
    note: float | None = None
    commentaire: str | None = None

    model_config = {"from_attributes": True}

class CollectionUpdate(BaseModel):
    statut: Status | None = None
    note: float | None = None
    commentaire: str | None = None

class CollectionCreate(BaseModel):
    user_id: int
    item_id: int
    statut: Status
    date: date = Field(default_factory=date.today)
    note: float | None = None
    commentaire: str | None = None

class CollectionStats(BaseModel):
    total: int
    par_statut: dict[str, int]
    note_moyenne: float | None
