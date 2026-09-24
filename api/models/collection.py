from typing import List,Optional
from sqlalchemy import Date, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .item import Items
from .user import User
from ..core.config import Base

class CollectionEntry(Base):
    __tablename__ = "collection"
    id: Mapped[int] = mapped_column(primary_key=True)
    statut: Mapped[str]
    date: Mapped[date]
    categorie: Mapped[str]
    note: Mapped[float]
    commentaire: Mapped[str]
    
    user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"),nullable=False)
    user: Mapped["User"] = relationship(back_populates="collections")
    items: Mapped[Optional["Items"]] = relationship(back_populates="collection", cascade="all, delete-orphan")
