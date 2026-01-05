from dataclasses import dataclass


@dataclass
class RollDiceResultEntity:
    rolled_dice_value: int
    text: str
