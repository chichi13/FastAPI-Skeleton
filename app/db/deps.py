from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import async_session


async def get_db() -> AsyncIterator[AsyncSession]:
    async with async_session() as db:
        yield db
