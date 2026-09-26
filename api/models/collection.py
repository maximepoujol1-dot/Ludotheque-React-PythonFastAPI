from datetime import date
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db.session import Base

if TYPE_CHECKING:
    from .item import Items
    from .user import Users

class Collection(Base):
    __tablename__ = "collection"
    
    collection_id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey("items.item_id"), nullable=False)
    
    statut: Mapped[str]
    date: Mapped[date]
    categorie: Mapped[str]
    note: Mapped[float]
    commentaire: Mapped[str]

    user: Mapped["Users"] = relationship("Users", back_populates="collection")
    item: Mapped["Items"] = relationship("Items", back_populates="collection")