from pydantic import BaseModel

from .collection import Collection


class Me(BaseModel):
    name: str
    collection: list[Collection]