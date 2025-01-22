from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.api.controller.users import UserController
from app.api.schemas.auth import User
from app.api.dependecies.dependecies import get_user
from app.api.models import Users

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.get("/", response_model=List[User])
async def get_users(
        current_user: Users = Depends(get_user),
        controller: UserController = Depends(),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return await controller.get_all_users()

@router.get("/{id}", response_model=User)
async def get_user(
        user_id: int,
        current_user: Users = Depends(get_user),
        controller: UserController = Depends(),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return await controller.get_user_by_id(user_id)


@router.delete("/{id}")
async def delete_user(
        user_id: int,
        current_user: Users = Depends(get_user),
        controller: UserController = Depends(),
):
    if current_user.is_superuser and current_user.id != user_id:
        return await controller.delete_user(user_id)
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)