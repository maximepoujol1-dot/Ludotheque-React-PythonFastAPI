from pydantic import BaseModel, EmailStr, Field
from .collection import CollectionEntry

class UserInput(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=72)


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    
UserResponse.model_rebuild()          