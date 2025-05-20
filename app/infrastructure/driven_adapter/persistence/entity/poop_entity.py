from sqlalchemy import Column, Integer, String
from app.infrastructure.driven_adapter.persistence.config.database import Base


class PoopEntity(Base):
    __tablename__ = "poop_times"
    __table_args__ = {'schema': 'poop_manager'}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(String)
    pet_id = Column(Integer)
    



