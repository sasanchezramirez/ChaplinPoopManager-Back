import logging


from datetime import datetime
from app.domain.model.poop import Poop
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.gateway.persistence_gateway import PersistenceGateway
from app.domain.usecase.util.security import  hash_password

logger = logging.getLogger("Poop UseCase")


class PoopUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway
        

    async def new_poop(self, poop: Poop):
        logger.info("Init new poop usecase")
        poop.date = datetime.now().isoformat()
        try:  
            return self.persistence_gateway.new_poop(poop)
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)
        
    async def get_poop(self, poop: Poop):
        logger.info("Init get poop usecase")
        try:  
            return self.persistence_gateway.get_poop(poop)
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)

        




            

