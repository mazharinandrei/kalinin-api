from dataclasses import dataclass
from infrastructure.abstract.abstract_repository import Repository


@dataclass
class CRUDService:
    repository: Repository

    async def create(self, data: dict):
        res = await self.repository.create(**data)
        # вынес .to_read_model() из репозитория,
        # так как этот метод ломает создание Rule
        # текущее решение - неправильное, так как создаёт зависимость от модели sqlalchemy
        return res.to_read_model()

    async def list(self):
        res = await self.repository.list()
        return res

    async def get(self, pk):
        res = await self.repository.get(id=pk)
        return res

    async def update(self, pk, **data):
        res = await self.repository.update(pk=pk, **data)
        return res

    async def delete(self, pk):
        res = await self.repository.delete(pk=pk)
        return res
