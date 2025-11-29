from domain.enities.reply_option import ReplyOptionEntity
from infrastructure.alchemy.mappers.abstract_sqlalchemy_mapper import (
    AbstractSQLAlchemyMapper,
)
from infrastructure.alchemy.models.rule import ReplyOption


class SQLAlchemyReplyOptionMapper(AbstractSQLAlchemyMapper):
    @staticmethod
    def to_entity(model: ReplyOption) -> ReplyOptionEntity:
        return ReplyOptionEntity(id=int(model.id), text=str(model.text))
