from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from ..core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_SessionLocal = async_sessionmaker(bind=engine,expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncGenerator[AsyncSession,None]:
  async with async_SessionLocal() as db:
    try:
      yield db
      await db.commit()
    except Exception:
      await db.rollback()
      raise
    finally:
      await db.close()

async def create_table():
  async with engine.begin() as connection:
    await connection.run_sync(Base.metadata.create_all)
