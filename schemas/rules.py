
from pydantic import BaseModel, Field


class CreateRule(BaseModel):
    triggers: list[str] = Field(min_length=1)
    reply_options: list[str] = Field(min_length=1)


class ExtendRule(BaseModel):
    triggers: list[str] | None = None
    reply_options: list[str] | None = None
