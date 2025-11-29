import uvicorn
from fastapi import APIRouter, FastAPI

from api.v1.process_message import router as reply_router_v1
from api.v1.rules import router as rules_router_v1
from api.v1.universal_replies import router as universal_router_v1

app = FastAPI(title="🤖Kalinin API")

router_v1 = APIRouter(prefix="/v1")

router_v1.include_router(reply_router_v1)
router_v1.include_router(rules_router_v1)
router_v1.include_router(universal_router_v1)

app.include_router(router_v1)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
