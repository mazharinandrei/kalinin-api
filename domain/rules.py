from dataclasses import dataclass

from domain.crud import CRUDService
from domain.enities.reply_option import ReplyOptionEntity
from domain.enities.rule import RuleEntity
from domain.enities.trigger import TriggerEntity
from infrastructure.abstract.abstract_repository import Repository


@dataclass
class RuleService(CRUDService):
    trigger_repository: Repository
    reply_option_repository: Repository

    async def create(self, data: dict):

        trigger_entities = [TriggerEntity(text=text) for text in data["triggers"]]

        reply_option_entities = [
            ReplyOptionEntity(text=text) for text in data["reply_options"]
        ]

        rule_entity = RuleEntity(
            triggers=trigger_entities, reply_options=reply_option_entities
        )

        await self.repository.save(rule_entity)

    async def update(self, pk, **data):

        raise NotImplementedError("рано ещё!")
