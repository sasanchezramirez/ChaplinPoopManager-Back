from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Clean(BaseModel):
    id: Optional[int] = None
    date_of_clean: Optional[datetime] = None
    pet_id: Optional[int] = None

class CleanList(BaseModel):
    pets: list[Clean]