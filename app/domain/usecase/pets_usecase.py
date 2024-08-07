import logging

from app.domain.model.pets import Pet, PetList
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.gateway.persistence_gateway import PersistenceGateway

logger = logging.getLogger("Pets UseCase")

class PetsUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway
        
    async def get_user_pets(self, pet: Pet):
        logger.info("Init get user pets usecase")
        try:  
            pets = self.persistence_gateway.get_pets_by_user_id(pet)
            return PetList(pets=pets)
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)