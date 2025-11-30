from collections.abc import Iterable, Mapping

from sqlalchemy import insert, select

from domain.abstract_repository import Repository


class SQLAlchemyCRUDRepository(Repository):
    def __init__(self, model, mapper):
        self.model = model
        self.mapper = mapper

    async def create(self, session, **kwargs):
        instance = self.model(**kwargs)
        session.add(instance)

        await session.flush()

        entity = self.mapper.to_entity(instance)
        return entity

    async def bulk_create(
        self,
        session,
        objects: Iterable[Mapping],
    ):
        created = await session.execute(
            insert(self.model).returning(self.model),
            objects,
        )

        await session.flush()

        entities = [
            await self.mapper.to_entity(instance[0]) for instance in created.all()
        ]
        return entities

    async def list(self, session, **kwargs):
        stmt = select(self.model)
        res = await session.execute(stmt)
        entities = [self.mapper.to_entity(row[0]) for row in res.all()]
        return entities

    async def get(self, session, **kwargs):
        stmt = select(self.model).filter_by(**kwargs)
        res = await session.execute(stmt)
        res = res.scalar_one_or_none()
        if res:
            entity = self.mapper.to_entity(res)
            return entity
        return None

    async def update(self, session, pk, **data):
        stmt = select(self.model).filter_by(id=pk).with_for_update(nowait=True)
        res = await session.execute(stmt)
        instance = res.scalar_one_or_none()

        for field, value in data.items():
            setattr(instance, field, value)

        entity = self.mapper.to_entity(instance)
        return entity

    async def delete(self, session, pk):
        stmt = select(self.model).filter_by(id=pk)
        res = await session.execute(stmt)
        instance = res.scalar_one_or_none()

        await session.delete(instance)

    async def save(self, session, entity):
        raise NotImplementedError("пока не создал")
