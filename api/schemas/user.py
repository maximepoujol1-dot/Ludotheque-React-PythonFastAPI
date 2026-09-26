from pydantic import BaseModel, EmailStr, Field
from .collection import CollectionEntry

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    fullname: str


class UserResponse(BaseModel):
    id: int
    username: str
    fullname: str
    email: EmailStr
    collection: list[CollectionEntry] = Field(default_factory=list)
    disabled: bool

    model_config = {"from_attributes": True}
    

class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    fullname: str | None = None
    collection: list[CollectionEntry] = Field(default_factory=list)

    model_config = {"from_attributes": True}

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: int | None = None    