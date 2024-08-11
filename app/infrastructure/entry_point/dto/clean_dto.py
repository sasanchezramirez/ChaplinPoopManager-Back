from pydantic import BaseModel
from datetime import datetime

class NewCleanInput(BaseModel):
    pet_id: int


class GetCleanInput(BaseModel):
    id: int
    pet_id: int
    date_of_clean: datetime

class CleanOutput(BaseModel):
    id: int
    pet_id: int
    date_of_clean: datetime

class CleanListOutput(BaseModel):
    cleans: list[CleanOutput]
