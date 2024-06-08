from typing import Any

from pydantic import BaseModel


class DefaultResponse(BaseModel):
    msg: str
    details: dict[Any, Any] | None = {}
