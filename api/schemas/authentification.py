from pydantic import BaseModel

from api.models.me import Me


class AuthInput(BaseModel):
    email: str
    password: str


class AuthOutput(AuthInput):
    uuid: str
    email: str
    me: Me