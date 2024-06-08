from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from starlette.responses import JSONResponse

from app.db.deps import get_db
from app.schema import DefaultResponse
from app.utils.config import settings

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
def root() -> dict:
    return {
        "msg": "Project information",
        "details": {
            "name": f"{settings.PROJECT_NAME}",
            "version": f"{settings.APP_VERSION}",
        },
    }


@router.get("/health", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
async def get_health(db: AsyncSession = Depends(get_db)) -> JSONResponse:
    # create a dictionary to store the health check details for each service
    # In this skeleton, we only have the database service
    details = {}

    try:
        result = await db.execute(text("SELECT 1"))
        if result.scalar() is None:
            details["database"] = "Not Healthy ❌"
            return JSONResponse(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                content=DefaultResponse(
                    msg="Database is not healthy ❌", details=details
                ).dict(),
            )
        details["database"] = "Healthy ✅"
    except Exception as e:
        details["database"] = str(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=DefaultResponse(
                msg="Database health check failed ❌", details=details
            ).dict(),
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=DefaultResponse(
            msg="All services are healthy ✅", details=details
        ).dict(),
    )
