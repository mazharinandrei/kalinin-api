from fastapi import APIRouter

from api.v1.process_message import router as reply_router_v1
from api.v1.rules import router as rules_router_v1
from api.v1.universal_replies import router as universal_router_v1

router_v1 = APIRouter(prefix="/v1")

router_v1.include_router(reply_router_v1)
router_v1.include_router(rules_router_v1)
router_v1.include_router(universal_router_v1)
