from dataclasses import dataclass


@dataclass
class RollDiceRangeEntity:
    start: int
    end: int
    text: str
    id: int | None = None
