from abc import ABC, abstractmethod
from app.domain.model.user import User
from app.domain.model.poop import Poop

class PersistenceGateway(ABC):

    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def get_user_by_id(self, id: int):
        pass

    @abstractmethod
    def get_user_by_email(self, id: int):
        pass

    @abstractmethod
    def update_user(self, user: User):
        pass

    @abstractmethod
    def new_poop(self, poop: Poop):
        pass

    def get_poop_times_by_pet_id(self, poop: Poop):
        pass
