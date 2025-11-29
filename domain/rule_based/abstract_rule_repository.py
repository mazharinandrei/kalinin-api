from abc import abstractmethod

from domain.abstract_repository import Repository
from domain.enities.rule import RuleEntity
from domain.enities.trigger import TriggerEntity


class RuleRepository(Repository):
    @abstractmethod
    async def find_by_triggers(self, triggers: list[TriggerEntity]) -> list[RuleEntity]: ...
