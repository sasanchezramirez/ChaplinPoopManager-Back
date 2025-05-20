import logging
import app.infrastructure.driven_adapter.persistence.mapper.user_mapper as mapper

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.infrastructure.driven_adapter.persistence.entity.user_entity import User_entity
from app.infrastructure.driven_adapter.persistence.repository.user_repository import UserRepository
from app.domain.model.user import User
from app.domain.model.poop import Poop
from app.domain.model.pets import Pet
from app.domain.model.clean import Clean
from app.infrastructure.driven_adapter.persistence.repository.poop_repository import PoopRepository
from app.infrastructure.driven_adapter.persistence.mapper.poop_mapper import map_poop_to_poop_entity, map_poop_entity_to_poop
from app.domain.gateway.persistence_gateway import PersistenceGateway
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.infrastructure.driven_adapter.persistence.repository.pets_repository import PetsRepository
from app.infrastructure.driven_adapter.persistence.mapper.pets_mapper import map_pet_to_pets_entity, map_pets_entity_to_pet
from app.infrastructure.driven_adapter.persistence.mapper.poop_management_mapper import map_clean_to_poop_management_entity, poop_management_entity_to_clean
from app.infrastructure.driven_adapter.persistence.repository.poop_management_repository import PoopManagementRepository
logger = logging.getLogger("Persistence")

class Persistence(PersistenceGateway):
    def __init__(self, session: Session):
        logger.info("Init persistence service")
        self.session = session
        self.user_repository = UserRepository(session)
        self.poop_repository = PoopRepository(session)
        self.pets_repository = PetsRepository(session)
        self.poop_management_repository = PoopManagementRepository(session)

    def create_user(self, user: User):
        try:
            user_entity = User_entity()
            user_entity.email = user.email
            user_entity.password = user.password
            user_entity.creation_date = user.creation_date
            user_entity.profile_id = user.profile_id
            user_entity.status_id = user.status_id
            created_user_entity = self.user_repository.create_user(user_entity)
            self.session.commit()
            return mapper.map_user_entity_to_user(created_user_entity)
        except IntegrityError as e:
            logger.error(f"Operation failed: {e}")
            if "llave duplicada" or "duplicate key" in str(e.orig):
                raise CustomException(ResponseCodeEnum.KOU01)
            elif "viola la llave" or "key violation" in str(e.orig):
                if "profile_id" in str(e.orig):
                    raise CustomException(ResponseCodeEnum.KOU03)
                elif "status_id" in str(e.orig):
                    raise CustomException(ResponseCodeEnum.KOU04)
            raise CustomException(ResponseCodeEnum.KOG02)
        except SQLAlchemyError as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG02)
        except Exception as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)
        
    def get_user_by_id(self, id: int):
        try:
            user_entity = self.user_repository.get_user_by_id(id)
            return mapper.map_user_entity_to_user(user_entity)
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG02)
        except Exception as e:
            logger.error(f"Operation failed: {e}")  
            raise CustomException(ResponseCodeEnum.KOG01)
        
    def get_user_by_email(self, email: str):
        try:
            user_entity = self.user_repository.get_user_by_email(email)
            return mapper.map_user_entity_to_user(user_entity)
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG02)
        except Exception as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)
    
    def update_user(self, user: User):
        try:
            user_entity = mapper.map_user_update_to_user_entity(user)
            existing_user = self.user_repository.get_user_by_id(user_entity.id)
            if not existing_user:
                raise CustomException(ResponseCodeEnum.KOD02)

            if user_entity.email:
                existing_user.email = user_entity.email
            if user_entity.password:
                existing_user.password = user_entity.password
            if user_entity.profile_id is not None and user_entity.profile_id != 0:
                existing_user.profile_id = user_entity.profile_id
            if user_entity.status_id is not None and user_entity.status_id != 0:
                existing_user.status_id = user_entity.status_id
            user_entity = mapper.map_user_update_to_user_entity(user, existing_user)
            updated_user_entity = self.user_repository.update_user(user_entity)
            self.session.commit()
            return mapper.map_user_entity_to_user(updated_user_entity)
        except IntegrityError as e:
            logger.error(f"Operation failed: {e}")
            if "llave duplicada" in str(e.orig) or "duplicate key" in str(e.orig):
                raise CustomException(ResponseCodeEnum.KOU01)
            elif "viola la llave" in str(e.orig) or "key violation" in str(e.orig):
                if "profile_id" in str(e.orig):
                    raise CustomException(ResponseCodeEnum.KOU03)
                elif "status_id" in str(e.orig):
                    raise CustomException(ResponseCodeEnum.KOU04)
            raise CustomException(ResponseCodeEnum.KOG02)
        except SQLAlchemyError as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG02)
        except Exception as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)
    
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
    
    def get_poop_times_by_pet_id(self, poop: Poop):
        try:
            poop_times_list = []
            poop_entity = map_poop_to_poop_entity(poop)
            poop_times_list_entity = self.poop_repository.get_poop_by_pet_id(poop_entity)
            for poop_times_entity in poop_times_list_entity:
                poop_times_list.append(map_poop_entity_to_poop(poop_times_entity))
            return poop_times_list
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting poop: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def get_pets_by_user_id(self, user_id: int):
        try:
            pets_list = []
            pets_entity = self.pets_repository.get_pets_by_user_id(user_id)
            for pets_entity in pets_entity:
                pets_list.append(map_pets_entity_to_pet(pets_entity))
            return pets_list
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting poop: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def new_pet(self, pet: Pet):
        try:
            pet_entity = map_pet_to_pets_entity(pet)
            created_pet_entity = self.pets_repository.new_pet(pet_entity)
            logger.info(f"Created pet: {created_pet_entity.id}")
            created_pet = map_pets_entity_to_pet(created_pet_entity)
            self.session.commit()
            return created_pet
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error creating pet: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def new_clean(self, clean: Clean):
        try:
            clean_entity = map_clean_to_poop_management_entity(clean)
            created_clean_entity = self.poop_management_repository.new_clean(clean_entity)
            self.session.commit()
            if created_clean_entity:
                return True
            else:
                raise CustomException(ResponseCodeEnum.KOG02)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error creating clean: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def get_clean_by_pet_id(self, pet_id: int):
        try:
            clean_list = []
            clean_list_entity = self.poop_management_repository.get_clean_by_pet_id(pet_id)
            for clean_entity in clean_list_entity:
                clean_list.append(poop_management_entity_to_clean(clean_entity))
            print(clean_list)
            return clean_list
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting clean: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)