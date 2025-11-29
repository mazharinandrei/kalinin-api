from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies import reply_service
from domain.rule_based.rule_based_reply_service import ReplyService
from schemas.message import Message

router = APIRouter(prefix="", tags=["Process message"])


@router.post("/process_message")
async def process_message(
    message: Message,
    service: Annotated[ReplyService, Depends(reply_service)],
) -> dict:
    reply = await service.get_reply(input_message=str(message.text))
    return {"data": reply}
