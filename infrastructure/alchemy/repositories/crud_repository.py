from typing import Iterable, Mapping

from sqlalchemy import select, insert

from infrastructure.abstract.abstract_repository import Repository


class SQLAlchemyCRUDRepository(Repository):
    def __init__(self, model, session, mapper):
        self.model = model
        self.session = session
        self.mapper = mapper

    async def create(self, commit: bool = True, **kwargs):
        instance = self.model(**kwargs)
        self.session.add(instance)

        if commit:
            await self.session.commit()

        else:
            await self.session.flush()

        entity = await self.mapper.to_entity(instance)
        return entity

    async def bulk_create(self, objects: Iterable[Mapping], commit: bool = True):

        created = await self.session.execute(
            insert(self.model).returning(self.model), objects
        )

        if commit:
            await self.session.commit()
        else:
            await self.session.flush()

        entities = [
            await self.mapper.to_entity(instance[0]) for instance in created.all()
        ]
        return entities

    async def list(self, **kwargs):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        entities = [self.mapper.to_entity(row[0]) for row in res.all()]
        return entities

    async def get(self, **kwargs):
        stmt = select(self.model).filter_by(**kwargs)
        res = await self.session.execute(stmt)
        res = res.scalar_one_or_none()
        if res:
            entity = self.mapper.to_entity(res)
            return entity
        return None

    async def update(self, pk, **data):
        stmt = select(self.model).filter_by(id=pk).with_for_update(nowait=True)
        res = await self.session.execute(stmt)
        instance = res.scalar_one_or_none()

        for field, value in data.items():
            setattr(instance, field, value)

        await self.session.commit()
        entity = await self.mapper.to_entity(instance)
        return entity

    async def delete(self, pk):
        stmt = select(self.model).filter_by(id=pk)
        res = await self.session.execute(stmt)
        instance = res.scalar_one_or_none()

        await self.session.delete(instance)
        await self.session.commit()
