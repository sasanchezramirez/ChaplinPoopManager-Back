from app.infrastructure.driven_adapter.persistence.entity.poop_entity import PoopEntity
from app.domain.model.poop import Poop


def map_poop_entity_to_poop(poop_entity: PoopEntity) -> Poop:
    return Poop(
        id=poop_entity.id,
        date=poop_entity.date,
        pet_id=poop_entity.pet_id
    )

def map_poop_to_poop_entity(poop: Poop) -> PoopEntity: 
    return PoopEntity(
        id=poop.id,
        date=poop.date,
        pet_id=poop.pet_id
    )



