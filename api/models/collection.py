from datetime import date
from .item import Item


class CollectionGame:
    jeu: Item
    statut: Statut
    date: date
    note: float | None
    commentaire: str | None