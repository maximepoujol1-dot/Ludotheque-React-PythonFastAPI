from fastapi import FastAPI
from .models.user import Users
from .models.item import Items
from .models.collection import Collection
from .routers import auth_routes, items_routes, collection_routes
from .db.session import create_table
from .core import errors
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app : FastAPI):
    print("created")
    create_table()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth_routes.router)
app.include_router(items_routes.router)
app.include_router(collection_routes.router)
app.include_router(errors.router)

@app.get("/")
async def root():
    return {"root": "hello world"}

@app.get("/health")
async def health_check():
    return {"status": "running..."}

