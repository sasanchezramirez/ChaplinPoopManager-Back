import logging

from fastapi import APIRouter, Depends 
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide


logger = logging.getLogger("Poop Manager Handler")


router = APIRouter(
    prefix='/pets',
    tags=['pets']
)