from dataclasses import dataclass

from domain.abstract_repository import Repository
from domain.abstract_uow import UnitOfWork


@dataclass
class CRUDService:
    repository: Repository
    uow: UnitOfWork

    async def create(self, data: dict):
        async with self.uow.begin() as session:
            res = await self.repository.create(session, **data)
            return res

    async def list(self):
        async with self.uow.begin() as session:
            res = await self.repository.list(session=session)
            return res

    async def get(self, pk):
        async with self.uow.begin() as session:
            res = await self.repository.get(id=pk, session=session)
            return res

    async def update(self, pk, **data):
        async with self.uow.begin() as session:
            res = await self.repository.update(pk=pk, session=session, **data)
            return res

    async def delete(self, pk):
        async with self.uow.begin() as session:
            res = await self.repository.delete(pk=pk, session=session)
            return res
