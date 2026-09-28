from pydantic import BaseModel, Field
from .items import Items
from datetime import date as Date
from typing import Literal

Status = Literal["a_decouvrir", "en_cours", "termine"]
Category = Literal["fps", "rpg", "rts", "gestion"]

class CollectionEntry(BaseModel):
    id: int
    item: Items
    statut: Status
    date: Date  = Field(default_factory=Date.today)
    note: int | None = None
    commentaire: str | None = None

    model_config = {"from_attributes": True}

class CollectionUpdate(BaseModel):
    statut : Status | None = None
    note : int | None = Field(default=None, ge=0, le=5)
    commentaire : str | None = None

class CollectionCreate(BaseModel):
    item_id: int
    statut: Status = "a_decouvrir"
    note: int | None = Field(default=None, ge=0, le=5)
    commentaire: str | None = None

class CollectionStats(BaseModel):
    total: int
    par_statut: dict[str, int]
    note_moyenne: float | None
