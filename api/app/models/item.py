from typing import Literal

class Item:
    item_id: int
    name: str
    categorie: Literal["fps" , "rpg" , "rts","gestion"]
    description: str
    image: str
    annee: int
