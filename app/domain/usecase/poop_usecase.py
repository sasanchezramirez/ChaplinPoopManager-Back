import logging


from datetime import datetime
from app.domain.model.poop import Poop, PoopList
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.gateway.persistence_gateway import PersistenceGateway

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
            poop_times = self.persistence_gateway.get_poop_times_by_pet_id(poop)
            poop_list = PoopList(poops=poop_times)
            return poop_list
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)

        




            

