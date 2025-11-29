from pydantic import BaseModel


class CreateUniversalReply(BaseModel):
    text: str
