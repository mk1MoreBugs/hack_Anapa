from fastapi import APIRouter

from app.api.routers import platform, organizer, booking

api_router = APIRouter()

api_router.include_router(platform.router)
api_router.include_router(organizer.router)
api_router.include_router(booking.router)
