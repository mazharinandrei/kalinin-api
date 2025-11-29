from sqlalchemy import select, or_, func
from sqlalchemy.orm import joinedload

from domain.enities.rule import RuleEntity
from domain.enities.trigger import TriggerEntity
from infrastructure.abstract.abstract_rule_repository import RuleRepository
from infrastructure.alchemy.models.rule import Trigger, ReplyOption, Rule
from infrastructure.alchemy.repositories.crud_repository import SQLAlchemyCRUDRepository


class SQLAlchemyRuleRepository(RuleRepository, SQLAlchemyCRUDRepository):

    async def find_by_triggers(self, triggers: list[TriggerEntity]) -> tuple[RuleEntity]:
        patterns = triggers

        conditions = [
            func.lower(pattern).like('%' + func.lower(Trigger.text) + '%')
            for pattern in patterns
        ]

        stmt = (
            select(Rule)
            .join(Rule.triggers)
            .join(Rule.reply_options)
            .options(
                joinedload(Rule.triggers),
                joinedload(Rule.reply_options),
            )
            .where(or_(*conditions))
            .distinct()
        )

        result = await self.session.scalars(stmt)
        result = result.unique().all()
        return tuple(self.mapper.to_entity(orm) for orm in result)

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

        if entity.id:
            rule_orm = await self.session.execute(
                select(self.model).filter_by(id=entity.id)
            )
            rule_orm = rule_orm.scalar_one_or_none()

        else:
            rule_orm = self.model()

        rule_orm.triggers = await self._bulk_get_or_create(
            entities=entity.triggers, model=Trigger, unique_field="text"
        )
        rule_orm.reply_options = await self._bulk_get_or_create(
            model=ReplyOption, entities=entity.reply_options, unique_field="text"
        )

        self.session.add(rule_orm)

        await self.session.commit()

        return self.mapper.to_entity(rule_orm)

    async def update(self, **kwargs):
        raise NotImplementedError("That repo only supports the save method")
