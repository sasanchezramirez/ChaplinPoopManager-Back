from app.domain.model.pets import Pet, PetList
from app.infrastructure.entry_point.dto.pets_dto import NewPetInput, GetUserPetsInput, GetPetsInput, PetOutput, PetListOutput
from app.domain.model.user import User

def map_pet_dto_to_pet(pet_dto: NewPetInput) -> Pet:
        return Pet(
            pet_name=pet_dto.pet_name,
            user_id=pet_dto.user_id,
            birthday=pet_dto.birthday,
            profile_image=pet_dto.profile_image
        )

def map_pet_to_pet_output_dto(pet: Pet) -> PetOutput:
        return PetOutput(
                id=pet.id,
                pet_name=pet.pet_name,
                user_id=pet.user_id,
                birthday=pet.birthday,
                profile_image=pet.profile_image if pet.profile_image else ""
        )
def map_get_pet_dto_to_pet(pet_dto: GetPetsInput) -> Pet:
        return Pet(
            id=pet_dto.pet_id
        )

def map_pet_list_to_pet_list_output_dto(pet_list: PetList) -> PetListOutput:
        return PetListOutput(
            pets=[map_pet_to_pet_output_dto(pet) for pet in pet_list.pets] 
        )

def map_get_user_pets_dto_to_user(get_user_pets_dto: GetUserPetsInput) -> User:
        return User(
                id=get_user_pets_dto.user_id
        )