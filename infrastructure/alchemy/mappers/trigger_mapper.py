from domain.enities.trigger import TriggerEntity
from infrastructure.alchemy.mappers.abstract_sqlalchemy_mapper import (
    AbstractSQLAlchemyMapper,
)
from infrastructure.alchemy.models.rule import Trigger


class SQLAlchemyTriggerMapper(AbstractSQLAlchemyMapper):
    @staticmethod
    def to_entity(model: Trigger) -> TriggerEntity:

        return TriggerEntity(id=int(model.id), text=str(model.text))
