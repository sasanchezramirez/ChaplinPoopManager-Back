from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Pet(BaseModel):
    id: Optional[int] = None
    pet_name: Optional[str] = None
    user_id: Optional[int] = None
    birthday: Optional[datetime] = None
    profile_url: Optional[str] = None

class PetList(BaseModel):
    pets: list[Pet]