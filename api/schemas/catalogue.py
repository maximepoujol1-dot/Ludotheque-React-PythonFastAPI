from pydantic import BaseModel

from api.models.item import Item


class CatalogueInput(BaseModel):
    name: str | None = None


class CatalogueOutput(BaseModel):
    items: list[Item]