from abc import abstractmethod, ABC


class Repository(ABC):

    @abstractmethod
    async def create(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    async def list(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    async def get(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    async def update(self, pk, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, pk):
        raise NotImplementedError()
