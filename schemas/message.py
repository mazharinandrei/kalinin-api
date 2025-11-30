from pydantic import BaseModel, Field

from api.v1.api_spec import ProcessMessageSpec


class Message(BaseModel):
    text: str = Field(examples=[ProcessMessageSpec.INPUT_MESSAGE_EXAMPLE])
