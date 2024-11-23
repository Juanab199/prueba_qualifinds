from fastapi import APIRouter


healthz_router = APIRouter(prefix="/v1/healthz")


@healthz_router.get(path="/liveness", tags=["Am I alive?"])
async def live():
    return {"health": "live"}


@healthz_router.get(path="/readiness", tags=["Am I ready?"])
async def ready():
    return {"health": "ready"}