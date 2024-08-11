from app.infrastructure.driven_adapter.persistence.entity.poop_management_entity import PoopManagementEntity
from app.domain.model.clean import Clean
from datetime import date


def map_clean_to_poop_management_entity(clean: Clean) -> PoopManagementEntity:
    return PoopManagementEntity(
        id=clean.id,
        date_of_clean=clean.date_of_clean,
        pet_id=clean.pet_id
    )

def poop_management_entity_to_clean(poop_managment_entity: PoopManagementEntity) -> Clean:
    return Clean(
        id=poop_managment_entity.id,
        date_of_clean=date(poop_managment_entity.date_of_clean.year, poop_managment_entity.date_of_clean.month, poop_managment_entity.date_of_clean.day),
        pet_id=poop_managment_entity.pet_id
    )




