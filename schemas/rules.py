
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
    triggers: list[str] = Field(min_length=1)
    reply_options: list[str] = Field(min_length=1)


class ExtendRule(BaseModel):
    triggers: list[str] | None = None
    reply_options: list[str] | None = None
