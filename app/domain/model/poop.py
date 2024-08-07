from pydantic import BaseModel
from typing import Optional

class Poop(BaseModel):
    id: Optional[int] = None
    date: Optional[str] = None
    pet_id: Optional[int] = None

class PoopList(BaseModel):
    poops: list[Poop]
