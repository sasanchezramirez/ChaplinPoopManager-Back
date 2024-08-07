from pydantic import BaseModel
from datetime import datetime

class NewPoopInput(BaseModel):
    pet_id: int

class GetPoopInput(BaseModel):
    pet_id: int

class PoopOutput(BaseModel):
    id: int
    pet_id: int
    date: datetime

class PoopListOutput(BaseModel):
    poops: list[PoopOutput]