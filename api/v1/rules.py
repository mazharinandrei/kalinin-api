from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from dependencies import rules_service
from domain.rules import RuleService
from schemas.rules import CreateRule, ExtendRule

router = APIRouter(prefix="", tags=["Rules"])


@router.get("/rules")
async def list_rules(
    service: Annotated[RuleService, Depends(rules_service)],
) -> dict:
    res = await service.list()

    return {"data": res}


@router.get("/rules/{rule_id}")
async def detail_rule(
    rule_id: int, service: Annotated[RuleService, Depends(rules_service)]
) -> dict:
    rule = await service.get(rule_id)

    if rule is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {"data": rule}


@router.post("/rules")
async def add_rule(
    rule: CreateRule,
    service: Annotated[RuleService, Depends(rules_service)],
) -> dict:
    new_obj = await service.create(rule.model_dump())
    return {"data": new_obj}


@router.put("/rules/{rule_id}")
async def update_rule(
    rule_id: int,
    rule: CreateRule,
    service: Annotated[RuleService, Depends(rules_service)],
) -> dict:
    updated = await service.update(pk=rule_id, **rule.model_dump())
    return {"data": updated}


@router.patch("/rules/{rule_id}")
async def extend_rule(
    rule_id: int,
    rule: ExtendRule,
    service: Annotated[RuleService, Depends(rules_service)],
) -> dict:
    updated = await service.extend(pk=rule_id, **rule.model_dump())
    return {"data": updated}


@router.delete("/rules/{rule_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rule(
    rule_id: int,
    service: Annotated[RuleService, Depends(rules_service)],
):
    await service.delete(rule_id)
