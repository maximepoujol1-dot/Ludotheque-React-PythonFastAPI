from ..services.collection_services import (
    delete_collection_by_id,
    get_collection,
    get_stats,
    patch_collection_by_id,
    post_collection,
)


@app.get("/me/collection")
async def get_collection():
    return

@app.post("/me/collection")
async def add_collection():
    return

@app.patch("/me/collection/{entry_id}")
async def edit_collection():
    return

@app.delete("/me/collection/{entry_id}")
async def remove_collection_game(entry_id:int):
    return

@app.get("/me/collection/stats")
async def get_stat_collection():
    return
