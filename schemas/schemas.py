from pydantic import BaseModel


class CreateUniversalReply(BaseModel):
    text: str


class ReadUniversalReply(BaseModel):
    id: int
    text: str
