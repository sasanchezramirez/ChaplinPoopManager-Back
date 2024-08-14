import logging
import app.infrastructure.driven_adapter.persistence.mapper.user_mapper as mapper
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.infrastructure.driven_adapter.persistence.entity.user_entity import User_entity
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.util.custom_exceptions import CustomException

logger = logging.getLogger("User Repository")

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user_entity: User_entity):
        self.session.add(user_entity)
        self.session.commit()
        return user_entity

        
    def get_user_by_id(self, id: int):
        user_entity = self.session.query(User_entity).filter_by(id=id).first()
        return user_entity

        
    def get_user_by_email(self, email: str):
        user_entity = self.session.query(User_entity).filter_by(email=email).first()
        return user_entity 

        
    def update_user(self, user_entity: User_entity):
        existing_user = self.session.query(User_entity).filter_by(id=user_entity.id).first()
        self.session.commit()
        return existing_user

