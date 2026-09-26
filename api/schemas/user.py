from pydantic import BaseModel, EmailStr, Field
from typing import Union
from .collection import CollectionEntry

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    fullname: str
    disabled : bool


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    fullname: str
    collection: list[CollectionEntry] = Field(default_factory=list)
    disabled: bool

    model_config = {"from_attributes": True}
    

class UserUpdate(BaseModel):
    id: int
    username: str | None = None
    email: EmailStr | None = None
    fullname: str | None = None
    collection: list[CollectionEntry] = Field(default_factory=list)

    model_config = {"from_attributes": True}

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserToken(BaseModel):
    token: str    

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None    