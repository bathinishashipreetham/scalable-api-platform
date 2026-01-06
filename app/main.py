from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version,
    description="Production-grade backend system built with FastAPI",
)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
