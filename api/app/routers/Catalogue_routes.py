from ..services.Catalogue_services import (
    find_item_by_id,
    get_all_item,
)


@app.get("/catalogue")
async def list_catalogue():
    return 

@app.get("/catalogue/{item_id}")
async def get_catalogue_game(entry_id:int):
    return 
