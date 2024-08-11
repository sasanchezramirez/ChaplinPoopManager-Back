from sqlalchemy import Column, Integer, DateTime
from app.infrastructure.driven_adapter.persistence.config.database import Base


class PoopManagmentEntity(Base):
    __tablename__ = "poop_managment"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date_of_clean = Column(DateTime)
    pet_id = Column(Integer)
    



