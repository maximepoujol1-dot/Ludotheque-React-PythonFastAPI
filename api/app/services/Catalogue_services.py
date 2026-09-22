
from ..schemas.items import Item


fake_item = [
    {
        item_id=1,
        name="The Witcher 3",
        categorie="rpg",
        description="Un jeu de role en monde ouvert.",
        image="/images/the-witcher-3.jpg",
        annee=2015,
    },{
    
        item_id=2,
        name="Age of Empires IV",
        categorie="rts",
        description="Un jeu de strategie en temps reel.",
        image="/images/age-of-empires-iv.jpg",
        annee=2021,
    }
]

def get_all_item(game : str | None):
    if game is None :
        return fake_item
    return [g for g  in fake_item if g["name"].lower() == artist.lower()]    

def find_item_by_id(item_id: int):
    return next((g for g in fake_item if c["id"] == item_id), None) 

