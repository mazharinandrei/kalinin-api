from abc import ABC, abstractmethod


class AbstractSQLAlchemyMapper(ABC):

    @staticmethod
    @abstractmethod
    def to_entity(model): ...
