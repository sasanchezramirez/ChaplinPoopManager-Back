from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Poop(BaseModel):
    id: Optional[int] = None
    date: Optional[datetime] = None
    pet_id: Optional[int] = None

class PoopList(BaseModel):
    poops: list[Poop]
