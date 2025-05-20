from sqlalchemy import Column, Integer, String, Date
from app.infrastructure.driven_adapter.persistence.config.database import Base

class PetsEntity(Base):
    __tablename__ = "pets"
    __table_args__ = {'schema': 'poop_manager'}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pet_name = Column(String)
    user_id = Column(Integer)
    birthday = Column(Date)
    profile_image = Column(String)