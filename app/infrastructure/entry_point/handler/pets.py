import logging

from fastapi import APIRouter, Depends 
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.infrastructure.entry_point.dto.response_dto import ResponseDTO
from app.infrastructure.entry_point.utils.api_response import ApiResponse
from app.application.container import Container
from app.domain.usecase.util.jwt import get_current_user
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.usecase.pets_usecase import PetsUseCase
from app.infrastructure.entry_point.dto.pets_dto import GetUserPetsInput, NewPetInput
from app.infrastructure.entry_point.mapper import pets_mapper
from app.infrastructure.entry_point.mapper.pets_mapper import map_get_user_pets_dto_to_user

logger = logging.getLogger("Poop Manager Handler")


router = APIRouter(
    prefix='/pets',
    tags=['pets']
)

@router.post("/get-pets", 
             response_model=ResponseDTO,
             responses={
                 200: {"description": "Operation successful", "model": ResponseDTO},
                 400: {"description": "Validation Error", "model": ResponseDTO},
                 500: {"description": "Internal Server Error", "model": ResponseDTO},
             }
)
@inject
async def get_user_pets(
    get_user_pets_dto: GetUserPetsInput,
    pets_usecase: PetsUseCase = Depends(Provide[Container.pets_usecase]),
    current_user: str = Depends(get_current_user)
):
    """
    Retrieves the details of a pet.

    Args:
        get_user_pets_dto (GetUserPetsInput): The data transfer object containing the user's details.
        pets_usecase (PetsUseCase): The Pets UseCase.

    Returns:
        ResponseDTO: A response object containing the pet's data.
    """
    logger.info("Init get-pets handler")

    try:
        user = map_get_user_pets_dto_to_user(get_user_pets_dto)
        pets = await pets_usecase.get_user_pets(user.id)
        response_data = pets_mapper.map_pet_list_to_pet_list_output_dto(pets)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, response_data)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)

@router.post("/new-pet", 
             response_model=ResponseDTO,
             responses={
                 200: {"description": "Operation successful", "model": ResponseDTO},
                 400: {"description": "Validation Error", "model": ResponseDTO},
                 500: {"description": "Internal Server Error", "model": ResponseDTO},
             }
)
@inject
async def new_pet(
    new_pet_dto: NewPetInput,
    pets_usecase: PetsUseCase = Depends(Provide[Container.pets_usecase]),
    current_user: str = Depends(get_current_user)
):
    """
    Creates a new pet.

    Args:
        new_pet_dto (NewPetInput): The data transfer object containing the pet's details.
        pets_usecase (PetsUseCase): The Pets UseCase.

    Returns:
        ResponseDTO: A response object containing the pet's data.
    """
    logger.info("Init new-pet handler")

    try:
        pet = pets_mapper.map_pet_dto_to_pet(new_pet_dto)
        pet_created = await pets_usecase.new_pet(pet)
        response_data = pets_mapper.map_pet_to_pet_output_dto(pet)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, response_data)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)