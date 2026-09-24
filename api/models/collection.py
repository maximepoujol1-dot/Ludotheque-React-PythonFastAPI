from typing import List,Optional
from sqlalchemy import Date, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .item import Items
from .user import Users
from ..core.config import Base

class Collection(Base):
    __tablename__ = "collection"
    
    collection_id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id = Column(Integer, ForeignKey("users.uuid"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.item_id"), nullable=False)
    
    statut: Mapped[str]
    date: Mapped[date]
    categorie: Mapped[str]
    note: Mapped[float]
    commentaire: Mapped[str]

    user = relationship("Users", back_populates="collection")
    item = relationship("Items", back_populates="collection")