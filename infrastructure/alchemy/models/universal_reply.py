from sqlalchemy.orm import Mapped

from infrastructure.alchemy.db import Base, int_pk
from schemas.schemas import ReadUniversalReply


class UniversalReply(Base):
    read_schema = ReadUniversalReply
    id: Mapped[int_pk]
    text: Mapped[str]

    def to_read_model(self):
        return self.read_schema(id=self.id, text=self.text)
