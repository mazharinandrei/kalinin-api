from dataclasses import dataclass
from random import randint, choice

from domain.crud_service import CRUDService
from domain.enities.roll_dice_result import RollDiceResultEntity


@dataclass
class RollDiceService(CRUDService):
    async def roll(self) -> RollDiceResultEntity:
        async with self.uow.begin() as session:
            rolled_dice_value = randint(1, 20)
            result = await self.repository.get_roll_interpretation(
                session=session, value=rolled_dice_value
            )
            result = choice(result)
            return RollDiceResultEntity(
                rolled_dice_value=rolled_dice_value, text=result.text
            )
