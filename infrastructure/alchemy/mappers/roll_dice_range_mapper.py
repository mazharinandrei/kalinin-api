from domain.enities.roll_dice_range import RollDiceRangeEntity
from infrastructure.alchemy.mappers.abstract_sqlalchemy_mapper import (
    AbstractSQLAlchemyMapper,
)
from infrastructure.alchemy.models.roll_dice_range import RollDiceRange


class SQLAlchemyRollDiceRangeMapper(AbstractSQLAlchemyMapper):
    @staticmethod
    def to_entity(model: RollDiceRange) -> RollDiceRangeEntity:
        return RollDiceRangeEntity(
            id=int(model.id),
            start=int(model.start),
            end=int(model.end),
            text=str(model.text),
        )
