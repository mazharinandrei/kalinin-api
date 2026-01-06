from typing import Literal

from domain.enities.brick_translate_result import BrickTranslateResult, consonants


class BrickTranslateService:
    cyrillic_vowels = "уеёыаоэяию"
    latin_vowels = "aeiouy"
    vowels = cyrillic_vowels + latin_vowels

    async def translate(
        self, dialect: Literal[*consonants], text: str
    ) -> BrickTranslateResult:
        result = []
        for symbol in text:
            if symbol.lower() in self.vowels:
                result.extend((symbol, dialect, symbol.lower()))
            else:
                result.append(symbol)
        return BrickTranslateResult(dialect=dialect, result_text="".join(result))
