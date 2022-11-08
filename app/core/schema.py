from typing import Any

from pydantic import BaseModel


class DefaultResponse(BaseModel):
    status: bool
    msg: str
    details: dict[Any, Any] | None = {}
