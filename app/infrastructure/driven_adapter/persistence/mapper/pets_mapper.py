from app.infrastructure.driven_adapter.persistence.entity.pets_entity import PetsEntity
from app.domain.model.pets import Pet

def map_pets_entity_to_pet(pets_entity: PetsEntity) -> Pet:
    return Pet(
        id=pets_entity.id,
        pet_name=pets_entity.pet_name,
        user_id=pets_entity.user_id,
        birthday=pets_entity.birthday,
        profile_url=pets_entity.profile_url
    )

def map_pet_to_pets_entity(pet: Pet) -> PetsEntity:
    return PetsEntity(
        id=pet.id,
        pet_name=pet.pet_name,
        user_id=pet.user_id,
        birthday=pet.birthday,
        profile_url=pet.profile_url
    )