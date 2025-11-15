from sqlalchemy.orm import Mapped

from infrastructure.alchemy.db import Base, int_pk


class UniversalReply(Base):
    id: Mapped[int_pk]
    text: Mapped[str]
