from fastapi import Depends, Request

from app.api.controller.auth import oauth2_scheme, AuthController


async def get_user(
        token: str = Depends(oauth2_scheme),
        controller: AuthController = Depends()
):
    return await controller.get_current_user(token)