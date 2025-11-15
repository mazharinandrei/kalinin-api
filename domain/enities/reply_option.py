from dataclasses import dataclass


@dataclass
class ReplyOptionEntity:
    text: str
    id: int | None = None
