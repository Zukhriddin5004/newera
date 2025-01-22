from typing import Optional, List
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.users import Users
from app.core.database.config import get_general_session


class UserRepository:
    def __init__(self, session: AsyncSession = Depends(get_general_session)):
        self.session = session

    async def get_user_by_id(self, user_id: int) -> Optional[Users]:
        return await self.session.get(Users, user_id)

    async def get_all_users(self) -> List[Users]:
        result = await self.session.execute(select(Users))
        return result.scalars().all()

    async def delete_user(self, user: Users):
        await self.session.delete(user)
        await self.session.commit()
        return {"message": "User deleted successfully"}