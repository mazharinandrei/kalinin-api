from pydantic import BaseModel


class CreateUniversalReply(BaseModel):
    text: str


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


class ReadUniversalReply(BaseModel):
    id: int
    text: str
