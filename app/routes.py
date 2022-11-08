from enum import Enum

from fastapi import APIRouter

from app.modules.system.routes import router as system_router

api_router = APIRouter()


# def _include_secured_router(router: APIRouter, tags: list[str | Enum]):
#     return api_router.include_router(
#         router, tags=tags, dependencies=[Depends(get_current_active_user)]
#     )


def _include_unsecured_router(router: APIRouter, tags: list[str | Enum]):
    return api_router.include_router(router, tags=tags)


_include_unsecured_router(system_router, tags=["System"])
