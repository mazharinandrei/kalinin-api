from sqlalchemy import select, and_

from infrastructure.alchemy.repositories.crud_repository import SQLAlchemyCRUDRepository


class SQLAlchemyRollDiceRepository(SQLAlchemyCRUDRepository):
    async def get_roll_interpretation(self, session, value):
        stmt = select(self.model).where(
            and_(self.model.start <= value, value <= self.model.end)
        )
        res = await session.execute(stmt)
        entities = [self.mapper.to_entity(row[0]) for row in res.all()]
        return entities
