from sqlalchemy import select

from domain.enities.rule import RuleEntity
from infrastructure.alchemy.models.rule import Trigger, ReplyOption
from infrastructure.alchemy.repositories.crud_repository import SQLAlchemyCRUDRepository


class SQLAlchemyRuleRepository(SQLAlchemyCRUDRepository):

    async def bulk_get_or_create(self, model, entities):
        """
        упоминается поле text, которого не должно быть
        """
        orms = []

        existing_orms = await self.session.execute(
            select(model).where(model.text.in_([entity.text for entity in entities]))
        )

        existing_orms = existing_orms.scalars()

        orms_by_text = {
            existing_trigger.text: existing_trigger
            for existing_trigger in existing_orms
        }

        for entity in entities:
            if entity.text in orms_by_text:
                orms.append(orms_by_text[entity.text])
            else:
                orms.append(model(text=entity.text))

        return orms

    async def save(self, entity: RuleEntity):

        rule_orm = self.model()
        rule_orm.triggers = await self.bulk_get_or_create(
            entities=entity.triggers, model=Trigger
        )
        rule_orm.reply_options = await self.bulk_get_or_create(
            model=ReplyOption, entities=entity.reply_options
        )

        self.session.add(rule_orm)

        await self.session.commit()

        return entity

    async def update(self, **kwargs):
        raise NotImplementedError("рано ещё!")
