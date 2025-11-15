from abc import abstractmethod, ABC


class AbstractSQLAlchemyMapper(ABC):

    @staticmethod
    @abstractmethod
    def to_entity(model): ...

    @staticmethod
    @abstractmethod
    def to_orm(entity): ...
