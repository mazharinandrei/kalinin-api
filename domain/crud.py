from dataclasses import dataclass

from infrastructure.abstract.abstract_repository import Repository


@dataclass
class CRUDService:
    repository: Repository

    async def create(self, data: dict):
        res = await self.repository.create(**data)
        return res

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
