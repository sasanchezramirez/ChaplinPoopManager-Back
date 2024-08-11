from app.infrastructure.driven_adapter.persistence.entity.poop_managment_entity import PoopManagmentEntity
from app.domain.model.clean import Clean


def map_clean_to_poop_management_entity(clean: Clean) -> PoopManagmentEntity:
    return PoopManagmentEntity(
        id=clean.id,
        date=clean.date,
        pet_id=clean.pet_id
    )

def poop_management_entity_to_clean(poop: PoopManagmentEntity) -> Clean:
    return Clean(
        id=poop.id,
        date=poop.date,
        pet_id=poop.pet_id
    )




