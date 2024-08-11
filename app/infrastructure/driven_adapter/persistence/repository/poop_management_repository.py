import logging
import app.infrastructure.driven_adapter.persistence.mapper.user_mapper as mapper
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.infrastructure.driven_adapter.persistence.entity.poop_management_entity import PoopManagementEntity
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.util.custom_exceptions import CustomException

logger = logging.getLogger("PoopManagment Repository")

class PoopManagementRepository:
    def __init__(self, session: Session):
        self.session = session

    def new_clean(self, poop_management_entity: PoopManagementEntity):
        self.session.add(poop_management_entity)
        self.session.commit()
        return poop_management_entity

        
    def get_clean_by_pet_id(self, poop_management_entity: PoopManagementEntity):
        return self.session.query(PoopManagementEntity).filter(PoopManagementEntity.pet_id == poop_management_entity.pet_id).all()

        

