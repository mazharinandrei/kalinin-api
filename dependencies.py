from domain.crud import CRUDService
from infrastructure.alchemy.db import async_session_maker
from infrastructure.alchemy.models.universal_reply import UniversalReply
from infrastructure.alchemy.repository import SQLAlchemyRepository


def universal_replies_service() -> CRUDService:
    return CRUDService(
        repository=SQLAlchemyRepository(
            model=UniversalReply, session=async_session_maker()
        )
    )
