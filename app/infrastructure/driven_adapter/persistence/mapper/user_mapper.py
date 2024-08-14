from app.infrastructure.driven_adapter.persistence.entity.user_entity import User_entity
from app.domain.model.user import User


def map_user_entity_to_user(user_entity: User_entity) -> User:
    return User(
        id=user_entity.id,
        email=user_entity.email,
        password=user_entity.password,
        creation_date=str(user_entity.creation_date),
        profile_id=user_entity.profile_id,
        status_id=user_entity.status_id
    )

def map_user_to_user_entity(user: User) -> User_entity: 
    return User_entity(
        id=user.id,
        email=user.email,
        password=user.password,
        creation_date=user.creation_date,
        profile_id=user.profile_id,
        status_id=user.status_id
    )

def map_user_update_to_user_entity(user_update: User, user_entity: User_entity) -> User_entity:
    return User_entity(
        id=user_update.id if user_update.id is not None else user_entity.id,
        email=user_update.email if user_update.email is not None else user_entity.email,
        password=user_update.password if user_update.password is not None else user_entity.password,
        creation_date=user_update.creation_date if user_update.creation_date is not None else user_entity.creation_date,
        profile_id=user_update.profile_id if user_update.profile_id is not None and user_update.profile_id != 0 else user_entity.profile_id,
        status_id=user_update.status_id if user_update.status_id is not None and user_update.status_id != 0 else user_entity.status_id
    )

