from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.schema import DefaultResponse
from app.db.deps import get_db

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
def root() -> dict:
    return {
        "status": True,
        "msg": "Project information",
        "details": {
            "name": f"{settings.PROJECT_NAME}",
            "version": f"{settings.APP_VERSION}",
        },
    }


@router.get("/health", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
async def get_health(db: AsyncSession = Depends(get_db)) -> dict:
    try:
        healthy = await db.execute("SELECT 1")
        if healthy.scalars().first() is None:
            raise HTTPException(status_code=404, detail={"msg": "Not Healthy ❌"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"status": True, "msg": "Healthy ✅"}
