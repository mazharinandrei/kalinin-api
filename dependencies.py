from domain.crud import CRUDService
from domain.process_message import ReplyService, RuleBasedReplyService
from domain.rules import RuleService
from infrastructure.alchemy.db import async_session_maker
from infrastructure.alchemy.mappers.reply_option_mapper import (
    SQLAlchemyReplyOptionMapper,
)
from infrastructure.alchemy.mappers.rule_mapper import SQLAlchemyRuleMapper
from infrastructure.alchemy.mappers.trigger_mapper import SQLAlchemyTriggerMapper
from infrastructure.alchemy.mappers.universal_reply_mapper import (
    SQLAlchemyUniversalReplyMapper,
)
from infrastructure.alchemy.models.rule import Rule, Trigger, ReplyOption
from infrastructure.alchemy.models.universal_reply import UniversalReply
from infrastructure.alchemy.repository import SQLAlchemyRepository


def universal_replies_service() -> CRUDService:
    return CRUDService(
        repository=SQLAlchemyRepository(
            model=UniversalReply,
            session=async_session_maker(),
            mapper=SQLAlchemyUniversalReplyMapper,
        )
    )


def rules_service() -> RuleService:
    session = async_session_maker()
    return RuleService(
        repository=SQLAlchemyRepository(
            model=Rule, session=session, mapper=SQLAlchemyRuleMapper
        ),
        trigger_repository=SQLAlchemyRepository(
            model=Trigger, session=session, mapper=SQLAlchemyTriggerMapper
        ),
        reply_option_repository=SQLAlchemyRepository(
            model=ReplyOption, session=session, mapper=SQLAlchemyReplyOptionMapper
        ),
    )


def reply_service() -> ReplyService:
    return RuleBasedReplyService()
