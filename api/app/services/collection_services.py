from datetime import date
from ..schemas.collection import CollectionGame
from ..schemas.items import Item

fake_collection = [
    {
        "id": 1,
        "item": {
            "item_id": 1,
            "name": "The Witcher 3",
            "categorie": "rpg",
            "description": "Un jeu de role en monde ouvert.",
            "image": "/images/the-witcher-3.jpg",
            "annee": 2015,
        },
        "statut": "en_cours",
        "date": date(2026, 9, 1),
        "categorie": "rpg",
        "note": 4.5,
        "commentaire": "Une grande aventure.",
    },
    {       
        "id": 2,
        "item": {
            "item_id": 2,
            "name": "Age of Empires IV",
            "categorie": "rts",
            "description": "Un jeu de strategie en temps reel.",
            "image": "/images/age-of-empires-iv.jpg",
            "annee": 2021,
        },
        "statut": "en_cours",
        "date": date(2026, 9, 1),
        "categorie": "rts",
        "note": 4.5,
        "commentaire": "Une grande aventure.",
    }
]

def get_collection(game : str | None):
    if game is None :
        return fake_collection
    return [g for g  in fake_collection if g["name"].lower() == artist.lower()]    

def post_collection(data: list[CollectionGame]):
    new_id = max((g["id"] for g in fake_collection), default=0) + 1
    game = {"id": new_id, **data.model_dump()}
    fake_collection.append(game)
    return game

def patch_collection_by_id(game_id: int, data: list[CollectionGame]):
    for index, game in enumerate(fake_collection):
        if game["id"] == game_id:
            updated = {"id": game_id, **data.model_dump()}
            fake_collection[index] = updated
            return updated
    return None

def delete_collection_by_id(game_id: int):
    for index, game in enumerate(fake_collection):
        if game["id"] == game_id:
            return fake_collection.pop(index)
    return None


def get_stats(game_id: int):
    for index, game in enumerate(fake_collection):
        if game["id"] == game_id:
            return [
                {
                    "statut": game["statut"],
                    "date": game["date"],
                    "categorie": game["categorie"],
                    "note": game["note"],
                    "commentaire": game["commentaire"],
                }
            ]

    