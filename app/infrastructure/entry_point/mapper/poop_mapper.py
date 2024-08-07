from app.domain.model.poop import Poop, PoopList
from app.infrastructure.entry_point.dto.poop_dto import PoopOutput, PoopListOutput, GetPoopInput, NewPoopInput

def map_poop_dto_to_poop(poop_dto: NewPoopInput) -> Poop:
        return Poop(
            pet_id=poop_dto.pet_id
        )

def map_get_poop_dto_to_poop(get_poop_dto: GetPoopInput) -> Poop:
    return Poop(
        pet_id=get_poop_dto.pet_id
    )

def map_poop_to_poop_output_dto(poop: Poop) -> PoopOutput:
    return PoopOutput(
        id=poop.id,
        pet_id=poop.pet_id,
        date=poop.date
    )

def  map_poop_list_to_poop_list_output_dto(poop_list: PoopList) -> PoopListOutput:
    return PoopListOutput(
        poops=[map_poop_to_poop_output_dto(poop) for poop in poop_list.poops]
    )
