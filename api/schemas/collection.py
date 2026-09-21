from pydantic import BaseModel

from api.models.collection import CollectionGame


class CollectionInput(BaseModel):
    collection: list[CollectionGame]


class CollectionOutput(CollectionInput):
    id: int
