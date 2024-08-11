import logging

from app.domain.model.pets import Pet, PetList
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.gateway.persistence_gateway import PersistenceGateway

logger = logging.getLogger("Pets UseCase")

class PetsUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway
        
    async def get_user_pets(self, user_id: int):
        logger.info("Init get user pets usecase")
        try:  
            pets = self.persistence_gateway.get_pets_by_user_id(user_id)
            return PetList(pets=pets)
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)
        
    async def new_pet(self, pet: Pet):
        logger.info("Init new pet usecase")
        try:  
            created_pet = self.persistence_gateway.new_pet(pet)
            logger.info(f"Created pet: {pet}")
            return created_pet
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)