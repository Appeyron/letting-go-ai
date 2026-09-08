from fastapi import FastAPI

from backend.database.init_db import create_tables

from backend.routers import life_areas
from backend.routers import conversations
from backend.routers import consciousness
from backend.routers import assessments

create_tables()

app = FastAPI(
    title="Letting Go AI API",
    description=(
        "Backend API for an AI chatbot inspired by "
        "David R. Hawkins' Letting Go: The Path of Surrender."
    ),
    version="0.1.0",
)


@app.get("/", tags=["System"])
async def root():
    return {
        "message": "Letting Go AI API is running",
        "version": "0.1.0"
    }


@app.get("/health", tags=["System"])
async def health_check():
    return {
        "status": "healthy"
    }


app.include_router(life_areas.router)
app.include_router(conversations.router)
app.include_router(consciousness.router)
app.include_router(assessments.router)