from domain.enities.reply_option import ReplyOptionEntity
from infrastructure.abstract.abstract_sqlalchemy_mapper import AbstractSQLAlchemyMapper
from infrastructure.alchemy.models.rule import ReplyOption


class SQLAlchemyReplyOptionMapper(AbstractSQLAlchemyMapper):
    @staticmethod
    def to_entity(model: ReplyOption) -> ReplyOptionEntity:
        return ReplyOptionEntity(int(model.id), str(model.text))

    @staticmethod
    def to_orm(entity: ReplyOptionEntity) -> ReplyOption:
        reply_option = ReplyOption()
        reply_option.id = entity.id
        reply_option.text = entity.text
        return reply_option
