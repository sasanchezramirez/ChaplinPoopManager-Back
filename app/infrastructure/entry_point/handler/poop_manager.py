import app.infrastructure.entry_point.mapper.poop_mapper as poop_mapper
import logging

from fastapi import APIRouter, Depends 
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide
from app.infrastructure.entry_point.dto.poop_dto import NewPoopInput, GetPoopInput
from app.domain.usecase.poop_usecase import PoopUseCase

from app.application.container import Container
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.usecase.util.jwt import get_current_user
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.infrastructure.entry_point.dto.response_dto import ResponseDTO
from app.infrastructure.entry_point.utils.api_response import ApiResponse

logger = logging.getLogger("Poop Manager Handler")

router = APIRouter(
    prefix='/poop',
    tags=['poop']
)

@router.post('/new-poop', 
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def new_poop(
    new_poop_dto: NewPoopInput,
    poop_usecase: PoopUseCase = Depends(Provide[Container.poop_usecase])
):
    """
    Puts a new poop in the system.
    
    Args:
        new_poop_dto (NewPoopInput): The data transfer object containing the poop's details.
        poop_usecase (PoopUseCase): The Poop UseCase.

    Returns:
        ResponseDTO: A response object containing the operation data.
    """
    
    logger.info("Init new-poop handler")


    new_poop = poop_mapper.map_poop_dto_to_poop(new_poop_dto)

    try:
        poop_status = await poop_usecase.new_poop(new_poop)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, poop_status)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)
    
@router.post('/get-poop', 
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        404: {"description": "Poop Not Found", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def get_poop(
    get_poop_dto: GetPoopInput,
    poop_usecase: PoopUseCase = Depends(Provide(Container.poop_usecase)),
    current_user: str = Depends(get_current_user)
):
    """
    Retrieves the details of a poop.    
    
    Args:
        get_poop_dto (GetPoopInput): The data transfer object containing the necessary poop details.
        poop_usecase (PoopUseCase): The Poop UseCase.
    
    Returns:
        ResponseDTO: A response object containing the poop's data.
    """
    logger.info("Init get-poop handler")

    get_poop = poop_mapper.map_get_poop_dto_to_poop(get_poop_dto)

    try:
        poop_times = await poop_usecase.get_poop(get_poop)
        logger.info(f"Poop times: {poop_times}")
        response_data = poop_mapper.map_poop_list_to_poop_list_output_dto(poop_times)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, response_data)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)


    


