from typing import Annotated

from fastapi import APIRouter, Depends

from api.v1.api_spec import ProcessMessageSpec
from dependencies import reply_service, roll_dice_service, brick_translate_service
from domain.roll_dice.roll_dice_service import RollDiceService
from domain.rule_based_replies.rule_based_reply_service import ReplyService
from domain.translate_brick.brick_translate_service import BrickTranslateService
from schemas.message import Message
from schemas.translate import BrickTranslateInput

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


@router.get("/roll_dice")
async def roll_dice(
    service: Annotated[RollDiceService, Depends(roll_dice_service)],
    user_id: str | None = None,
) -> dict:
    roll = await service.roll()
    return {"data": roll}


@router.post("/brick-translate")
async def translate_to_brick(
    data: BrickTranslateInput,
    service: Annotated[BrickTranslateService, Depends(brick_translate_service)],
) -> dict:
    result = await service.translate(dialect=data.dialect, text=data.input_text)
    return {"data": result}
