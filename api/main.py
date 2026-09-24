from fastapi import FastAPI
from routers import auth_routes, items_routes, collection_routes
from db.session import Base, engine
from core import error

app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(items_routes.router)
app.include_router(collection_routes.router)
app.include_router(error.router)

@app.get("/")
async def read_root():
    return {"message": "Bonjour"}

Base.metadata.create_all(engine)    