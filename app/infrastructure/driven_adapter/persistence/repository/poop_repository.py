import logging
import app.infrastructure.driven_adapter.persistence.mapper.user_mapper as mapper
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.infrastructure.driven_adapter.persistence.entity.poop_entity import PoopEntity
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.util.custom_exceptions import CustomException

logger = logging.getLogger("Poop Repository")

class PoopRepository:
    def __init__(self, session: Session):
        self.session = session

    def new_poop(self, poop_entity: PoopEntity):
        logger.info(f"Creating user: {poop_entity}")
        try:
            self.session.add(poop_entity)
            self.session.commit()
            return poop_entity
        except SQLAlchemyError as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG02)
        except Exception as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)
        

