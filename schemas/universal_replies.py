from pydantic import BaseModel, Field

from api.v1.api_spec import UniversalReplySpec


class CreateUniversalReply(BaseModel):
    text: str = Field(examples=[UniversalReplySpec.TEXT_EXAMPLE])
