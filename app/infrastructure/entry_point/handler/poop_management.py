import app.infrastructure.entry_point.mapper.poop_mapper as poop_mapper
import logging

from fastapi import APIRouter, Depends 
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide
from app.infrastructure.entry_point.dto.clean_dto import NewCleanInput, GetCleanInput
from app.application.container import Container
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.usecase.util.jwt import get_current_user
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.infrastructure.entry_point.dto.response_dto import ResponseDTO
from app.infrastructure.entry_point.utils.api_response import ApiResponse
from app.infrastructure.entry_point.mapper.clean_mapper import map_clean_to_clean_dto, map_clean_list_to_clean_list_output_dto, map_clean_dto_to_clean
from app.domain.usecase.clean_usecase import CleanUseCase

logger = logging.getLogger("Poop Management Handler")

router = APIRouter(
    prefix='/clean',
    tags=['clean']
)

@router.post('/new-clean', 
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def new_clean(
    new_clean_dto: NewCleanInput,
    clean_usecase: CleanUseCase = Depends(Provide[Container.clean_usecase])
):
    """
    Puts a new clean in the system.
    
    Args:
        new_clean_dto (NewCleanInput): The data transfer object containing the clean's details.
        # poop_usecase (PoopUseCase): The Poop UseCase.

    Returns:
        ResponseDTO: A response object containing the operation data.
    """
    
    logger.info("Init new-clean handler")


    new_clean = map_clean_dto_to_clean(new_clean_dto)
    try:
        clean_status = await clean_usecase.new_clean(new_clean)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, clean_status)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)
    


