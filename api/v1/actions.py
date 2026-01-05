from typing import Annotated

from fastapi import APIRouter, Depends

from api.v1.api_spec import ProcessMessageSpec
from dependencies import reply_service
from domain.rule_based_replies.rule_based_reply_service import ReplyService
from schemas.message import Message

router = APIRouter(prefix="", tags=["Actions"])


@router.post(
    "/messages",
    responses=ProcessMessageSpec.RESPONSES,
    description=ProcessMessageSpec.DESCRIPTION,
)
async def process_message(
    message: Message,
    service: Annotated[ReplyService, Depends(reply_service)],
) -> dict:
    reply = await service.get_reply(input_message=str(message.text))
    return {"data": reply}
