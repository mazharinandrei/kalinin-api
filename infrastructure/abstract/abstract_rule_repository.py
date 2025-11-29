from abc import abstractmethod

from domain.enities.rule import RuleEntity
from domain.enities.trigger import TriggerEntity
from infrastructure.abstract.abstract_repository import Repository


class RuleRepository(Repository):
    @abstractmethod
    async def find_by_triggers(self, triggers: list[TriggerEntity]) -> list[RuleEntity]: ...
