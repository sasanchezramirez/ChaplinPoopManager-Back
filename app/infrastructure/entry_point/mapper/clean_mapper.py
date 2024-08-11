from app.domain.model.clean import Clean
from app.infrastructure.entry_point.dto.clean_dto import NewCleanInput, GetCleanInput, CleanOutput, CleanListOutput

def map_clean_dto_to_clean(clean_dto: NewCleanInput) -> Clean:
    return Clean(
        pet_id=clean_dto.pet_id
    )


def map_clean_to_clean_dto(clean: Clean) -> CleanOutput:
    return CleanOutput(
        id=clean.id,
        pet_id=clean.pet_id,
        date_of_clean=clean.date_of_clean
    )


def  map_clean_list_to_clean_list_output_dto(clean_list: list[Clean]) -> CleanListOutput:
    return CleanListOutput(
        cleans=[map_clean_to_clean_dto(clean) for clean in clean_list]
    )

