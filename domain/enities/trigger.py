from dataclasses import dataclass


@dataclass
class TriggerEntity:
    text: str
    id: int | None = None
