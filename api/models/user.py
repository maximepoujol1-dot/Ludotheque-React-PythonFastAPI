from typing import TYPE_CHECKING, List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .collection import Collection 
from ..core.config import Base

#user table
class Users(Base):
    __tablename__ = "users"
    uuid: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] 
    fullname: Mapped[str]
    password: Mapped[str] 
    email: Mapped[str]

    collections: Mapped[List["Collection"]] = relationship(
    "Collection",
    back_populates="user"
)


    
