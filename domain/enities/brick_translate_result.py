from dataclasses import dataclass
from typing import Literal

latin_consonants = "bcdfghjklmnpqrstvwxyz"
cyrillic_consonants = "бвгджзйклмнпрстфхцчшщ"
consonants = cyrillic_consonants + latin_consonants


@dataclass
class BrickTranslateResult:
    dialect: Literal[*consonants]
    result_text: str
