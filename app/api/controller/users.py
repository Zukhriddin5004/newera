from fastapi import Depends, HTTPException
from typing import List
from app.api.repositories.users import UserRepository

from app.api.models.users import Users
from app.api.schemas.auth import User



class UserController:
    def __init__(self, user_repository: UserRepository = Depends()):
        self.user_repository = user_repository

    async def get_user_by_id(self, user_id: int):
        user = await self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return await self.user_repository.get_user_by_id(user_id)

    async def get_all_users(self):
        return await self.user_repository.get_all_users()


    async def delete_user(self, user_id: int):
        user = await self.user_repository.get_user_by_id(user_id)
        return await self.user_repository.delete_user(user)