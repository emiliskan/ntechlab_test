import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from services.users import UsersService, get_users_service, UserExists
from schemas.user import User

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", summary="Регистрация нового юзера.", response_model=User)
async def new_user(
        user_data: User,
        user_service: UsersService = Depends(get_users_service)
) -> User:
    try:
        created_user = await user_service.new_user(user_data)
    except UserExists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists.")

    return created_user


@router.put("/location", summary="Сохранение местоположения юзера.", response_model=User)
async def save_user_location(
        user: User,
        user_service: UsersService = Depends(get_users_service),
) -> User:
    return await user_service.save_user_location(user)


@router.get("/location/near", summary="Получение пользователей рядом.", response_model=List[User])
async def get_near_users(
        user_id: int,
        radius: float,
        count: int,
        user_service: UsersService = Depends(get_users_service),
) -> List[User]:
    near_users = await user_service.get_users_near(user_id, radius, count)
    return near_users
