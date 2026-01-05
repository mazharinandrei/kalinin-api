from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.alchemy.db import Base, int_pk


class RollDiceRange(Base):
    id: Mapped[int_pk]
    start: Mapped[int]
    end: Mapped[int]
    text: Mapped[str] = mapped_column(unique=True)
