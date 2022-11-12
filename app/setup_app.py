import sentry_sdk
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routes import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.APP_VERSION,
        docs_url=None if settings.is_prod() else "/docs",
        redoc_url=None if settings.is_prod() else "/redoc",
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )
    setup_routers(app)
    setup_middlewares(app)
    return app


def setup_sentry():
    if settings.SENTRY_ENABLED:
        sentry_sdk.init(
            dsn=settings.SENTRY_DSN,
            environment=settings.SENTRY_ENV,
            traces_sample_rate=1.0,
        )


def setup_routers(app: FastAPI) -> None:
    app.include_router(api_router, prefix=settings.API_V1_STR)


def setup_middlewares(app) -> None:
    # CORS
    origins = []

    # Set all CORS enabled origins : adding security between Backend and Frontend
    if settings.BACKEND_CORS_ORIGINS:
        origins_raw = settings.BACKEND_CORS_ORIGINS.split(",")

        for origin in origins_raw:
            use_origin = origin.strip()
            origins.append(use_origin)

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
