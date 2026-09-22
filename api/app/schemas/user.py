from pydantic import BaseModel
from .collection import CollectionGame

class UserInput(BaseModel):
    username: str
    email: str
    password: str
    name: str


class UserOutput(BaseModel):
    uuid: str
    username: str
    email: str
    name: str
    collection: list[CollectionGame] = []

