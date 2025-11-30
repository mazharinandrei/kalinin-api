from abc import ABC, abstractmethod


class UnitOfWork(ABC):
    @abstractmethod
    def begin(self): ...

    @abstractmethod
    def commit(self): ...

    @abstractmethod
    def rollback(self): ...

    @abstractmethod
    def close(self): ...
