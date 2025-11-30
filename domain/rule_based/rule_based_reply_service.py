from dataclasses import dataclass
from random import choice

from domain.abstract_repository import Repository
from domain.abstract_uow import UnitOfWork
from domain.enities.rule import RuleEntity
from domain.reply_service import ReplyService
from domain.rule_based.abstract_rule_repository import RuleRepository


@dataclass
class RuleBasedReplyService(ReplyService):
    trigger_repository: Repository
    rule_repository: RuleRepository
    universal_reply_repository: Repository
    uow: UnitOfWork

    async def get_reply(self, input_message: str):
        async with self.uow.begin() as session:
            rules: list[RuleEntity] = await self.rule_repository.find_by_triggers(
                session=session,
                triggers=input_message.split(),
            )

            all_options = [
                option for rule in rules or [] for option in (rule.reply_options or [])
            ]

            if not all_options:
                all_options = await self.universal_reply_repository.list(
                    session=session
                )

            return choice(all_options)
