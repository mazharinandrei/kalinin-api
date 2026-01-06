from typing import Literal

from pydantic import BaseModel

from domain.enities.brick_translate_result import consonants


class BrickTranslateInput(BaseModel):
    dialect: Literal[*consonants]
    input_text: str


class BrickTranslateResult(BaseModel):
    dialect: Literal[*consonants]
    result_text: str
