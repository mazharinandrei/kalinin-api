from contextlib import asynccontextmanager
from dataclasses import dataclass

from domain.abstract_uow import UnitOfWork
from infrastructure.alchemy.db import async_session_maker


@dataclass
class AlchemyUnitOfWork(UnitOfWork):
    session_maker = async_session_maker
    session = None

    @asynccontextmanager
    async def begin(self):
        try:
            self.session = self.session_maker()
            yield self.session
            await self.commit()
        except Exception as e:  # noqa: E722
            print(e)
            await self.rollback()
        finally:
            await self.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

    async def close(self):
        await self.session.close()
