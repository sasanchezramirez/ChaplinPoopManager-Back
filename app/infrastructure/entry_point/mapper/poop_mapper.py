from datetime import datetime
from app.domain.model.poop import Poop
from app.infrastructure.entry_point.dto.user_dto import NewUserInput, GetUser, UserOutput, LoginInput, UpdateUserInput

def map_poop_dto_to_poop(poop_dto: NewUserInput) -> Poop:
        return Poop(
            pet_id=poop_dto.pet_id
        )
