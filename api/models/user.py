from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db.session import Base
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .collection import Collection


#user table
class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] 
    fullname: Mapped[str]
    password_hash: Mapped[str] 
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    disabled: Mapped[bool] = mapped_column(default=False, nullable=False)

    collection: Mapped[List["Collection"]] = relationship("Collection", back_populates="user")


    
