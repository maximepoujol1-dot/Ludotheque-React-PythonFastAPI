@app.get("/me/collection")
def get_collection():
    return

@app.post("/me/collection")
def add_collection():
    return

@app.patch("/me/collection/{entry_id}")
def edit_collection():
    return

@app.delete("/me/collection/{entry_id}")
def remove_collection_game(entry_id:int):
    return

@app.get("/me/collection/stats")
def get_stat_collection():
    return
