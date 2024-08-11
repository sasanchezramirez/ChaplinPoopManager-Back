from pydantic import BaseModel
from typing import Optional
from datetime import date

class Clean(BaseModel):
    id: Optional[int] = None
    date_of_clean: Optional[date] = None
    pet_id: Optional[int] = None

class CleanList(BaseModel):
    cleans: list[Clean]