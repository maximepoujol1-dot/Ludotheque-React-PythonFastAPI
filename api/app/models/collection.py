from datetime import date
from .item import Item
from .statut import Statut
from .categorie import Categorie
from typing import Literal

class Collection:
    jeu: Item
    statut: Literal["a_decouvrir" , "en_cours" , "termine"]
    date: date
    categorie : Literal["fps" , "rpg" , "rts","gestion"]
    note: float | None
    commentaire: str | None




