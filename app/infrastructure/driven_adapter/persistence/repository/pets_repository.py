from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.infrastructure.driven_adapter.persistence.entity.pets_entity import PetsEntity
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.util.custom_exceptions import CustomException


class PetsRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_pets_by_user_id(self, user_id: int):
       return self.session.query(PetsEntity).filter(PetsEntity.user_id == user_id).all()
       