from app.application.handler import Handlers
from app.domain.usecase.user_usecase import UserUseCase
from app.domain.usecase.auth_usecase import AuthUseCase
from app.domain.usecase.poop_usecase import PoopUseCase
from app.domain.usecase.pets_usecase import PetsUseCase
from app.domain.usecase.clean_usecase import CleanUseCase
from app.infrastructure.driven_adapter.persistence.service.presistence import Persistence
from app.infrastructure.driven_adapter.persistence.config.database import SessionLocal
from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules= Handlers.modules())

    session = providers.Singleton(SessionLocal)

    persistence_gateway = providers.Factory(Persistence, session=session)

    user_usecase = providers.Factory(UserUseCase, persistence_gateway=persistence_gateway)
    auth_usecase = providers.Factory(AuthUseCase, persistence_gateway=persistence_gateway)
    poop_usecase = providers.Factory(PoopUseCase, persistence_gateway=persistence_gateway)
    pets_usecase = providers.Factory(PetsUseCase, persistence_gateway=persistence_gateway)
    clean_usecase = providers.Factory(CleanUseCase, persistence_gateway=persistence_gateway)

