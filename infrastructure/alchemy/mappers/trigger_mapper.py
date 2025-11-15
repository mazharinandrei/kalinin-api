from domain.enities.trigger import TriggerEntity
from infrastructure.abstract.abstract_sqlalchemy_mapper import AbstractSQLAlchemyMapper
from infrastructure.alchemy.models.rule import Trigger


class SQLAlchemyTriggerMapper(AbstractSQLAlchemyMapper):
    @staticmethod
    async def to_entity(model: Trigger) -> TriggerEntity:
        return TriggerEntity(int(model.id), str(model.text))

    @staticmethod
    async def to_orm(entity: TriggerEntity) -> Trigger:
        model = Trigger()
        model.id = entity.id
        model.text = entity.text
        return model
