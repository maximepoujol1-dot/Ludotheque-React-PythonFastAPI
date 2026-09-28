import datetime as dt
from typing import TYPE_CHECKING
from sqlalchemy import Date,ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db.session import Base

if TYPE_CHECKING:
    from .item import Items
    from .user import Users

class Collection(Base):
    __tablename__ = "collection"
    __table_args__ = (UniqueConstraint("user_id", "item_id", name="uq_collection_user_item"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey("items.id"), nullable=False)
    
    statut: Mapped[str] = mapped_column(String(20), nullable=False)
    date: Mapped[dt.date] = mapped_column(Date, server_default=func.current_date(), nullable=False)
    note: Mapped[int | None] = mapped_column(nullable=True)
    commentaire: Mapped[str | None] = mapped_column(nullable=True)

    user: Mapped["Users"] = relationship("Users", back_populates="collection")
    item: Mapped["Items"] = relationship("Items", back_populates="collection")