import logging

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.infrastructure.driven_adapter.persistence.entity.user_entity import User_entity
from app.infrastructure.driven_adapter.persistence.repository.user_repository import UserRepository
from app.domain.model.user import User
from app.domain.model.poop import Poop
from app.infrastructure.driven_adapter.persistence.repository.poop_repository import PoopRepository
from app.infrastructure.driven_adapter.persistence.mapper.poop_mapper import map_poop_to_poop_entity
from app.domain.gateway.persistence_gateway import PersistenceGateway
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
import app.infrastructure.driven_adapter.persistence.mapper.user_mapper as mapper

logger = logging.getLogger("Persistence")

class Persistence(PersistenceGateway):
    def __init__(self, session: Session):
        logger.info("Init persistence service")
        self.session = session
        self.user_repository = UserRepository(session)
        self.poop_repository = PoopRepository(session)

    def create_user(self, user: User):
        try:
            user_entity = User_entity(user)
            created_user_entity = self.user_repository.create_user(user_entity)
            self.session.commit()
            return mapper.map_user_entity_to_user(created_user_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error creating user: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def get_user_by_id(self, id: int):
        try:
            user_entity = self.user_repository.get_user_by_id(id)
            return mapper.map_user_entity_to_user(user_entity)
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting user: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def get_user_by_email(self, email: str):
        try:
            user_entity = self.user_repository.get_user_by_email(email)
            return mapper.map_user_entity_to_user(user_entity)
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting user: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
    
    def update_user(self, user: User):
        try:
            existing_user = self.user_repository.get_user_by_id(user.id)
            if not existing_user:
                raise CustomException(ResponseCodeEnum.KOU02)
            user_entity = mapper.map_user_update_to_user_entity(user, existing_user)
            updated_user_entity = self.user_repository.update_user(user_entity)
            self.session.commit()
            return mapper.map_user_entity_to_user(updated_user_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error updating user: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
    
    def new_poop(self, poop: Poop):
        try:
            poop_entity = map_poop_to_poop_entity(poop)
            created_poop_entity = self.poop_repository.new_poop(poop_entity)
            self.session.commit()
            if created_poop_entity:
                return True
            else:
                raise CustomException(ResponseCodeEnum.KOG02)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error creating poop: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
