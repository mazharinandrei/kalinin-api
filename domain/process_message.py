from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import choice

from domain.enities.rule import RuleEntity
from infrastructure.abstract.abstract_repository import Repository
from infrastructure.abstract.abstract_rule_repository import RuleRepository


class ReplyService(ABC):
    @abstractmethod
    async def get_reply(self, input_message: str):
        raise NotImplementedError


@dataclass
class RuleBasedReplyService(ReplyService):
    trigger_repository: Repository
    rule_repository: RuleRepository
    universal_reply_repository: Repository

    async def get_reply(self, input_message: str):

        rules: list[RuleEntity] = await self.rule_repository.find_by_triggers(input_message.split())

        all_options = [
            option
            for rule in rules or []
            for option in (rule.reply_options or [])
        ]

        if not all_options:
            all_options = await self.universal_reply_repository.list()

        return choice(all_options)
