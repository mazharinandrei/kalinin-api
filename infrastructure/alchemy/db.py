import re
import uuid
from datetime import datetime
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from config import settings

engine = create_async_engine(url=settings.db_url, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# настройка аннотаций
int_pk = Annotated[int, mapped_column(primary_key=True)]
uuid_pk = Annotated[uuid.UUID, mapped_column(primary_key=True, default=uuid.uuid4)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[
    datetime,
    mapped_column(server_default=func.now(), onupdate=datetime.now),
]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """Автоматическое название таблицы, название модели в множественном числе.
        Разделяет слова с большой буквы и соединяет в нижнем регистре с '_'.
        """
        substrings = re.findall("[A-Z][^A-Z]*", cls.__name__)
        name = "_".join(substrings)

        if name[-1] == "y":
            return f"{name.lower()[:-1]}ies"

        return f"{name.lower()}s"

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
