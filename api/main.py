from fastapi import FastAPI
from .models.user import Users
from .models.item import Items
from .models.collection import Collection
from .routers import auth_routes, items_routes, collection_routes
from .db.session import create_table, engine
from .core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app : FastAPI):
    print("created")
    await create_table()
    yield
    print("close")
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_routes.router)
app.include_router(items_routes.router)
app.include_router(collection_routes.router)


