from dataclasses import dataclass

from domain.enities.reply_option import ReplyOptionEntity
from domain.enities.trigger import TriggerEntity


@dataclass
class RuleEntity:

    triggers: list[TriggerEntity]
    reply_options: list[ReplyOptionEntity]

    id: int | None = None
