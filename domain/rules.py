from dataclasses import dataclass

from domain.crud import CRUDService
from infrastructure.abstract.abstract_repository import Repository


@dataclass
class RuleService(CRUDService):
    trigger_repository: Repository
    reply_option_repository: Repository

    async def create(self, data: dict):
        for trigger in data["triggers"]:
            print("trigger: ", trigger)
        for option in data["reply_options"]:
            print("option: ", option)

        triggers = await self.trigger_repository.bulk_create(
            objects=[{"text": trigger} for trigger in data["triggers"]], commit=False
        )

        reply_options = await self.reply_option_repository.bulk_create(
            objects=[{"text": option} for option in data["reply_options"]], commit=False
        )

        rule = await self.repository.create(commit=False)

        rule.triggers = triggers
        rule.reply_options = reply_options

        await self.repository.session.commit()

        raise NotImplementedError("рано ещё!")

    async def update(self, pk, **data):

        raise NotImplementedError("рано ещё!")
