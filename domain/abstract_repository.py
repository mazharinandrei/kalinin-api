from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    async def bulk_create(self, session, objects: list[dict]):
        raise NotImplementedError

    @abstractmethod
    async def create(self, session, commit: bool = True, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def list(self, session, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get(self, session, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update(self, session, pk, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, session, pk):
        raise NotImplementedError

    @abstractmethod
    async def save(self, session, entity): ...
