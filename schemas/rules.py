from typing import List, Optional

from pydantic import BaseModel, Field


class ReadTrigger(BaseModel):
    id: int
    text: str


class ReadReplyOption(BaseModel):
    id: int
    text: str


class ReadRule(BaseModel):
    id: int
    triggers: list[str]
    reply_options: list[str]


class CreateRule(BaseModel):
    triggers: List[str] = Field(min_length=1)
    reply_options: List[str] = Field(min_length=1)


class ExtendRule(BaseModel):
    triggers: Optional[List[str]] = None
    reply_options: Optional[List[str]] = None
