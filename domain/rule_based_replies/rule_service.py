from dataclasses import dataclass

from domain.abstract_repository import Repository
from domain.abstract_uow import UnitOfWork
from domain.crud_service import CRUDService
from domain.enities.reply_option import ReplyOptionEntity
from domain.enities.rule import RuleEntity
from domain.enities.trigger import TriggerEntity


@dataclass
class RuleService(CRUDService):
    trigger_repository: Repository
    reply_option_repository: Repository
    uow: UnitOfWork

    async def create(self, data: dict):
        async with self.uow.begin() as session:
            trigger_entities = [
                TriggerEntity(text=text) for text in data.get("triggers", [])
            ]

            reply_option_entities = [
                ReplyOptionEntity(text=text) for text in data.get("reply_options", [])
            ]

            rule_entity = RuleEntity(
                triggers=trigger_entities,
                reply_options=reply_option_entities,
            )

            saved_entity = await self.repository.save(
                entity=rule_entity, session=session
            )
            return saved_entity

    async def update(self, pk, **data):
        async with self.uow.begin() as session:
            trigger_entities = [
                TriggerEntity(text=text) for text in data.get("triggers", [])
            ]

            reply_option_entities = [
                ReplyOptionEntity(text=text) for text in data.get("reply_options", [])
            ]

            rule_entity = RuleEntity(
                id=pk,
                triggers=trigger_entities,
                reply_options=reply_option_entities,
            )

            saved_entity = await self.repository.save(
                entity=rule_entity, session=session
            )

            return saved_entity

    async def extend(self, pk, **data):
        async with self.uow.begin() as session:
            rule_entity = await self.repository.get(id=pk, session=session)

            if data.get("triggers", []):
                trigger_entities = [
                    TriggerEntity(text=text) for text in data.get("triggers", [])
                ]
                rule_entity.triggers += trigger_entities

            if data.get("reply_options", []):
                reply_option_entities = [
                    ReplyOptionEntity(text=text)
                    for text in data.get("reply_options", [])
                ]
                rule_entity.reply_options += reply_option_entities

            saved_entity = await self.repository.save(
                entity=rule_entity, session=session
            )

            return saved_entity
