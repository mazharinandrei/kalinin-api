from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from api.v1.api_spec import RollDiceSpec
from dependencies import roll_dice_service
from domain.roll_dice.roll_dice_service import RollDiceService
from schemas.roll_dice_range import CreateRollDiceRange

router = APIRouter(prefix="", tags=["Roll Dice Ranges"])


@router.get("/roll_dice_ranges", description=RollDiceSpec.LIST_DESCRIPTION)
async def list_roll_dice_ranges(
    service: Annotated[RollDiceService, Depends(roll_dice_service)],
) -> dict:
    res = await service.list()

    return {"data": res}


@router.get("/roll_dice_ranges/{range_id}", description=RollDiceSpec.DETAIL_DESCRIPTION)
async def detail_roll_dice_range(
    range_id: int,
    service: Annotated[RollDiceService, Depends(roll_dice_service)],
) -> dict:
    roll_dice_range = await service.get(range_id)

    if roll_dice_range is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {"data": roll_dice_range}


@router.post("/roll_dice_ranges", description=RollDiceSpec.CREATE_DESCRIPTION)
async def add_roll_dice_range(
    roll_dice_range: CreateRollDiceRange,
    service: Annotated[RollDiceService, Depends(roll_dice_service)],
) -> dict:
    new_obj = await service.create(roll_dice_range.model_dump())
    return {"data": new_obj}


@router.put("/roll_dice_ranges/{range_id}", description=RollDiceSpec.UPDATE_DESCRIPTION)
async def update_roll_dice_range(
    range_id: int,
    roll_dice_range: CreateRollDiceRange,
    service: Annotated[RollDiceService, Depends(roll_dice_service)],
) -> dict:
    updated = await service.update(pk=range_id, **roll_dice_range.model_dump())
    return {"data": updated}


@router.delete(
    "/roll_dice_ranges/{range_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    description=RollDiceSpec.DELETE_DESCRIPTION,
)
async def delete_roll_dice_range(
    range_id: int,
    service: Annotated[RollDiceService, Depends(roll_dice_service)],
):
    await service.delete(range_id)
