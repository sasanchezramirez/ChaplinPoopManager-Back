import logging


from datetime import datetime
from app.domain.model.clean import Clean, CleanList
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.gateway.persistence_gateway import PersistenceGateway

logger = logging.getLogger("Clean UseCase")


class CleanUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway
        

    async def new_clean(self, clean: Clean):
        logger.info("Init new clean usecase")
        clean.date_of_clean = datetime.now().isoformat()
        try:  
            return self.persistence_gateway.new_clean(clean)
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)
        
    async def get_clean(self, clean: Clean):
        logger.info("Init get clean usecase")
        try:  
            clean_times = self.persistence_gateway.get_clean_by_pet_id(clean)
            clean_list = CleanList(cleans=clean_times)
            return clean_list
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)

        




            

