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
            triggers=trigger_entities, reply_options=reply_option_entities,
        )

        saved_entity = await self.repository.save(rule_entity)
        return saved_entity

    async def update(self, pk, **data):
        trigger_entities = [TriggerEntity(text=text) for text in data["triggers"]]

        reply_option_entities = [
            ReplyOptionEntity(text=text) for text in data["reply_options"]
        ]

        rule_entity = RuleEntity(
            id=pk, triggers=trigger_entities, reply_options=reply_option_entities,
        )

        saved_entity = await self.repository.save(rule_entity)

        return saved_entity

    async def extend(self, pk, **data):
        rule_entity = await self.repository.get(id=pk)

        if data["triggers"]:
            trigger_entities = [TriggerEntity(text=text) for text in data["triggers"]]
            rule_entity.triggers += trigger_entities

        if data["reply_options"]:
            reply_option_entities = [
                ReplyOptionEntity(text=text) for text in data["reply_options"]
            ]
            rule_entity.reply_options += reply_option_entities

        saved_entity = await self.repository.save(rule_entity)

        return saved_entity
