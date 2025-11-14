from sqlalchemy import select

from infrastructure.abstract.abstract_repository import Repository


class SQLAlchemyRepository(Repository):
    def __init__(self, model, session):
        self.model = model
        self.session = session

    async def create(self, **kwargs):
        instance = self.model(**kwargs)
        self.session.add(instance)
        await self.session.commit()
        return instance.to_read_model()

    async def list(self, **kwargs):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def get(self, **kwargs):
        stmt = select(self.model).filter_by(**kwargs)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none().to_read_model()

    async def update(self, pk, **data):
        stmt = select(self.model).filter_by(id=pk).with_for_update(nowait=True)
        res = await self.session.execute(stmt)
        instance = res.scalar_one_or_none()

        for field, value in data.items():
            setattr(instance, field, value)

        await self.session.commit()
        return instance.to_read_model()

    async def delete(self, pk):
        stmt = select(self.model).filter_by(id=pk)
        res = await self.session.execute(stmt)
        instance = res.scalar_one_or_none()

        await self.session.delete(instance)
        await self.session.commit()
