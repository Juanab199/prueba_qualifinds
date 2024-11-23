from fastapi import FastAPI
from app.healthz import healthz_router

from app import SERVICE_VERSION
from app.controller.entrypoint import task_router

app: FastAPI = FastAPI(
    title="Prueba tecnica Inventario",
    description="Se crean y actualizan los productos del inventario",
    docs_url="/v1/docs",
    version=SERVICE_VERSION,
)

app.include_router(task_router)
app.include_router(healthz_router)