from domain.enities.universal_reply import UniversalReplyEntity
from infrastructure.abstract.abstract_sqlalchemy_mapper import AbstractSQLAlchemyMapper
from infrastructure.alchemy.models.universal_reply import UniversalReply


class SQLAlchemyUniversalReplyMapper(AbstractSQLAlchemyMapper):
    @staticmethod
    async def to_entity(model: UniversalReply) -> UniversalReplyEntity:
        return UniversalReplyEntity(id=int(model.id), text=str(model.text))

    @staticmethod
    async def to_orm(entity: UniversalReplyEntity) -> UniversalReply:
        universal_reply = UniversalReply()
        universal_reply.id = entity.id
        universal_reply.text = entity.text
        return universal_reply
