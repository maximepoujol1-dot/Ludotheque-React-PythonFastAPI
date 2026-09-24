from typing import TYPE_CHECKING, List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .collection import CollectionEntry
from ..core.config import Base

#user table
class User(Base):
    __tablename__ = "user"
    uuid: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] 
    fullname: Mapped[str]
    password: Mapped[str] 
    email: Mapped[str]

    collections: Mapped[List["CollectionEntry"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    
