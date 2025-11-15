from domain.enities.rule import RuleEntity
from infrastructure.abstract.abstract_sqlalchemy_mapper import AbstractSQLAlchemyMapper
from infrastructure.alchemy.mappers.reply_option_mapper import (
    SQLAlchemyReplyOptionMapper,
)
from infrastructure.alchemy.mappers.trigger_mapper import SQLAlchemyTriggerMapper
from infrastructure.alchemy.models.rule import Rule


class SQLAlchemyRuleMapper(AbstractSQLAlchemyMapper):
    @staticmethod
    async def to_entity(model: Rule) -> RuleEntity:
        trigger_mapper = SQLAlchemyTriggerMapper()
        reply_option_mapper = SQLAlchemyReplyOptionMapper()

        try:
            triggers = [
                await trigger_mapper.to_entity(trigger) for trigger in model.triggers
            ]
        except Exception:
            triggers = []

        try:
            reply_options = [
                await reply_option_mapper.to_entity(reply_option)
                for reply_option in model.reply_options
            ]
        except Exception:
            reply_options = []

        return RuleEntity(id=model.id, triggers=triggers, reply_options=reply_options)

    @staticmethod
    async def to_orm(entity: RuleEntity) -> Rule:
        rule = Rule()

        trigger_mapper = SQLAlchemyTriggerMapper()
        reply_option_mapper = SQLAlchemyReplyOptionMapper()

        triggers = [await trigger_mapper.to_orm(trigger) for trigger in entity.triggers]

        reply_options = [
            await reply_option_mapper.to_orm(reply_option)
            for reply_option in entity.reply_options
        ]

        rule.triggers = triggers
        rule.reply_options = reply_options

        return rule
