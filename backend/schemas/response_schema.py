from pydantic import BaseModel
from typing import Any


class ChatResponse(BaseModel):

    agent: str

    response: Any

    summary: dict