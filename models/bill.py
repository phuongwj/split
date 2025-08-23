from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float 
    participants: list[str]

class Bill(BaseModel):
    item: list[Item]
    tax: float = 0.0
    tip: float = 0.0