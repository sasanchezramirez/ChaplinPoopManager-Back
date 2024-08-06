from pydantic import BaseModel

class NewPoopInput(BaseModel):
    pet_id: int