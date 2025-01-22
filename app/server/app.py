from fastapi import FastAPI

from app.core.settings import get_settings

from app.api.views.products import router as products_router
from app.api.views.auth import router as auth_router
from app.api.views.orders import router as orders_router
from app.api.views.users import router as users_router

settings = get_settings()


def create_app() -> FastAPI:
    app_ = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
    )
    app_.include_router(products_router)
    app_.include_router(auth_router)
    app_.include_router(orders_router)
    app_.include_router(users_router)
    return app_
