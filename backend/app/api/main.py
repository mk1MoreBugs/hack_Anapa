from fastapi import APIRouter

from app.api.routes import platform, organizer

api_router = APIRouter()

api_router.include_router(platform.router)
api_router.include_router(organizer.router)
