from pydantic import BaseModel
from datetime import datetime

class NewPetInput(BaseModel):
    pet_name: str
    user_id: int
    birthday: datetime
    profile_image: str

class GetUserPetsInput(BaseModel):
    user_id: int

class GetPetsInput(BaseModel):
    pet_id: int

class PetOutput(BaseModel):
    id: int
    pet_name: str
    user_id: int
    birthday: datetime
    profile_image: str

class PetListOutput(BaseModel):
    pets: list[PetOutput]