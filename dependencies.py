from domain.crud_service import CRUDService
from domain.roll_dice.roll_dice_service import RollDiceService
from domain.rule_based_replies.rule_based_reply_service import (
    ReplyService,
    RuleBasedReplyService,
)
from domain.rule_based_replies.rule_service import RuleService
from infrastructure.alchemy.mappers.reply_option_mapper import (
    SQLAlchemyReplyOptionMapper,
)
from infrastructure.alchemy.mappers.roll_dice_range_mapper import (
    SQLAlchemyRollDiceRangeMapper,
)
from infrastructure.alchemy.mappers.rule_mapper import SQLAlchemyRuleMapper
from infrastructure.alchemy.mappers.trigger_mapper import SQLAlchemyTriggerMapper
from infrastructure.alchemy.mappers.universal_reply_mapper import (
    SQLAlchemyUniversalReplyMapper,
)
from infrastructure.alchemy.models.roll_dice_range import RollDiceRange
from infrastructure.alchemy.models.rule import ReplyOption, Rule, Trigger
from infrastructure.alchemy.models.universal_reply import UniversalReply
from infrastructure.alchemy.repositories.crud_repository import SQLAlchemyCRUDRepository
from infrastructure.alchemy.repositories.roll_dice_repository import (
    SQLAlchemyRollDiceRepository,
)
from infrastructure.alchemy.repositories.rule_repository import SQLAlchemyRuleRepository
from infrastructure.alchemy.uow import AlchemyUnitOfWork


def universal_replies_service() -> CRUDService:
    return CRUDService(
        repository=SQLAlchemyCRUDRepository(
            model=UniversalReply,
            mapper=SQLAlchemyUniversalReplyMapper,
        ),
        uow=AlchemyUnitOfWork(),
    )


def rules_service() -> RuleService:
    return RuleService(
        repository=SQLAlchemyRuleRepository(
            model=Rule,
            mapper=SQLAlchemyRuleMapper,
        ),
        trigger_repository=SQLAlchemyCRUDRepository(
            model=Trigger,
            mapper=SQLAlchemyTriggerMapper,
        ),
        reply_option_repository=SQLAlchemyCRUDRepository(
            model=ReplyOption,
            mapper=SQLAlchemyReplyOptionMapper,
        ),
        uow=AlchemyUnitOfWork(),
    )


def reply_service() -> ReplyService:
    return RuleBasedReplyService(
        trigger_repository=SQLAlchemyCRUDRepository(
            model=Trigger,
            mapper=SQLAlchemyTriggerMapper,
        ),
        rule_repository=SQLAlchemyRuleRepository(
            model=Rule,
            mapper=SQLAlchemyRuleMapper,
        ),
        universal_reply_repository=SQLAlchemyCRUDRepository(
            model=UniversalReply,
            mapper=SQLAlchemyUniversalReplyMapper,
        ),
        uow=AlchemyUnitOfWork(),
    )


def roll_dice_service() -> RollDiceService:
    return RollDiceService(
        repository=SQLAlchemyRollDiceRepository(
            model=RollDiceRange, mapper=SQLAlchemyRollDiceRangeMapper
        ),
        uow=AlchemyUnitOfWork(),
    )
