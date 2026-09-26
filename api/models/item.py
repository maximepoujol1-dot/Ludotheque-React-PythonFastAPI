from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db.session import Base
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .collection import Collection

class Items(Base):
    __tablename__ = "items"

    item_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    titre: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    
    categorie: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] 
    image_url: Mapped[str] 
    annee: Mapped[int] 
     
    collection: Mapped[List["Collection"]] = relationship("Collection", back_populates="item")

