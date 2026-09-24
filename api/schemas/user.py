from pydantic import BaseModel
from .collection import CollectionEntry

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    fullname: str
    disabled : bool


class UserResponse(BaseModel):
    uuid: str
    username: str
    email: str
    fullname: str
    collection: list[CollectionEntry] = []

