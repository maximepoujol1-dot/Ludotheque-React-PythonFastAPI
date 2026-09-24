from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .collection import Collection
from ..core.config import Base

class Items(Base):
    __tablename__ = "items"
    item_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] 
    categorie: Mapped[str] 
    description: Mapped[str] 
    image: Mapped[str] 
    annee: Mapped[str] 
     
    collections: Mapped[List["Collection"]] = relationship("Collection", back_populates="item")

