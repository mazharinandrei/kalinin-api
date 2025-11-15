from dataclasses import dataclass

from domain.crud import CRUDService
from domain.enities.rule import RuleEntity
from infrastructure.abstract.abstract_repository import Repository
from infrastructure.alchemy.models.rule import Rule


@dataclass
class RuleService(CRUDService):
    trigger_repository: Repository
    reply_option_repository: Repository

    async def create(self, data: dict):
        triggers = await self.trigger_repository.bulk_create(
            objects=[{"text": trigger} for trigger in data["triggers"]], commit=False
        )

        reply_options = await self.reply_option_repository.bulk_create(
            objects=[{"text": option} for option in data["reply_options"]], commit=False
        )

        rule = RuleEntity(triggers=triggers, reply_options=reply_options)

        rule.triggers = triggers
        rule.reply_options = reply_options

        orm_rule = await self.repository.mapper.to_orm(rule)
        self.repository.session.add(orm_rule)
        await self.repository.session.commit()

        return rule

    async def update(self, pk, **data):

        raise NotImplementedError("рано ещё!")
