from pydantic import BaseModel
from datetime import date

class NewCleanInput(BaseModel):
    pet_id: int


class GetCleanInput(BaseModel):
    pet_id: int


class CleanOutput(BaseModel):
    id: int
    pet_id: int
    date_of_clean: date

class CleanListOutput(BaseModel):
    cleans: list[CleanOutput]
