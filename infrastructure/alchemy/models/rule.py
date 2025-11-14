from typing import List

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from schemas.schemas import ReadTrigger, ReadReplyOption, ReadRule
from infrastructure.alchemy.db import Base, int_pk


class Trigger(Base):
    read_schema = ReadTrigger
    id: Mapped[int_pk]
    text: Mapped[str]

    def to_read_model(self):
        return self.read_schema(id=self.id, text=self.text)


class ReplyOption(Base):
    read_schema = ReadReplyOption
    id: Mapped[int_pk]
    text: Mapped[str]

    def to_read_model(self):
        return self.read_schema(id=self.id, text=self.text)


rule_triggers = Table(
    "rule_triggers",
    Base.metadata,
    Column("rule_id", ForeignKey("rules.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "trigger_id", ForeignKey("triggers.id", ondelete="CASCADE"), primary_key=True
    ),
)

rule_reply_options = Table(
    "rule_reply_options",
    Base.metadata,
    Column("rule_id", ForeignKey("rules.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "reply_option_id",
        ForeignKey("reply_options.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class Rule(Base):
    read_schema = ReadRule
    id: Mapped[int_pk]
    triggers: Mapped[List[Trigger]] = relationship(
        "Trigger",
        secondary=rule_triggers,
        passive_deletes=True,
        lazy="selectin",
        cascade="all",
    )

    reply_options: Mapped[List[ReplyOption]] = relationship(
        "ReplyOption",
        secondary=rule_reply_options,
        passive_deletes=True,
        lazy="selectin",
        cascade="all",
    )

    def to_read_model(self):
        return self.read_schema(
            id=self.id,
            triggers=[trigger.text for trigger in self.triggers],
            reply_options=[response.text for response in self.reply_options],
        )
