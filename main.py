import uvicorn
from fastapi import FastAPI

from api.v1.router import router_v1

app = FastAPI(title="🤖Kalinin API")

app.include_router(router_v1)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
