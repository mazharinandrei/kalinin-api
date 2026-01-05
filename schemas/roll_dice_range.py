from pydantic import BaseModel, Field

from api.v1.api_spec import RollDiceSpec


class CreateRollDiceRange(BaseModel):
    start: int
    end: int
    text: str = Field(examples=[RollDiceSpec.TEXT_EXAMPLE])
