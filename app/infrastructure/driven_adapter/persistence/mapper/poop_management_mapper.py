from app.infrastructure.driven_adapter.persistence.entity.poop_management_entity import PoopManagementEntity
from app.domain.model.clean import Clean


def map_clean_to_poop_management_entity(clean: Clean) -> PoopManagementEntity:
    return PoopManagementEntity(
        id=clean.id,
        date_of_clean=clean.date_of_clean,
        pet_id=clean.pet_id
    )

def poop_management_entity_to_clean(poop: PoopManagementEntity) -> Clean:
    return Clean(
        id=poop.id,
        date_of_clean=poop.date_of_clean,
        pet_id=poop.pet_id
    )




