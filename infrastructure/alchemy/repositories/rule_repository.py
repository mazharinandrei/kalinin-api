from sqlalchemy import select

from domain.enities.rule import RuleEntity
from infrastructure.alchemy.models.rule import Trigger, ReplyOption
from infrastructure.alchemy.repositories.crud_repository import SQLAlchemyCRUDRepository


class SQLAlchemyRuleRepository(SQLAlchemyCRUDRepository):

    async def _bulk_get_or_create(self, model, entities, unique_field):

        orm_objects = []

        existing_orm_objects = await self.session.execute(
            select(model).where(
                getattr(model, unique_field).in_(
                    [getattr(entity, unique_field) for entity in entities]
                )
            )
        )

        existing_orm_objects = existing_orm_objects.scalars()

        orm_objects_by_unique_field = {
            getattr(existing_object, unique_field): existing_object
            for existing_object in existing_orm_objects
        }

        for entity in entities:
            if getattr(entity, unique_field) in orm_objects_by_unique_field:
                orm_objects.append(
                    orm_objects_by_unique_field[getattr(entity, unique_field)]
                )
            else:
                orm_objects.append(
                    model(**{unique_field: getattr(entity, unique_field)})
                )

        return orm_objects

    async def save(self, entity: RuleEntity):

        rule_orm = self.model()
        rule_orm.triggers = await self._bulk_get_or_create(
            entities=entity.triggers, model=Trigger, unique_field="text"
        )
        rule_orm.reply_options = await self._bulk_get_or_create(
            model=ReplyOption, entities=entity.reply_options, unique_field="text"
        )

        self.session.add(rule_orm)

        await self.session.commit()

        return entity

    async def update(self, **kwargs):
        raise NotImplementedError("рано ещё!")
