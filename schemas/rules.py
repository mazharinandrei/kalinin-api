from pydantic import BaseModel


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
    triggers: list[str]
    reply_options: list[str]
