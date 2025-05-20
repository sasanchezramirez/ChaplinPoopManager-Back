from app.domain.model.user import User
from app.infrastructure.driven_adapter.persistence.entity.user_entity import UserEntity

def map_user_entity_to_user(UserEntity: UserEntity) -> User:
    return User(
        id=UserEntity.id,
        email=UserEntity.email,
        password=UserEntity.password,
        creation_date=str(UserEntity.creation_date),
        profile_id=UserEntity.profile_id,
        status_id=UserEntity.status_id
    )

def map_user_to_user_entity(user: User) -> UserEntity: 
    user_entity = UserEntity()
    user_entity.id = user.id
    user_entity.email = user.email
    user_entity.password = user.password
    user_entity.creation_date = user.creation_date
    user_entity.profile_id = user.profile_id
    user_entity.status_id = user.status_id
    return user_entity

def map_user_update_to_user_entity(user_update: User, existing_entity: UserEntity = None) -> UserEntity:
    if existing_entity is None:
        user_entity = UserEntity()
    else:
        user_entity = existing_entity
        
    if user_update.id is not None:
        user_entity.id = user_update.id
    if user_update.email is not None:
        user_entity.email = user_update.email
    if user_update.password is not None:
        user_entity.password = user_update.password
    if user_update.creation_date is not None:
        user_entity.creation_date = user_update.creation_date
    if user_update.profile_id is not None and user_update.profile_id != 0:
        user_entity.profile_id = user_update.profile_id
    if user_update.status_id is not None and user_update.status_id != 0:
        user_entity.status_id = user_update.status_id
        
    return user_entity

