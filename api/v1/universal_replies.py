from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from api.v1.api_spec import UniversalReplySpec
from dependencies import universal_replies_service
from domain.crud_service import CRUDService
from schemas.universal_replies import CreateUniversalReply

router = APIRouter(prefix="", tags=["Universal replies"])


@router.get("/universal-replies", description=UniversalReplySpec.LIST_DESCRIPTION)
async def list_universal_replies(
    service: Annotated[CRUDService, Depends(universal_replies_service)],
) -> dict:
    res = await service.list()

    return {"data": res}


@router.post("/universal-replies", description=UniversalReplySpec.CREATE_DESCRIPTION)
async def add_universal_reply(
    universal_reply: CreateUniversalReply,
    service: Annotated[CRUDService, Depends(universal_replies_service)],
) -> dict:
    new_obj = await service.create(universal_reply.model_dump())
    return {"data": new_obj}


@router.get(
    "/universal-replies/{reply_id}",
    description=UniversalReplySpec.DETAIL_DESCRIPTION,
)
async def detail_universal_reply(
    reply_id: int,
    service: Annotated[CRUDService, Depends(universal_replies_service)],
) -> dict:
    reply = await service.get(reply_id)

    if reply is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {"data": reply}


@router.patch(
    "/universal-replies/{reply_id}",
    description=UniversalReplySpec.UPDATE_DESCRIPTION,
)
async def update_universal_reply(
    response_id: int,
    universal_reply: CreateUniversalReply,
    service: Annotated[CRUDService, Depends(universal_replies_service)],
) -> dict:
    updated = await service.update(pk=response_id, **universal_reply.model_dump())
    return {"data": updated}


@router.delete(
    "/universal-replies/{reply_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    description=UniversalReplySpec.DELETE_DESCRIPTION,
)
async def delete_universal_reply(
    response_id: int,
    service: Annotated[CRUDService, Depends(universal_replies_service)],
):
    await service.delete(response_id)
