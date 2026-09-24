from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .collection import CollectionEntry
from ..core.config import Base

class Items(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] 
    categorie: Mapped[str] 
    description: Mapped[str] 
    image: Mapped[str] 
    annee: Mapped[str] 
     
    collection_id: Mapped[int] = mapped_column(ForeignKey("collection.id"),nullable=False)
    collection: Mapped["CollectionEntry"] = relationship(back_populates="items")

