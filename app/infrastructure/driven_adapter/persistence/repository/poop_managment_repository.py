import logging
import app.infrastructure.driven_adapter.persistence.mapper.user_mapper as mapper
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.infrastructure.driven_adapter.persistence.entity.poop_managment_entity import PoopManagmentEntity
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.util.custom_exceptions import CustomException

logger = logging.getLogger("PoopManagment Repository")

class PoopManagmentRepository:
    def __init__(self, session: Session):
        self.session = session

    def new_clean(self, poop_managment_entity: PoopManagmentEntity):
        self.session.add(poop_managment_entity)
        self.session.commit()
        return poop_managment_entity

        
    def get_clean_by_pet_id(self, poop_managment_entity: PoopManagmentEntity):
        return self.session.query(PoopManagmentEntity).filter(PoopManagmentEntity.pet_id == poop_managment_entity.pet_id).all()

        

